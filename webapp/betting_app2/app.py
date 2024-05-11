from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-teams', methods=['GET'])
def get_teams():
    # Script URL to fetch team data
    script_url = 'https://script.google.com/macros/s/AKfycbxinGc4O3f3Go_U4mC84yfEgXqHUudAoCwQF9JLLrHcLC4tGahjvp6ikUrNuen5wrWGJg/exec'
    try:
        response = requests.get(script_url)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': 'Failed to fetch teams data', 'status': response.status_code})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e), 'status': 500})

@app.route('/compare', methods=['POST'])
def compare_models():
    data = request.get_json()
    home_team = data['homeTeam']
    away_team = data['awayTeam']
    rc_data = fetch_model_data(home_team, away_team, 'RC')
    bsr_data = fetch_model_data(home_team, away_team, 'BsR')
    return jsonify({'RC': rc_data, 'BsR': bsr_data})

def fetch_model_data(home_team, away_team, model):
    # Replace with your script's POST URL ensuring it can handle POST requests for data processing
    script_url = 'https://script.google.com/macros/s/AKfycbxinGc4O3f3Go_U4mC84yfEgXqHUudAoCwQF9JLLrHcLC4tGahjvp6ikUrNuen5wrWGJg/exec'
    params = {
        'homeTeam': home_team,
        'awayTeam': away_team,
        'model': model
    }
    try:
        response = requests.post(script_url, json=params)
        if response.status_code == 200:
            return response.json()  # Data formatting can be done here if necessary
        else:
            return {'error': 'Failed to fetch model data', 'status': response.status_code}
    except requests.exceptions.RequestException as e:
        return {'error': str(e), 'status': 500}

if __name__ == '__main__':
    app.run(debug=True)
