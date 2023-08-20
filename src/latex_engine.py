from PIL import Image
from pix2tex.cli import LatexOCR
import os

latex_ocr_model = LatexOCR()

import pyperclip

def recognize_latex(screenshot_file_path):
    if not screenshot_file_path:
        return ""

    # Save the current clipboard content
    original_clipboard_content = pyperclip.paste()

    if os.path.isfile(screenshot_file_path):
        screenshot = Image.open(screenshot_file_path)
        recognized_latex = latex_ocr_model(screenshot, resize=True)

        # Restore the original clipboard content
        pyperclip.copy(original_clipboard_content)

        if recognized_latex:
            return recognized_latex

    return ""
