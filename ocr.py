import base64
import os
import requests
from PIL import Image

SYSTEM_PROMPT = """Act as an OCR assistant. Analyze the provided image and:
Please tell me which ingredients are in this product.
Thanks!"""

def encode_image_to_base64(image_path):
    """Convert an image file to a base64 encoded string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def perform_ocr(image_path):
    """Perform OCR on the given image using Llama 3.2-Vision."""
    base64_image = encode_image_to_base64(image_path)
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2-vision",
            "stream" : False,
            "prompt": SYSTEM_PROMPT,
            "images": [base64_image]
        }
    )
    if response.status_code == 200:
        print(response.json())
        return response.json().get("message", {}).get("content", "")
    else:
        print("Error:", response.status_code, response.text)
        return None

if __name__ == "__main__":
    image_path = os.getcwd() + "/images/dots candy package.jpg"
    result = perform_ocr(image_path)
    if result:
        print("OCR Recognition Result:")
        print(result)