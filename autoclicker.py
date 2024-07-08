import pyautogui
import time
from PyQt6.QtCore import QThread, pyqtSignal

class AutoClicker(QThread):
    def __init__(self):
        super().__init__()
        self.running = False
        self.interval = 1.0

    def run(self):
        while self.running:
            pyautogui.click()
            time.sleep(self.interval)

    def stop(self):
        self.running = False

    def set_interval(self, interval):
        self.interval = interval