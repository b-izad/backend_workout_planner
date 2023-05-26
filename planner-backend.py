from flask import Flask, request, jsonify
import os
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Get the OpenAI key from environment variable
openai.api_key = os.getenv('OPENAI_KEY')

@app.route('/getWorkoutPlan', methods=['POST'])
def get_workout_plan():
    data = request.get_json()
    
    try:
        response = openai.Completion.create(
          model="text-davinci-003",
          prompt=data['prompt'],
          max_tokens=500,
          temperature=0.5
        )
        return jsonify(response['choices'][0]['text'].strip())
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(port=5000)
