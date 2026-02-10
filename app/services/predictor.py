import os
import joblib
import numpy as np
import logging
from app.schemas import PredictRequest, PredictResponse

logger = logging.getLogger(__name__)

class Predictor:
    def __init__(self) -> None:
        model_path = os.getenv("MODEL_PATH", "models/model.joblib")
        self.model = joblib.load(model_path)
        logger.info("model_loaded", extra={"model_path": model_path})

    def predict(self, req: PredictRequest) -> PredictResponse:
        features = np.array([[req.minute, req.score_diff, req.stamina_index]], dtype=float)

        proba = float(self.model.predict_proba(features)[0][1])
        should_sub = proba >= 0.5

        logger.info(
            "prediction_made",
            extra={
                "match_id": req.match_id,
                "minute": req.minute,
                "score_diff": req.score_diff,
                "stamina_index": req.stamina_index,
                "probability": proba,
                "should_sub": should_sub,
            },
        )

        return PredictResponse(
            should_sub=should_sub,
            probability=proba,
            reason="logreg_model_v1"
        )
