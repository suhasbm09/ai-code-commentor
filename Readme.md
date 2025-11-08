# 🧠 AI Code Commentor

A full-stack web app that uses GenAI to automatically comment on code — line by line, plus a final explanation.

Built with:

- 💡 Flask (Python backend)
- 💻 HTML, CSS, JavaScript (frontend)
- 🔗 OpenRouter API (Mistral 7B & OpenChat 7B)
- 🚢 Dockerized with Jenkins CI/CD pipeline
- 🎥 Live video background with sleek dark UI

---

## 🚀 Features

- ✨ Paste any code (Python, C++, etc.)
- 🧠 AI adds comments inline + final explanation
- 🔄 Reset, 📋 Copy, ⬇️ Download the result
- 🧩 Switch between Mistral 7B and OpenChat 7B
- ✅ Fully automated DevOps pipeline (build → push → deploy)


---

## 📸 UI Preview

![preview](https://github.com/suhasbm09/ai-code-commentor/blob/master/frontend/static/image.png)  


---

## 🧰 Tech Stack

| Frontend       | Backend        | AI API         | DevOps          |
|----------------|----------------|----------------|-----------------|
| HTML, CSS, JS  | Python (Flask) | OpenRouter API |Docker + Jenkins |
| Video BG via `<video>` | REST API (CORS enabled) | Mistral 7B / OpenChat 7B |

---

## 📦Local Installation

```bash
git clone https://github.com/suhasbm09/ai-code-commentor.git
cd ai-code-commentor
```

**1️⃣ Install backend dependencies**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2️⃣ Create a .env file in backend/
```env
OPENROUTER_API_KEY=your-api-key-here
👉 Get your key here: https://openrouter.ai/
```

**▶️ Run the App**
```bash
cd backend
source venv/bin/activate
python app.py
Then open http://127.0.0.1:5000 in your browser.
```
---

**🐳 Docker Deployment**
Build Docker Image

```bash
docker build -t ai-code-commentor ./backend
```

Run Container
```bash

docker run -d -p 5000:5000 --env-file backend/.env ai-code-commentor:latest
```

**⚙️ CI/CD with Jenkins**
- Automatically builds & pushes Docker image to Docker Hub
- Triggered manually or on each commit (via GitHub webhook or Jenkins Pipeline)
- Jenkinsfile included in repo with DockerHub credentials integration

**📂 Project Structure**
```
├── backend/                # Flask backend
│   ├── app.py              # Main Flask app
│   ├── requirements.txt    # Dependencies
│   ├── Dockerfile          # Docker build steps
│   ├── .env                # API key (excluded from Git)
│   ├── templates/          # (linked from frontend)
│   └── static/             # (linked from frontend)
├── frontend/               # Frontend assets
│   ├── templates/
│   │   └── index.html      # Frontend UI
│   └── static/
│       ├── bg.mp4          # Live video background
│       └── image.png       # Preview image
├── Jenkinsfile             # CI/CD pipeline config
└── .gitignore              # Git ignore rules
```

---

**🧠 Sample Prompt Sent to Model**
““Comment this code clearly and meaningfully with inline comments. At the end, add a brief explanation.““

---

**Built by**
SUHAS B M | CSE Student

- @suhaasbm2004@gmail.com
