from app.config import CONFIDENCE_THRESHOLD

def apply_confidence_logic(items):
    """ 
    Marks items as auto_approved or needs_review
    
    """
    
    for item in items:
        if item.confidence < CONFIDENCE_THRESHOLD:
            item.status= "Needs review"
        
        else:
            item.status = "auto_approved"
    return items

