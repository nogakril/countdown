import sys
import threading

from PyQt5.QtWidgets import QApplication
from flask import Flask, request, jsonify
from flask_cors import CORS

from MainWindow import MainWindow
from OpenAIManager import OpenAIManager

app = Flask(__name__)
openai_manager = OpenAIManager()
main_window = None
CORS(app)

json_format = {
    "First Name": "noga",
    "Last Name": "kril",
    "Age": 27,
    "City": "tel aviv",
    "Occupation": "software engineer",
    "Graduate": True,
    "Height (m)": 1.70,
    "Weight": 50,
    "Marital Status": "single",
    "Astrological Sign": "leo",
    "Question": "when will I get married?"
}


@app.route('/countdown/new', methods=['POST'])
def countdown_new():
    global main_window
    try:
        data = request.json
        question = data.get("question", "")
        time_frame, never, max = openai_manager.generate_completion_request(question, data)
        if never:
            return jsonify({"message": "The answer is never!"}), 200
        main_window.counter.set_random_counter(time_frame, max)
        if not main_window.counter_thread.isRunning():
            main_window.counter_thread.start()
        return jsonify({"message": f"Countdown set to {time_frame}!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


def run_flask():
    app.run(debug=True, use_reloader=False)

def run_pyqt():
    global main_window
    app_qt = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.dot_grid.draw_digits()
    main_window.dot_grid.draw_letters()
    sys.exit(app_qt.exec_())


if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    run_pyqt()
