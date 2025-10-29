# Lung CT Cancer Detection API

A Flask backend that uploads lung CT scan images and predicts benign/malignant/normal using a locally stored Keras model.

## Project Structure

```
lung_cancer_project/
├── app/
│   ├── __init__.py                    # Flask app factory, blueprint registration
│   ├── config.py                      # App configuration (paths, etc.)
│   ├── api/
│   │   ├── upload.py                  # Image upload endpoint
│   │   └── predict.py                 # Prediction endpoint using the ML service
│   └── services/
│       └── local_model_service.py     # Loads the Keras model and runs predictions
├── ml_models/
│   └── lung_ct_model.keras            # The downloaded Keras model file from Hugging Face
├── requirements.txt                   # Python dependencies (Keras 3+, TensorFlow, Flask, etc.)
└── run.py                             # App entry point
```

## Installation

```bash
pip install -r requirements.txt
```

> **Note:** Uses `keras 3.x` and `tensorflow 2.15.x+`. Model file (`.keras`) should be placed in `ml_models/lung_ct_model.keras`.

## Usage

Start the backend:

```bash
python run.py
```

## API Endpoints

### 1. POST /api/upload

Uploads an image (jpg/png) to the server.

- **Request:** `multipart/form-data` with key `file`
- **Response:**

```json
{
  "success": true,
  "file_id": "unique_id_image.jpg"
}
```

### 2. POST /api/predict

Runs lung CT scan prediction using the uploaded file.

- **Request:** JSON body with key `"file_id"` (from upload step)
- **Response:**

```json
{
  "success": true,
  "prediction_class": "Malignant",
  "confidence": 95.44,
  "all_scores": {
    "Benign": 2.48,
    "Malignant": 95.44,
    "Normal": 2.08
  }
}
```

## Major Changes / Notes

- **Offline Model Prediction:** Switched frontend ML service from Hugging Face Inference API to direct Keras loading for offline inference.
- **Keras 3 Compatibility:** Migrated preprocessing to use `keras.utils.load_img` and `keras.utils.img_to_array` since `tensorflow.keras.preprocessing.image` is deprecated.
- **Backend Classes:**
  - `LocalModelService` loads the `.keras` model once at app start and provides `.predict()` endpoint logic.
- **No Cloud Dependency:** App works fully offline as long as the model file is available locally.

## Testing

- Can be tested via Postman or cURL (see "API Endpoints" section for examples).
- Validated for multiple images and all three classes (Benign, Malignant, Normal).

## Requirements

```txt
flask>=2.3.0
keras>=3.0.0
tensorflow>=2.15.0
numpy>=1.24.0
pillow>=10.0.0
```

## License

MIT License