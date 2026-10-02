"""
Fill in each answer, then run:  python onboarding_check.py

Short answers are fine. The point is that you looked, not that you memorised.
"""

# --- Mission 2: reading the code -------------------------------------------

# Which file defines the category taxonomy the classifier chooses from?
# Give the path relative to the repo root, e.g. "utils/example.py"
TAXONOMY_FILE = "utils/categories.py"

# How many TOP LEVEL categories are there? (an integer)
# Hint: utils/predict_category_list.py has a helper that returns them.
TOP_LEVEL_COUNT = 7

# What is the name of the function in lambda_function.py that handles
# category prediction requests?
PREDICT_HANDLER = "predict_category_handler"


# --- Mission 2.5: the architecture ------------------------------------------

# lambda_function.py has a unified router, lambda_handler, which picks a service
# out of the request and calls that service's handler. How many services can it
# dispatch to? (an integer). ARCHITECTURE_MAP.md draws this.
ROUTER_SERVICE_COUNT = 5

# Name one CONTRACT test from tests/ that you read. The test function name is
# enough, e.g. "test_something"; a full "tests/test_file.py::test_something"
# also works. docs/testing/TEST_CATALOGUE.md says which files are contract
# tests.
CONTRACT_TEST = "test_predict_returns_ranked_objects_under_categories"

# In your own words: what behaviour does that test protect, and what would
# break for the web client if it started failing?
CONTRACT_TEST_PROTECTS = "Ensures the predict_category endpoint always returns category_name, category_number, confidence and hierarchy fields. If it failed, the web client would break because it maps over exactly these 4 fields to render results to the user."



# --- Mission 3: the incident ------------------------------------------------

# In one sentence: why did a single upstream change break several services
# at once?
INCIDENT_ROOT_CAUSE = "All services shared the same model client in utils/client.py, so when the upstream model was retired, every service depending on it failed simultaneously."

# Name ONE change that would have reduced the impact.
INCIDENT_PREVENTION = "Add monitoring to alert when classification consistently returns General Category instead of specific categories."


# --- Mission 4: tools -------------------------------------------------------

# You measured the tool path against asking the model directly. For a lookup
# over 73 fixed rows, does a model belong in the request path at all? Say what
# you measured and what you concluded. Disagreeing with the README is fine if
# you show your numbers.
TOOL_VS_DIRECT = "The tool path is slower (2 model calls + function call) vs asking directly (1 call), but the tool path returns verified numbers from a real dataset. Asking the model directly risks hallucinated numbers as seen with the 555 block example in the README. For 73 fixed rows, a model does not belong in the request path — a direct dataset lookup is faster, cheaper, and guaranteed correct."


# --- Mission 6: grounding (elective) ----------------------------------------

# Your grounded search returns fewer organizations than the current one, and
# some queries return none. Explain that to somebody who wanted six results.
GROUNDING_TRADEOFF = ""


# --- Mission 5: evaluation --------------------------------------------------

# Which metric did you choose, and what does it fail to capture? Every metric
# is wrong about something; name yours.
EVAL_METRIC = "Keyword match — checks if a relevant word appears in the subject line. It fails to capture whether the subject is grammatically correct, appropriately concise, or avoids sounding like a diagnosis. A subject containing the keyword but phrased badly would still pass."


# --- Your own observations and feedback -------------------------------------

# Run a few descriptions through the harness. Write 3+ sentences on something
# that surprised you, confused you, or looked wrong.
OBSERVATIONS = "The subject line heavily influences classification — the same plumbing description returned empty with subject Water leak but correct results with Home repair. The car example consistently returned General Category which is correct since the description is too ambiguous. Plumbing took 3 model calls at depth 0-1-2 while ambiguous requests stopped at depth 0 with 1 call."

# Something in this onboarding that was unclear, broken, or could be better.
# Genuinely useful to us. "Nothing" is a valid answer only if you mean it.
FEEDBACK = "The Python version requirement of 3.11+ is not explicitly stated in the README — hit a TypeError on Python 3.9 before figuring out the issue."
