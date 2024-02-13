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
        self.root.attributes("-topmost", True)
        self.root.eval('tk::PlaceWindow . center')
        self.root.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure("LargeButton.TButton", font=("TkDefaultFont", 12))

        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Button(button_frame, text="Text OCR", command=self.capture_and_copy_text, style="LargeButton.TButton").pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(button_frame, text="LaTeX OCR", command=self.capture_and_copy_latex, style="LargeButton.TButton").pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(button_frame, text="Clear Clipboard", command=self.reset_clipboard, style="LargeButton.TButton").pack(side=tk.LEFT, padx=10, pady=10)

        self.status_text = tk.StringVar()
        self.status_text.trace_add("write", self.update_window_title)
        self.update_window_title()

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
                self.status_text.set("Text recognized and copied")

    def capture_and_copy_latex(self):
        screenshot_file_path = capture_screen()

        if screenshot_file_path:
            recognized_content = recognize_latex(screenshot_file_path)

            if recognized_content:
                current_clipboard = pyperclip.paste()
                self.copy_content(recognized_content, current_clipboard, is_latex=True)
                self.status_text.set("LaTeX recognized and copied")

    def reset_clipboard(self):
        pyperclip.copy('')
        self.status_text.set("Clipboard reset")

    def update_window_title(self, *args):
        self.root.title(self.status_text.get())

    def run(self):
        self.root.mainloop()

def main():
    app = GUI()
    app.run()

if __name__ == "__main__":
    main()
