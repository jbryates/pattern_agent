from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-5-mini", 
    messages=[
        {"role": "system", "content": "Explain what an AI agent is in one sentence."},
        ],
    )

print(response.choices[0].message.content)
