import pyaudio
import wave

# 녹음할 시간(초)
RECORD_SECONDS = 5

# 녹음할 파일명
WAVE_OUTPUT_FILENAME = "output.mp3"

# PyAudio 인스턴스 생성
audio = pyaudio.PyAudio()

# 녹음 설정
stream = audio.open(format=pyaudio.paInt16, channels=1,
                rate=44100, input=True,
                frames_per_buffer=1024)
while(1):
    print("start : 녹음시작 / stop : 작동중지")
    command = input()

    if command == "start":
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
    elif command == "stop":
        break
