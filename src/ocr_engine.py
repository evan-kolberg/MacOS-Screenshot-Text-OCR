from PIL import Image
from pytesseract import image_to_string
import os

def recognize_text(screenshot_file_path, lang="eng"):
    if not screenshot_file_path:
        return ""

    if os.path.isfile(screenshot_file_path):
        screenshot = Image.open(screenshot_file_path)
        recognized_text = image_to_string(screenshot, lang=lang, config='--psm 6')
        os.unlink(screenshot_file_path)
        return recognized_text.strip()

    return ""
