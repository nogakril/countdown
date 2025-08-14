# Countdown App (Python + GUI + OpenAI)

Countdown is an interactive installation that allows participants to ask a digital "Oracle" specific "When" question about their futures. In response, the Oracle predicts the date of the event in question and initiates a countdown. The time calculation is a combination of randomness and AI analysis based on the user details provided. This project prompts us to contemplate the unpredictable nature of life and the reliability of AI algorithms.

Main components:
- A desktop countdown timer with a graphical interface and optional AI-enhanced controls, developed in Python.
- Android app
- Vercel server

---

##  Features

- GUI-based countdown display with dynamic grid visuals (`DotGrid.py`)
- Support for threaded countdown logic (`CounterThread.py`) to keep the UI responsive
- AI-powered interactions or prompts via `OpenAIManager.py` (e.g., voice commands, likely GPT-driven automation)
- Modular architecture—clear separation between logic (`Counter.py`), GUI, and AI components

---

##  Requirements

- Python 3.10+ (version may vary)
- Dependencies listed in `requirements.txt`
- Optionally: OpenAI API key (if `OpenAIManager` is used)

---

##  Getting Started

```bash
git clone https://github.com/nogakril/countdown.git
cd countdown
python3 -m venv venv
source venv/bin/activate  # or: venv\Scripts\activate (Windows)
pip install -r requirements.txt
python main.py
```

---

##  Demo
https://github.com/user-attachments/assets/7bccc46e-d9a0-4b62-a7f8-1ce04f6cacd5

---

##  Additional Photos
<img src="https://github.com/user-attachments/assets/1aeaaad6-5b32-4068-b6a8-63cfb68b6eec" alt="YG-08576" width="300"/>

