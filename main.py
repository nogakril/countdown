import sys
import requests
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from MainWindow import MainWindow
from OpenAIManager import OpenAIManager

# The main PyQt application class
class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()
        self.openai_manager = OpenAIManager()
        self.current_json = None  # This will store the latest JSON data
        self.setup_timer()

    def setup_timer(self):
        # Set up a QTimer to fetch new data every 2 seconds
        self.timer = QTimer()
        self.timer.timeout.connect(self.fetch_new_data)
        self.timer.start(2000)  # 2000 milliseconds = 2 seconds

    def fetch_new_data(self):
        try:
            response = requests.get('https://countdown-app-oizl.vercel.app/latest')
            if response.status_code != 200:
                print(f"Failed to fetch data: {response.status_code}")
                return
            new_json = response.json()
            if new_json != self.current_json:
                self.current_json = new_json
                self.process_new_data(new_json)
        except Exception as e:
            print(f"Failed to fetch or process data: {e}")

    def process_new_data(self, data):
        # Assuming 'question' and other needed fields are part of the data
        question = data.get("question", "")
        time_frame, never, max = self.openai_manager.generate_completion_request(question, data)
        if never:
            self.main_window.counter.set_message("The answer is never!")
        else:
            self.main_window.counter.set_random_counter(time_frame, max)
            if not self.main_window.counter_thread.isRunning():
                self.main_window.counter_thread.start()

    def run(self):
        self.main_window.show()
        self.main_window.dot_grid.update_digits(88, 88, 88, 88, 88, 88)
        self.main_window.dot_grid.draw_letters()
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    application = Application()
    application.run()
