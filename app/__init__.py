from flask import Flask
from app.config import Config
from app.api.upload import upload_bp
from app.api.predict import predict_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register blueprints here
    app.register_blueprint(upload_bp, url_prefix='/api')

    app.register_blueprint(predict_bp, url_prefix='/api')
    
    return app
