from flask import Flask, render_template, jsonify
import random
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

def predict_usage():
    X = np.array([[1],[2],[3],[4],[5],[6],[7]])
    y = np.array([80, 60, 90, 40, 30, 20, 10])
    model = LinearRegression()
    model.fit(X, y)
    future = model.predict([[8]])
    return max(0, int(future[0]))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/stats')
def stats():
    predicted = predict_usage()
    current = random.randint(20, 80)
    saving = 100 - predicted if predicted < 50 else 10
    return jsonify({
        "current_cpu": current,
        "predicted_cpu": predicted,
        "cost_saved": f"{saving}%",
        "action": "Scale DOWN" if predicted < 30 else "Scale UP",
        "co2_saved": f"{saving * 0.5} kg"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)