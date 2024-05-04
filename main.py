from flask import Flask, request, send_file
from flask_cors import CORS

app = Flask(__name__)
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
def start_new_countdown():
    data = request.json
    question = data.get('question')
    if not question:
        return {"error": "No question provided."}, 400
    return "Request received", 200


if __name__ == '__main__':
    app.run(debug=True)