import json
import os

# Load the emergency numbers dataset once at import time
_DATA_PATH = os.path.join(os.path.dirname(__file__), "services", "emergency_numbers.json")

with open(_DATA_PATH, "r") as f:
    _EMERGENCY_DATA = json.load(f)

# Tool schema — describes the function to the LLM
TOOL_SCHEMA = {
    "name": "lookup_emergency_number",
    "description": (
        "Look up the emergency phone number for a specific service in a given country. "
        "Use ISO alpha-2 country codes (e.g. 'US' for United States, 'JP' for Japan, "
        "'IN' for India). Available services include: police, ambulance, fire, general_emergency."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "country": {
                "type": "string",
                "description": "ISO alpha-2 country code, e.g. 'US', 'JP', 'IN'"
            },
            "service": {
                "type": "string",
                "description": "Emergency service type: police, ambulance, fire, or general_emergency"
            }
        },
        "required": ["country", "service"]
    }
}


def lookup_emergency_number(country: str, service: str) -> str | None:
    """
    Look up an emergency number from the local dataset.
    Never raises — returns None for any invalid or unknown input.
    """
    try:
        if not isinstance(country, str) or not isinstance(service, str):
            return None

        country = country.strip().upper()
        service = service.strip().lower()

        country_data = _EMERGENCY_DATA.get(country)
        if not country_data:
            return None

        default = country_data.get("default", {})
        number = default.get(service)

        if not number:
            return None

        return str(number)

    except Exception:
        return None
