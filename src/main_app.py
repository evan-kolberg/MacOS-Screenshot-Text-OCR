import tkinter as tk
from tkinter import ttk
import pyperclip

from ocr_engine import recognize_text
from latex_engine import recognize_latex
from capture_tools import capture_screen

class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Screen Capture OCR")
        self.root.geometry("450x250")

        main_frame = ttk.Frame(self.root)
        main_frame.pack(pady=10)

        ttk.Label(main_frame, text="Choose recognition mode:").grid(row=0, column=0, sticky="W", padx=(20, 0), columnspan=2)

        ttk.Button(main_frame, text="Text OCR", command=self.capture_and_copy_text).grid(row=1, column=0, padx=(20, 0), pady=5)
        ttk.Button(main_frame, text="LaTeX OCR", command=self.capture_and_copy_latex).grid(row=1, column=1, padx=(10, 0), pady=5)


        ttk.Button(main_frame, text="Clear Clipboard", command=self.reset_clipboard).grid(row=3, column=0, padx=(20, 0), pady=5, columnspan=2)

        self.status_text = tk.StringVar()
        ttk.Label(main_frame, textvariable=self.status_text).grid(row=4, column=0, sticky="W", padx=(20, 0), pady=5, columnspan=2)

        self.root.bind("<Return>", lambda event: self.capture_and_copy_text())


    def copy_content(self, content, current_clipboard, is_latex=False):
        if is_latex:
            content = f"$$\n{content}\n$$"

        if current_clipboard:
            new_clipboard = current_clipboard + "\n\n" + content
        else:
            new_clipboard = content

        pyperclip.copy(new_clipboard)

    def capture_and_copy_text(self):
        screenshot_file_path = capture_screen()

        if screenshot_file_path:
            recognized_content = recognize_text(screenshot_file_path)

            if recognized_content:
                current_clipboard = pyperclip.paste()
                self.copy_content(recognized_content, current_clipboard, is_latex=False)
                self.status_text.set("Text recognized and appended to clipboard!")

    def capture_and_copy_latex(self):
        screenshot_file_path = capture_screen()

        if screenshot_file_path:
            recognized_content = recognize_latex(screenshot_file_path)

            if recognized_content:
                current_clipboard = pyperclip.paste()
                self.copy_content(recognized_content, current_clipboard, is_latex=True)
                self.status_text.set("LaTeX recognized and appended to clipboard!")

    def reset_clipboard(self):
        pyperclip.copy('')
        self.status_text.set("Clipboard has been reset.")

    def run(self):
        self.root.mainloop()

def main():
    app = GUI()
    app.run()

if __name__ == "__main__":
    main()