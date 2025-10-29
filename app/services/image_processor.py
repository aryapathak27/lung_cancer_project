from PIL import Image
import numpy as np
import os

class ImageProcessor:
    TARGET_SIZE = (256, 256)  # Model requirement
    
    def preprocess_for_api(self, image_path):
        """
        Preprocess image according to model requirements
        Input: 256x256, RGB format
        """
        # Load image
        img = Image.open(image_path)
        
        # Convert to RGB if needed
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Resize to 256x256
        img = img.resize(self.TARGET_SIZE, Image.LANCZOS)
        
        # Save processed image
        processed_path = image_path.replace('uploads/', 'processed/')
        img.save(processed_path)
        
        return processed_path
    
    def validate_image(self, image_path):
        """Verify image can be opened and processed"""
        try:
            img = Image.open(image_path)
            img.verify()
            return True
        except:
            return False
