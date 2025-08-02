from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend access

genai.configure(api_key="AIzaSyAdjSuNYcCWsOhV0nqo2qyHdHJDu6NPQss")  
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=(
        "You are a coding instructor. You only answer programming-related queries. "
        "If someone asks irrelevant things like 'how are you?', reply rudely."
    )
)

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return "This endpoint is for POST requests only. Please use a tool like JavaScript or Postman."
    
    user_input = request.json.get('message')
    response = model.generate_content(user_input)
    return jsonify({'reply': response.text})

if __name__ == '__main__':
    app.run(debug=True)
