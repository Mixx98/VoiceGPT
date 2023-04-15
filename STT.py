import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
audio_file = open("output.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

text_value = transcript.text

print(text_value)