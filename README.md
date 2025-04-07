# Real-time Traffic Monitor Chatbot

A real-time traffic monitoring chatbot that uses Flask for the backend, WebSocket for real-time updates, and integrates with the Gemini API for natural language processing.

## Features

- Real-time traffic updates using WebSocket
- Natural language processing using Gemini API
- Clean and responsive chat interface
- Mock traffic data simulation
- Support for both traffic-related and general queries

## Prerequisites

- Python 3.7+
- pip (Python package manager)
- A Gemini API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd traffic-monitor-chatbot
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
traffic-monitor-chatbot/
├── app.py              # Flask application and WebSocket server
├── requirements.txt    # Python dependencies
├── static/
│   ├── styles.css     # CSS styles
│   └── script.js      # Frontend JavaScript
├── templates/
│   └── index.html     # Main HTML template
└── README.md          # This file
```

## Usage

1. The chat interface allows you to ask questions about traffic conditions
2. Real-time traffic updates are displayed in the right panel
3. You can ask both traffic-related questions (e.g., "What's the traffic like on I-95?") and general questions
4. The chatbot will process your queries using the Gemini API and provide relevant responses

## Mock Traffic Data

The application uses mock traffic data for demonstration purposes. The data includes:
- Speed information
- Congestion levels (low, medium, high)
- Traffic incidents (construction, accidents)

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 