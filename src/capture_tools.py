import tempfile
import subprocess

def capture_screen():
    try:
        with tempfile.NamedTemporaryFile(prefix="screenshot_", suffix=".png", delete=False) as tmp:
            screenshot_file_path = tmp.name
            subprocess.run(["screencapture", "-i", "-s", screenshot_file_path], check=True)
        return screenshot_file_path
    except subprocess.CalledProcessError as e:
        print(f"Error capturing screen: {e}")
        return None