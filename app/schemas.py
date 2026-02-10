from pydantic import BaseModel, Field

class PredictRequest(BaseModel):
    match_id: str = Field(..., examples=["match_123"])
    minute: int = Field(..., ge=0, le=130)
    score_diff: int = Field(..., ge=-10, le=10)
    stamina_index: float = Field(..., ge=0.0, le=1.0)

class PredictResponse(BaseModel):
    should_sub: bool
    probability: float
    reason: str
