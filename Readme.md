# 🧠 AI Code Commentor

A full-stack web app that uses GenAI to automatically add meaningful comments to your code — line by line.

Built with:
- 💡 Flask (Python backend)
- 💻 HTML, CSS, JavaScript (frontend)
- 🔗 OpenRouter API (Mistral 7B & OpenChat 7B models)
- 🎥 Live video background with clean dark UI

---

## 🚀 Features

- ✨ Paste any code (Python, C++, etc.)
- 🧠 AI adds comments inline + final explanation
- 🔄 Reset, 📋 Copy, ⬇️ Download the result
- 🎥 Beautiful animated hacker-style background
- 🧩 Model selection (Mistral 7B, OpenChat 7B)
- 📜 Styled placeholder and green terminal-like output

---

## 📸 UI Preview

![preview](https://github.com/suhasbm09/ai-code-commentor/CODE_COMMENTOR.mp4)  
*(Replace with your deployed app screenshot or screen recording)*

---

## 🧰 Tech Stack

| Frontend       | Backend        | AI API         |
|----------------|----------------|----------------|
| HTML, CSS, JS  | Python (Flask) | OpenRouter API |
| Video BG via `<video>` | REST API (CORS enabled) | Mistral 7B / OpenChat 7B |

---

## 📦 Installation

```bash
git clone https://github.com/suhasbm09/ai-code-commentor.git
cd ai-code-commentor

1️⃣ Install backend dependencies
```bash
pip install flask flask-cors requests

2️⃣ Set your OpenRouter API key in app.py
```python

OPENROUTER_API_KEY = "your-api-key-here"
👉 Get your key here: https://openrouter.ai/

▶️ Run the App
```bash
python app.py
Then open http://127.0.0.1:5000 in your browser.

📂 Project Structure
```csharp
├── app.py               # Flask backend
├── templates/
│   └── index.html       # Frontend UI with video background
└── static/              # (Optional for assets)


🧠 Sample Prompt Sent to Model
“Comment this code clearly and meaningfully with the code and add comments in the middle. At the end, add a brief explanation of the code.”


**Built by**
SUHAS B M 

-feel free to contact @suhasbm2004@gmail.com
