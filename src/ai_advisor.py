import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Get API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file.")

# Create Groq client
client = Groq(api_key=GROQ_API_KEY)


def get_financial_advice(financial_summary):
    """
    Generate AI-powered financial advice.
    """

    prompt = f"""
You are a professional financial advisor.

Analyze the user's financial data and provide:

1. Financial Health Score (out of 10)
2. Spending Analysis
3. Budget Suggestions
4. Saving Tips
5. Risk Analysis
6. 30-Day Action Plan

User Financial Data:

{financial_summary}

Keep the advice simple, practical, and actionable.
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert financial advisor."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
            max_tokens=700
        )

        # Return only the generated text
        return response.choices[0].message.content

    except Exception as e:
        return f"Error occurred: {e}"