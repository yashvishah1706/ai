import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq()
MODEL = "qwen/qwen3.8-27b"

PROMPT = """Generate a short subject line (under 10 words) for this help request. Only return the subject line, nothing else. Do not start with 'Subject:'."""

CONTROL_PROMPT = """Generate a subject line."""

GOLDEN = [
    ("I need help finding a job in software engineering", "job"),
    ("My apartment has a plumbing leak and no heat", "plumbing"),
    ("I cannot afford my rent this month", "rent"),
    ("My car broke down and I need help with repairs", "car"),
    ("I need food assistance for my family", "food"),
    ("I am looking for a tutor for my child in math", "tutor"),
    ("I need help with my immigration paperwork", "immigration"),
    ("My electricity was shut off and I have kids at home", "electricity"),
    ("I need help paying my medical bills", "medical"),
    ("I lost my job and need unemployment help", "unemployment"),
    ("I need a lawyer for my custody case", "custody"),
    ("My landlord is not fixing the heat", "heat"),
    ("I need help learning English", "english"),
    ("I am homeless and need shelter", "shelter"),
    ("I need help with my taxes", "tax"),
    ("My child needs school supplies", "school"),
    ("I need transportation to my doctor appointments", "transport"),
    ("I need help with my water bill", "water"),
    ("I am a veteran and need benefits help", "veteran"),
    ("I need childcare assistance", "child"),
    ("My phone was disconnected and I need help", "phone"),
    ("I need help applying for food stamps", "food"),
    ("I need someone to help me move", "mov"),
    ("I need help with funeral expenses", "funeral"),
    ("I need a wheelchair ramp for my home", "wheelchair"),
    ("I need help with domestic violence resources", "domestic"),
    ("I need help with my student loans", "loan"),
    ("I need help finding affordable housing", "hous"),
    ("I need help with my social security application", "social"),
    ("I need mental health counseling", "mental"),
]

def score_prompt(prompt):
    correct = 0
    for description, keyword in GOLDEN:
        r = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": description}
            ],
            max_tokens=20,
            temperature=0.1
        )
        result = r.choices[0].message.content.strip().lower()
        if keyword.lower() in result:
            correct += 1
    return {"score": correct / len(GOLDEN), "correct": correct, "total": len(GOLDEN)}

def run(prompt=PROMPT):
    return score_prompt(prompt)

if __name__ == "__main__":
    print("Scoring good prompt...")
    good = score_prompt(PROMPT)
    print(f"Good prompt: {good['correct']}/{good['total']} = {good['score']:.2f}")

    print("Scoring control prompt...")
    bad = score_prompt(CONTROL_PROMPT)
    print(f"Control prompt: {bad['correct']}/{bad['total']} = {bad['score']:.2f}")

    if good["score"] > bad["score"]:
        print("✅ Good prompt beats control")
    else:
        print("❌ Control prompt won — check your prompts")
