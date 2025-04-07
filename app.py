from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
import requests
import os
import random
from dotenv import load_dotenv
import json
from datetime import datetime
import google.generativeai as genai

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
socketio = SocketIO(app)

# Mock traffic data structure
MOCK_TRAFFIC_DATA = {
    'I-95': {'speed': 65, 'congestion': 'low', 'incidents': []},
    'I-495': {'speed': 45, 'congestion': 'medium', 'incidents': ['construction']},
    'US-1': {'speed': 35, 'congestion': 'high', 'incidents': ['accident']}
}

# Gemini API configuration
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Define the model name - using an available model from your system
MODEL_NAME = "models/gemini-1.5-pro"

try:
    # Print available models for debugging
    print("Available Models:")
    for m in genai.list_models():
        print(f"Name: {m.name}, Generation Methods: {m.supported_generation_methods}")
except Exception as e:
    print(f"Error listing models: {e}")

def get_gemini_response(prompt):
    """Get response from Gemini API"""
    try:
        # Create the model - do this for each request to ensure fresh state
        model = genai.GenerativeModel(MODEL_NAME)
        
        # Prepare the prompt with context about traffic data
        context = f"""You are a traffic monitoring assistant. Here's the current traffic data:
        {json.dumps(MOCK_TRAFFIC_DATA, indent=2)}
        
        User question: {prompt}
        
        Please provide a helpful response based on this traffic data."""
        
        # Generate the response
        response = model.generate_content(context)
        
        if hasattr(response, 'text'):
            return response.text
        else:
            return str(response)
            
    except Exception as e:
        print(f"Detailed Gemini API error: {str(e)}")  # Detailed error logging
        return f"Error getting response from Gemini API: {str(e)}"

def update_mock_traffic_data():
    """Simulate real-time traffic data updates"""
    for route in MOCK_TRAFFIC_DATA:
        MOCK_TRAFFIC_DATA[route]['speed'] = random.randint(25, 75)
        MOCK_TRAFFIC_DATA[route]['congestion'] = random.choice(['low', 'medium', 'high'])
        if random.random() < 0.1:  # 10% chance of new incident
            MOCK_TRAFFIC_DATA[route]['incidents'] = random.choice([[], ['construction'], ['accident']])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    # Process the message with Gemini API
    response = get_gemini_response(user_message)
    
    return jsonify({'response': response})

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

def background_traffic_updates():
    """Background task to send traffic updates"""
    while True:
        update_mock_traffic_data()
        socketio.emit('traffic_update', MOCK_TRAFFIC_DATA)
        socketio.sleep(5)  # Update every 5 seconds

if __name__ == '__main__':
    socketio.start_background_task(background_traffic_updates)
    socketio.run(app, debug=True) 