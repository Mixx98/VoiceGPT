import os
import openai
openai.api_key = "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"
audio_file = open("output.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

text_value = transcript.text

print(text_value)