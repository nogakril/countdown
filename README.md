# Countdown App (Python + GUI + OpenAI)

A desktop countdown timer with a graphical interface and optional AI-enhanced controls, developed in Python.

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


