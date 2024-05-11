from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-teams', methods=['GET'])
def get_teams():
    # Replace with your script's URL to fetch team data
    script_url = 'https://script.google.com/macros/s/AKfycbwpGasFf-zL6c6RL3cmJfG2iFElCA0cnrbPy2qZDDtzeazWiGHYMGrbcAXX116Vg2b1GQ/exec'
    try:
        response = requests.get(script_url)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': 'Failed to fetch teams data'}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/submit', methods=['POST'])
def submit():
    # The data from the frontend includes the model type and team names
    data = request.get_json()
    # Replace with your script's POST URL, ensuring it can handle POST requests for data processing
    script_url = 'https://script.google.com/macros/s/AKfycbwpGasFf-zL6c6RL3cmJfG2iFElCA0cnrbPy2qZDDtzeazWiGHYMGrbcAXX116Vg2b1GQ/exec'
    try:
        response = requests.post(script_url, json=data)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': 'Failed to fetch data'}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
