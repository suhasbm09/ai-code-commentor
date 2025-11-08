from flask import Flask, render_template, request, jsonify
import requests
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Hardcoded OpenRouter API key
load_dotenv()
api_key=os.getenv("OPENROUTER_API_KEY")

print("API KEY: ",api_key)
app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/comment", methods=["POST"])
def comment():
    data = request.json
    code = data.get("code", "")
    model = data.get("model", "mistralai/mistral-7b-instruct")

    if not code.strip():
        return jsonify({"error": "No code provided"}), 400

    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://127.0.0.1:5000/",
            "X-Title": "AI Code Commenter",
        }

        payload = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": f"Please add clear and precise inline comments to the following code. Ensure comments are meaningful and concise, not verbose. Format the output as a code block with the commented code, followed by a brief explanation section.\n\nCode:\n{code}"
                }
            ],
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)
        print("Status Code:", response.status_code)
        print("Response:", response.text)

        response.raise_for_status()
        commented_code = response.json()["choices"][0]["message"]["content"]

        return jsonify({"commented_code": commented_code})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
