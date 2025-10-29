import os
from huggingface_hub import InferenceClient

class HuggingFaceService:
    def __init__(self):
        self.model_id = os.getenv("HUGGINGFACE_MODEL")
        self.api_token = os.getenv("HUGGINGFACE_TOKEN")
        self.client = InferenceClient(model=self.model_id, token=self.api_token)

    def predict(self, image_path):
        with open(image_path, "rb") as image_file:
            predictions = self.client.image_classification(image_file)
            # predictions: [{'label': 'Malignant', 'score': 0.871}, ...]
            scores = {pred['label']: round(pred['score'] * 100, 2) for pred in predictions}
            top = max(predictions, key=lambda x: x['score'])
            return {
                "prediction_class": top['label'],
                "confidence": round(top['score'] * 100, 2),
                "all_scores": scores
            }
