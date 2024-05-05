import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from DotGrid import DotGrid


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interactive Dot Grid")
        self.showFullScreen()
        self.setStyleSheet("background-color: black;")
        self.dot_grid = DotGrid()
        self.setCentralWidget(self.dot_grid)
