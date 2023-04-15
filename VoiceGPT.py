import os
import openai
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr

openai.api_key = os.getenv("OPENAI_API_KEY")
language = "ko"

messages = []

def getChatGPT(userContent):
    # try:
        messages.append({"role": "user", "content": f"{userContent}"})

        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)

        assistantContent = completion.choices[0].message["content"].strip()
        messages.append({"role": "assistant", "content": f"{userContent}"})

        return assistantContent
    # except:
    #     pass


def getSTT():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('듣고 있습니다.')
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language=language)
        print(f"user : {text}")
        return text
    
    except sr.UnknownValueError:
        print("인식 실패") # 음성 인식 실패        

    except sr.RequestError as e:
        print('요청 실패 : {0}'.format(e)) # 기타 다른 에러

        
def getTTS(content):
    try:
        tts = gTTS(content,lang=language)
        tts.save("voice.mp3")

        print(f"chatGPT : {content}")
        playsound("voice.mp3")
    except PermissionError as e:
        print(e)
        


while True :
    print("start : 작동시작 / stop : 작동중지")
    command = input()

    if command == "start":
        getTTS(getChatGPT(getSTT()))

    elif command == "stop":
        break