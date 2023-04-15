import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = []

while True :
    user_content = input("user : ")
    messages.append({"role": "user", "content": f"{user_content}"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)

    assistant_content = completion.choices[0].message["content"].strip()
    messages.append({"role": "assistant", "content": f"{user_content}"})

    print(f"chatGPT : {assistant_content}")
