# app.py
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the model
model = pipeline('text-generation', model='gpt2')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the text from the POST request
    text = request.json['text']

    # Use the model to generate text
    result = model(text)

    # Return the model's prediction
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
"""
acr: acrds655
resource group: myResourceGroup
"""