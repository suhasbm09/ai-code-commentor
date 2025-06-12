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

![preview](https://github.com/suhasbm09/ai-code-commentor/blob/master/static/image.png)  


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
pip install flask flask-cors requests python-dotenv
```

2️⃣ Create a .env file
```env
OPENROUTER_API_KEY=your-api-key-here
👉 Get your key here: https://openrouter.ai/
```

**▶️ Run the App**
```bash
python app.py
Then open http://127.0.0.1:5000 in your browser.
```
---

**🐳 Docker Deployment**
Build Docker Image

```bash
docker build -t ai-code-commentor .
```

Run Container
```bash

docker run -d -p 5000:5000 --env-file .env ai-code-commentor:latest
```

**⚙️ CI/CD with Jenkins**
- Automatically builds & pushes Docker image to Docker Hub
- Triggered manually or on each commit (via GitHub webhook or Jenkins Pipeline)
- Jenkinsfile included in repo with DockerHub credentials integration

**📂 Project Structure**
```csharp
├── app.py                 # Flask backend
├── requirements.txt       # Dependencies
├── Dockerfile             # Docker build steps
├── Jenkinsfile            # CI/CD pipeline config
├── .env                   # API key (excluded from Git)
├── templates/
│   └── index.html         # Frontend UI
└── static/
    └── bg.mp4 
    └──image.png            # Live video background
```

---

**🧠 Sample Prompt Sent to Model**
““Comment this code clearly and meaningfully with inline comments. At the end, add a brief explanation.““

---

**Built by**
SUHAS B M | CSE Student

- @suhaasbm2004@gmail.com
