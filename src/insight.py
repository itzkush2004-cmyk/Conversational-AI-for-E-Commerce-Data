import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

INSIGHT_PROMPT = """
You are a senior data analyst. Given a business question and its query result, write a 2-3 sentence plain English insight.
Rules:
- Use the actual numbers from the result
- Round numbers to 2 decimal places where relevant
- Add one business recommendation or observation at the end
- Be concise and direct — no fluff
- Do not mention SQL or databases
"""

def generate_insight(question: str, result: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": INSIGHT_PROMPT},
            {"role": "user", "content": f"Question: {question}\n\nResult:\n{result}"}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()