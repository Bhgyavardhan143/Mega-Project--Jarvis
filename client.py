from openai import OpenAI


client = OpenAI(
    api_key="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"
)
completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud "},
        {"role": "user", "content":""}
    ]
)