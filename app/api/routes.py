from fastapi import APIRouter
from app.schemas import PredictRequest, PredictResponse
from app.services.predictor import Predictor

router = APIRouter()
predictor = Predictor()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    result = predictor.predict(req)
    return result
