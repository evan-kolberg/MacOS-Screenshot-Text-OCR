# Screen Text Recognizer

This Python script captures a portion of the screen and uses [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) to recognize and extract the text from the captured image. The recognized text will be copied to the clipboard.


## Setup

1. Install the required libraries using pip:

```sh
pip install -r requirements.txt
```

2. Install Tesseract OCR following the instructions from its [official website](https://github.com/tesseract-ocr/tesseract).

3. Update the `tesseract_cmd` variable in the script with the correct path to your Tesseract executable.

## Usage

Run the script using the following command:

```sh
python screenshot.py
```

After running the script, you will be prompted to capture a portion of the screen. The recognized text will be copied to the clipboard.
