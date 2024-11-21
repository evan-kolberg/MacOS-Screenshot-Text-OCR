# MacOS Screenshot OCR & LaTeX Model

Merged Pull Request Additions:
- Window is always on top -> If you focus on another application window, the OCR program window will stay on the topmost layer. Having to refocus the program window can often be annoying and waste time. 
- Canvas is smaller and slimmer -> This allows users to put the app in the corner of the screen without compromising large amounts of screen real estate. 
- Moved the on-click button messages to the window's title to keep the canvas size constant.

![Screenshot 2024-02-13 at 11 35 33 AM](https://github.com/rawcsav/MacOS-Screenshot-Text-OCR/assets/70989484/b3a7c397-d772-459c-8f5e-fbb21c813c0f)
![Screenshot 2024-02-13 at 11 34 37 AM](https://github.com/rawcsav/MacOS-Screenshot-Text-OCR/assets/70989484/5a800c6f-f189-44bd-b0f1-43db821135cf)


This Python program extracts text and LaTeX code from screenshots, which can be useful when dealing with poorly formatted PDFs or complex scientific documents. The program leverages Optical Character Recognition (OCR) technology, temporary file management, and user-friendly GUI for streamlined and efficient text and LaTeX extraction.

## Features
- **Screenshot Capture**: Capture screenshots of selected screen areas and save them as temporary files.
- **OCR Engine (Pytesseract)**: Extract text from the captured screenshots using the Pytesseract library.
- **LaTeX Engine (Modified Pix2tex from Forked LatexOCR)**: Extract LaTeX code from the captured temporary screenshots based on the LaTeX-OCR (modified pix2tex, a forked [LatexOCR model](https://github.com/rawcsav/LaTeX-OCR)).
- **Clipboard Management**: Append the recognized text or LaTeX code to the clipboard in an organized manner. Includes an easy-clear button for clearing the clipboard content.
- **User Interface**: A lightweight, easy-to-use interface built with tkinter.


## Installation

1. Clone the repository and navigate to the project folder:

```bash
git clone https://github.com/yourusername/mac_screenshot_ocr_latex.git
cd mac_screenshot_ocr_latex
```
2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Clone and integrate the modified LatexOCR model (https://github.com/rawcsav/LaTeX-OCR) for use with the `latex_engine.py` file.
  
5. Modify the `capture_tools.py`, `ocr_engine.py`, and `latex_engine.py` files to include your custom configurations, if necessary.

6. Run the `main_app.py` script to start the application:

```bash
python main_app.py
```

## Usage

1. Open the application and choose your desired recognition mode (Text OCR or LaTeX OCR).

2. Press "Enter" or click the corresponding button to capture a screenshot of the desired content.

3. The recognized text or translated LaTeX code will be appended to your clipboard.

4. Optional: Click "Clear Clipboard" to erase the clipboard content.

5. Paste the extracted content into your preferred application.

## Demos
- [Online Demo](https://rawcsav.com/projects/macocr.html)

## Limitations and Acknowledgement
Thanks to Lukas Belcher and his foundational Latex model (https://github.com/lukas-blecher/LaTeX-OCR)!

While this solution performs well in recognizing standard text, it may struggle with complex scientific symbols, mathematical notations, or technical expressions. In the future, specialized OCR models can be developed to handle such content more accurately. Additionally, improvements can be made to preprocessing and post-processing techniques to further enhance the quality and readability of extracted text.
