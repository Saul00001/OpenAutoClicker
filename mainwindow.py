from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox, QSpinBox, QLabel
from autoclicker import AutoClicker

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenAutoClicker")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.interval_type = QComboBox()
        self.interval_type.addItems(["Microsecond", "Millisecond", "Second", "Minute", "Hour"])
        layout.addWidget(self.interval_type)

        self.interval_value = QSpinBox()
        self.interval_value.setRange(1, 1000000)
        layout.addWidget(self.interval_value)

        self.toggle_button = QPushButton("Start")
        self.toggle_button.clicked.connect(self.toggle_clicker)
        layout.addWidget(self.toggle_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.autoclicker = AutoClicker()

    def toggle_clicker(self):
        if self.autoclicker.running:
            self.autoclicker.stop()
            self.toggle_button.setText("Start")
        else:
            interval = self.interval_value.value()
            multiplier = {
                "Microsecond": 0.000001,
                "Millisecond": 0.001,
                "Second": 1,
                "Minute": 60,
                "Hour": 3600
            }[self.interval_type.currentText()]
            self.autoclicker.set_interval(interval * multiplier)
            self.autoclicker.running = True
            self.autoclicker.start()
            self.toggle_button.setText("Stop")
