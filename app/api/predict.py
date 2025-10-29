import os
from flask import Blueprint, request, jsonify, current_app
from app.services.local_model_service import LocalModelService

predict_bp = Blueprint('predict_bp', __name__)

# Load the model once for efficiency
model_service = LocalModelService()

@predict_bp.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    file_id = data.get('file_id')
    if not file_id:
        return jsonify({'error': 'file_id missing'}), 400

    # Build the path to the uploaded image
    image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], file_id)
    if not os.path.exists(image_path):
        return jsonify({'error': 'Image file not found'}), 404

    try:
        prediction = model_service.predict(image_path)
        return jsonify({"success": True, **prediction}), 200
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500
