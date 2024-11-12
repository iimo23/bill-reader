# backend/services/image_utils.py
from pathlib import Path
import mimetypes

def save_temp_image(file):
    temp_path = Path(f"temp_{file.filename}")
    file.save(temp_path)
    return temp_path

def image_format(image_path):
    img = Path(image_path)
    if not img.exists():
        raise FileNotFoundError(f"Could not find image: {img}")
    mime_type, _ = mimetypes.guess_type(img)
    if mime_type not in ["image/jpeg", "image/png", "image/webp"]:
        raise ValueError(f"Unsupported image format: {mime_type}")
    return {"mime_type": mime_type, "data": img.read_bytes()}
