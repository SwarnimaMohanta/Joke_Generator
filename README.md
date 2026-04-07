# 😂 JokeBot — AI Joke Generator

> A full-stack joke generator powered by **Claude AI** and **100,000+ Reddit jokes**. Generate funny, family-friendly jokes by topic with a beautiful dark UI.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![Claude AI](https://img.shields.io/badge/Claude-AI-FF6B35?style=for-the-badge&logo=anthropic&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 AI-Generated Jokes | Fresh jokes created by Claude AI every time |
| 📰 Reddit Classics | 100,000+ real jokes filtered and cleaned |
| 🔀 Mixed Mode | Best of both AI and Reddit combined |
| 🎯 Topic Filters | Animals, Food, Tech, School, Office, Sports, Weather |
| 👇 Reveal Punchline | Tap to dramatically reveal the punchline |
| ❤️ Like System | Save your favourite jokes in a session |
| 🌙 Dark UI | Animated gradient cards and glowing blobs |

---

## 🗂️ Project Structure

```
joke-generator/
├── backend/
│   ├── app.py                  # Flask REST API
│   ├── joke_engine.py          # Joke logic (dataset + AI)
│   ├── preprocess.py           # One-time data cleaning script
│   ├── .env                    # Your API key (never commit!)
│   ├── data/
│   │   ├── reddit_jokes.json   # Raw Kaggle dataset (download separately)
│   │   └── jokes_cleaned.json  # Auto-generated after preprocessing
│   └── requirements.txt
│
├── frontend/
│   ├── index.html              # Main UI
│   ├── style.css               # Styling
│   └── script.js               # Frontend logic
│
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- An Anthropic API key → [console.anthropic.com](https://console.anthropic.com)
- Reddit jokes dataset → [Kaggle Dataset](https://www.kaggle.com/datasets/averkij/reddit-jokes-dataset)

---

### Step 1 — Clone the Repository

```bash
git clone https://github.com/SwarnimaMohanta/Joke_Generator.git
cd Joke_Generator
```

### Step 2 — Create a Virtual Environment

```bash
# Create
python -m venv jokevenv

# Activate (Windows)
jokevenv\Scripts\activate

# Activate (Mac / Linux)
source jokevenv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r backend/requirements.txt
```

### Step 4 — Download the Dataset

Download the dataset from Kaggle and place it here:

```
backend/data/reddit_jokes.json
```

👉 [Download from Kaggle](https://www.kaggle.com/datasets/averkij/reddit-jokes-dataset)

### Step 5 — Clean the Dataset *(Run Once)*

```bash
python backend/preprocess.py
```

This automatically filters out adult, offensive, and low-quality jokes.

### Step 6 — Set Up Your API Key

Create a file at `backend/.env`:

```env
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxx
```

> ⚠️ **Never commit this file.** It is already in `.gitignore`.

### Step 7 — Start the Server

```bash
python backend/app.py
```

You should see:
```
* Running on http://127.0.0.1:5000
```

### Step 8 — Open the App 🎉

Double-click `frontend/index.html` in File Explorer to open it in your browser.

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/jokes` | Get jokes |
| `GET` | `/api/topics` | Get available topics |
| `GET` | `/api/health` | Check server status |

### Query Parameters for `/api/jokes`

| Parameter | Options | Default |
|-----------|---------|---------|
| `topic` | `animals` `food` `technology` `school` `office` `sports` `weather` `random` | `random` |
| `mode` | `mixed` `ai` `reddit` | `mixed` |
| `count` | `1` to `6` | `3` |

**Example Request:**
```
GET http://localhost:5000/api/jokes?topic=animals&mode=ai&count=3
```

**Example Response:**
```json
{
  "success": true,
  "count": 3,
  "jokes": [
    {
      "setup": "Why did the cat sit on the computer?",
      "punchline": "To keep an eye on the mouse!",
      "source": "ai",
      "topic": "animals"
    }
  ]
}
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | HTML, CSS, Vanilla JavaScript |
| Backend | Python, Flask, Flask-CORS |
| AI | Anthropic Claude API (claude-sonnet) |
| Dataset | Reddit Jokes — Kaggle (100,000+ jokes) |
| Environment | python-dotenv |

---

## ⚙️ Requirements

```
flask
flask-cors
anthropic
python-dotenv
```

---

## 🔒 Environment Variables

| Variable | Description |
|----------|-------------|
| `ANTHROPIC_API_KEY` | Your key from [console.anthropic.com](https://console.anthropic.com) |

---

## 📌 Important Notes

- `backend/data/` is excluded from Git — dataset files are too large for GitHub
- `jokevenv/` is excluded from Git — never commit virtual environments
- `.env` is excluded from Git — contains your secret API key
- You **never** need to run `joke_engine.py` directly — it loads automatically with `app.py`
- Run `preprocess.py` again anytime to re-clean the dataset

---

## 👩‍💻 Author

**Swarnima Mohanta**
- GitHub: [@SwarnimaMohanta](https://github.com/SwarnimaMohanta)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">
  Built with ❤️ using Claude AI
</div>
