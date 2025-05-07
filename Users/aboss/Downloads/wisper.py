import whisper
import os

# FFmpegのパスを直接指定
os.environ["PATH"] = os.environ["PATH"] + os.pathsep + r"C:\Users\aboss\Downloads\ffmpeg\bin"

model = whisper.load_model("small")
result = model.transcribe("MOSH- 申込者向けサイトのコンテンツ詳細.mp3", language="ja")
print(result["text"])