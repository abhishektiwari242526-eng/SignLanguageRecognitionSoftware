from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Serve the frontend
@app.route('/')
def serve_frontend():
    return send_from_directory('.', 'index.html')

# Simulate gesture recognition
@app.route('/recognize_gesture', methods=['POST'])
def recognize_gesture():
    data = request.get_json()
    gesture = data.get('gesture', '').upper()  # Placeholder: Replace with actual gesture recognition logic
    
    # Simulate suggestion based on gesture
    suggestion = ''
    if gesture == 'V':
        suggestion = 'Opening YouTube...'
    elif gesture == 'G':
        suggestion = 'Opening Google...'
    elif gesture == 'L':
        suggestion = 'Opening LinkedIn...'
    elif gesture == 'O':
        suggestion = 'Opening Outlook...'
    else:
        suggestion = 'Gesture not recognized. Please try again.'
    
    return jsonify({'suggestion': suggestion})

if __name__ == '__main__':
    app.run(debug=True)