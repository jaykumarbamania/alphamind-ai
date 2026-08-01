from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def analyze_stock(data):
    
    prompt=f"""
You are a professional equity research analyst.

Analyze this company.

{data}

Return

1 Executive Summary

2 Strengths

3 Weaknesses

4 Growth Drivers

5 Risks

6 Valuation Opinion

7 Final Recommendation

Give markdown response.
"""

    response=client.chat.completions.create(

        model="gpt-4.1",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content