import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print('듣고 있어요')
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language='ko')
    print(text)
except sr.UnknownValueError:
    print("인식 실패")
except sr.RequestError:
    print('요청 실패')