# backend/services/gemini_service.py

import json
from services.image_utils import save_temp_image, image_format
from config import GOOGLE_API_KEY, MODEL_CONFIG, SAFETY_SETTINGS
import google.generativeai as genai

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                              generation_config=MODEL_CONFIG,
                              safety_settings=SAFETY_SETTINGS)

def generate_json_from_image(file):
    temp_file_path = save_temp_image(file)
    image_info = image_format(temp_file_path)
    system_prompt = "You are a specialist in comprehending receipts. Input images in the form of receipts will be provided to you, and your task is to respond to questions based on the content of the input image."
    user_prompt = (
    "Convert the invoice data from the image into a JSON format with proper structure. "
    "Only output JSON, starting with { and ending with }. "
    "Include keys like 'items' (array), 'total_pre_tax', 'vat', 'total_after_tax', "
    "'store_name', 'store_address', and 'date'."
)

    try:
        input_prompt = [system_prompt, image_info, user_prompt]
        response = model.generate_content(input_prompt)
        # Check if response.text exists and is not empty
        if not response.text:
            raise ValueError("Empty response from AI model")

        json_output = json.loads(response.text)  # Attempt to parse JSON
    except json.JSONDecodeError:
        raise ValueError("Failed to parse JSON. Response was not in JSON format.")
    except Exception as e:
        raise ValueError(f"Error processing image: {str(e)}")
    finally:
        temp_file_path.unlink()  # Clean up the temporary file

    return json_output
