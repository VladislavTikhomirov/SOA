from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Serve the main HTML file
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to send and receive messages
@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.json.get('message')
    
    # Simulate AI response (replace this logic with your actual AI model call)
    if user_input.lower() == "hello":
        ai_response = "Hello! How can I assist you today?"
    else:
        ai_response = f"I received your message: {user_input}"

    return jsonify({'response': ai_response})

# Endpoint to switch models (placeholder, extend logic as needed)
@app.route('/change_model', methods=['POST'])
def change_model():
    model = request.json.get('model')
    
    # Placeholder: You can add logic to switch AI models here
    return jsonify({'status': f'Switched to {model}'})

if __name__ == '__main__':
    app.run(debug=True)
