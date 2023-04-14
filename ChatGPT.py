import openai
openai.api_key = "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"

messages = []

while True :
    user_content = input("user : ")
    messages.append({"role": "user", "content": f"{user_content}"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)

    assistant_content = completion.choices[0].message["content"].strip()
    messages.append({"role": "assistant", "content": f"{user_content}"})

    print(f"chatGPT : {assistant_content}")
