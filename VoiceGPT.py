import os
import openai
import pyaudio
import wave
from gtts import gTTS
from playsound import playsound
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = []

def getChatGPT(userContent):
    messages.append({"role": "user", "content": f"{userContent}"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)

    assistantContent = completion.choices[0].message["content"].strip()
    messages.append({"role": "assistant", "content": f"{userContent}"})

    print(f"chatGPT : {assistantContent}")
    return assistantContent

def getSTT():
    audioFile = open("voice.mp3", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audioFile)

    textValue = transcript.text
    print(f"user : {textValue}")

    return textValue

def getAudio(): 
    # 녹음할 시간(초)
    RECORD_SECONDS = 5

    # 녹음할 파일명
    WAVE_OUTPUT_FILENAME = "voice.mp3"

    # PyAudio 인스턴스 생성
    audio = pyaudio.PyAudio()

    # 녹음 설정
    stream = audio.open(format=pyaudio.paInt16, channels=1,
                    rate=44100, input=True,
                    frames_per_buffer=1024)
   
    print("녹음 시작.")
            
    # 녹음 데이터를 저장할 리스트
    frames = []

    # 녹음 데이터 읽어오기
    for i in range(0, int(44100 / 1024 * RECORD_SECONDS)):
        data = stream.read(1024)
        frames.append(data)

    print("녹음 끝.\n")

    # 녹음 스트림 닫기
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # 녹음 파일 저장
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(1)
    waveFile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    waveFile.setframerate(44100)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
        
def getTTS(textValue):
    # TTS 서비스를 이용하여 음성을 생성합니다.
    tts = gTTS(textValue,lang='ko')

    # 음성을 mp3 파일로 저장합니다.
    tts.save("voice.mp3")

    # 생성된 파일을 재생합니다.
    playsound("voice.mp3")



while True :
    print("start : 녹음시작 / stop : 작동중지")
    command = input()

    if command == "start":
        getAudio()
        getTTS(getChatGPT(getSTT()))

    elif command == "stop":
        break