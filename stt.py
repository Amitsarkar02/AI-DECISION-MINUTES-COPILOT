import openai
from dotenv import load_dotenv
import os
from openai import OpenAI


load_dotenv()

# Optional debug (remove later)
print("Loaded key:", os.getenv("OPENAI_API_KEY"))

client = OpenAI()

def transcribe(audio_path: str) -> str:
    with open(audio_path, "rb") as audio_file:
        transcript = openai.audio.transcriptions.create(
            file=audio_file,
            model="gpt-4o-transcribe"
        )
    return transcript.text

