import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DATABASE_URI = os.getenv('DATABASE_URI')
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')
    HUGGINGFACE_TOKEN = os.getenv('HUGGINGFACE_TOKEN')
    HUGGINGFACE_MODEL = os.getenv('HUGGINGFACE_MODEL')
    MAX_FILE_SIZE_MB = int(os.getenv('MAX_FILE_SIZE_MB', 10))
