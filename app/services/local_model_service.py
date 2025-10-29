import os
import numpy as np

os.environ["KERAS_BACKEND"] = "tensorflow"

import keras

class LocalModelService:
    def __init__(self):
        model_path = os.path.join(os.path.dirname(__file__), '../../ml_models/lung_ct_model.keras')
        self.model = keras.saving.load_model(model_path)
        self.class_labels = ['Benign', 'Malignant', 'Normal']

    def preprocess_image(self, image_path):
        img = keras.utils.load_img(image_path, target_size=(256, 256), color_mode='rgb')
        x = keras.utils.img_to_array(img) / 255.0
        x = np.expand_dims(x, axis=0)
        return x

    def predict(self, image_path):
        img_array = self.preprocess_image(image_path)
        preds = self.model.predict(img_array)[0]
        max_idx = np.argmax(preds)
        top_label = self.class_labels[max_idx]
        confidence = round(float(preds[max_idx]) * 100, 2)
        scores = {label: round(float(score) * 100, 2) for label, score in zip(self.class_labels, preds)}
        return {
            "prediction_class": top_label,
            "confidence": confidence,
            "all_scores": scores
        }
