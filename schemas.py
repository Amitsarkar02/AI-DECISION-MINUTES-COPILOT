from pydantic import BaseModel
from typing import Optional, List

class Decision(BaseModel):
    text: str
    owner: Optional[str] = None
    deadline: Optional[str] = None
    confidence: float
    status: Optional[str] = None

class ActionItem(BaseModel):
    text: str
    owner: Optional[str] = None
    deadline: Optional[str] = None
    confidence: float
    status: Optional[str] = None

class ExtractionResult(BaseModel):
    decisions: List[Decision]
    action_items: List[ActionItem]
    blockers: List[str]
