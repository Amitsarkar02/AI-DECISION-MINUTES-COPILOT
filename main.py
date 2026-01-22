from fastapi import FastAPI, UploadFile, File
import uuid
import shutil
import os
import tempfile
from typing import List
from app.schemas import ActionItem
from app.services.planner import create_task


from app.pipeline import analyze_meeting

app = FastAPI(title="Decision Minutes Copilot")

# Health check
@app.get("/")
def root():
    return {"status": "running"}

# 🔥 END-TO-END PIPELINE
@app.post("/analyze-meeting")
async def analyze_meeting_api(file: UploadFile = File(...)):
    # Cross-platform temp directory (Windows/Linux/macOS)
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(
        temp_dir,
        f"{uuid.uuid4()}_{file.filename}"
    )

    # Save uploaded audio
    with open(temp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Run full pipeline: STT → Extraction → Confidence
    result = analyze_meeting(temp_path)

    # Cleanup temp file
    try:
        os.remove(temp_path)
    except Exception:
        pass

    return result


@app.post("/confirm-actions")
def confirm_actions(actions :List[ActionItem]):
    """
    Human-in-the-loop confirmation.
    Only auto_approved actions are sent to planner.
    """
    created_tasks = []
    
    for action in actions:
        if action.status == "auto_approved":
            create_task(action)
            created_tasks.append(action)
    return {
        "tasks_created": created_tasks,
        "count": len(created_tasks),
        "message": "Approved actions sent to planner"
    }
                   
    