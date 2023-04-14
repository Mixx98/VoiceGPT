from gtts import gTTS
from playsound import playsound


# TTS 서비스를 이용하여 음성을 생성합니다.
tts = gTTS("안녕하세요. 반갑습니다.",lang='ko')

# 음성을 mp3 파일로 저장합니다.
tts.save("hello.mp3")

# 생성된 파일을 재생합니다.
playsound("hello.mp3")


