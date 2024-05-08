from PyQt5.QtCore import QThread, pyqtSignal


class CounterThread(QThread):
    update_signal = pyqtSignal(int, int, int, int, int, int)

    def __init__(self, counter):
        super().__init__()
        self.counter = counter
        self.running = True

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            self.update_signal.emit(
                self.counter.years,
                self.counter.months,
                self.counter.days,
                self.counter.hours,
                self.counter.minutes,
                self.counter.seconds
            )
            self.counter.decrement_counter()
            self.msleep(1000)
