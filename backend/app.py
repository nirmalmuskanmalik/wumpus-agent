from flask import Flask, jsonify, request
from flask_cors import CORS
from agent import WumpusAgent

app = Flask(__name__)
CORS(app)

agent = None

@app.route('/')
def home():
    return "Wumpus Backend Running"

@app.route('/init', methods=['POST'])
def init():
    global agent
    data = request.json

    rows = int(data['rows'])
    cols = int(data['cols'])

    agent = WumpusAgent(rows, cols)

    return jsonify(agent.get_state())

@app.route('/step', methods=['GET'])
def step():
    global agent

    if agent is None:
        return jsonify({"error": "Agent not initialized"})

    agent.move()
    return jsonify(agent.get_state())

if __name__ == '__main__':
    app.run(debug=True)