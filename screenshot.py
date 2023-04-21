import os
import tempfile
from PIL import Image
from pytesseract import image_to_string
import pyperclip
import subprocess

def main():
    print("Capturing portion of the screen...")

    with tempfile.NamedTemporaryFile(prefix="screenshot_", suffix=".png", delete=False) as tmp:
        screenshot_file_path = tmp.name
        subprocess.run(["screencapture", "-i", screenshot_file_path])

    if os.path.isfile(screenshot_file_path):
        screenshot = Image.open(screenshot_file_path)

        tesseract_cmd = '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'  # Change the path according to tesseract installation path
        recognized_text = image_to_string(screenshot, lang="eng", config='--psm 6')

        os.unlink(screenshot_file_path)

        pyperclip.copy(recognized_text)
        print("Text recognized and copied to clipboard!")

if __name__ == "__main__":
    main()