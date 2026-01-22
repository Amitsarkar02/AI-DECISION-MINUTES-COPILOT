from dotenv import load_dotenv
from openai import OpenAI
import json
from app.schemas import ExtractionResult



load_dotenv()
client = OpenAI()

SYSTEM_PROMPT = """
You are an AI assistant that extracts structured meeting outcomes.

Extract ONLY:
1. Decisions (final agreements)
2. Action items (tasks to be done)
3. Owners (if explicitly mentioned)
4. Deadlines (if explicitly mentioned)
5. Blockers

Rules:
- If owner or deadline is unclear, set it to null
- Assign a confidence score between 0 and 1
- Be conservative: if unsure, lower confidence
- Return STRICT JSON matching this schema:

{
  "decisions": [
    {"text": "", "owner": null, "deadline": null, "confidence": 0.0}
  ],
  "action_items": [
    {"text": "", "owner": null, "deadline": null, "confidence": 0.0}
  ],
  "blockers": []
}
"""

def extract_meeting_outcomes(transcript: str)-> ExtractionResult:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": transcript}
        ]
    )

    content = response.choices[0].message.content
    data = json.loads(content)

    return ExtractionResult(**data)