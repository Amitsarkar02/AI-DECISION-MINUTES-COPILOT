from app.services.stt import transcribe
from app.services.extraction import extract_meeting_outcomes
from app.services.confidence import apply_confidence_logic

def run_extraction_pipeline(transcript: str):
    result = extract_meeting_outcomes(transcript)

    result.decisions = apply_confidence_logic(result.decisions)
    result.action_items = apply_confidence_logic(result.action_items)

    return result

def analyze_meeting (audio_path:str):
    
    transcript = transcribe(audio_path)
    
    extraction_result = extract_meeting_outcomes(transcript)
    
    extraction_result.decisions = apply_confidence_logic(
        extraction_result.decisions
    )
    
    extraction_result.action_items = apply_confidence_logic(
        extraction_result.action_items
    )
    
    return {
        "transcript": transcript,
        "decisions": extraction_result.decisions,
        "action_items": extraction_result.action_items,
        "blockers": extraction_result.blockers
    }

