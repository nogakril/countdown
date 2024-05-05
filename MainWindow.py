import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from Counter import Counter
from CounterThread import CounterThread
from DotGrid import DotGrid


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interactive Dot Grid")
        self.showFullScreen()
        self.setStyleSheet("background-color: black;")
        self.dot_grid = DotGrid()
        self.setCentralWidget(self.dot_grid)

        self.counter = Counter()
        self.counter.set_counter(2, 3, 15, 23, 59, 55)

        self.counter_thread = CounterThread(self.counter)
        self.counter_thread.update_signal.connect(self.dot_grid.update_digits)
        self.counter_thread.start()


    def closeEvent(self, event):
        self.counter_thread.stop()
        self.counter_thread.wait()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
