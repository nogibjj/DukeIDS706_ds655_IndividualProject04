# app.py
from flask import Flask, request, render_template
import requests
import os

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {'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'}"}


def predict(text):
    response = requests.post(API_URL, headers=headers, json=text)
    try:
        return response.json()[0]["generated_text"]
    except:
        return "Sorry, there was an error. Please try again."


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    if request.method == "POST":
        text = request.form["text"]
        # Perform sentiment analysis on the provided text
        sentiment = predict(text)
        return render_template("result.html", text=text, sentiment=sentiment)


# @app.route("/predict", methods=["POST"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    # print(predict("Hello, my name is"))
