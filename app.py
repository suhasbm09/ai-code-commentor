from flask import Flask, render_template, request, jsonify
import requests
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Hardcoded OpenRouter API key
load_dotenv()
api_key=os.getenv("OPENROUTER_API_KEY")

print("API KEY: ",api_key)
app = Flask(__name__)
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
                    "content": f"Comment this code clearly and meaningfully with the code and add comments in middle thats it and at last explaination of code:\n\n{code}"
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
