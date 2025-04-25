from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BACKEND_URL = "http://backend-service:5000"

@app.route('/')
def index():
    results = requests.get(f"{BACKEND_URL}/results").json()
    return render_template("index.html", results=results)

@app.route('/vote', methods=['POST'])
def vote():
    animal = request.form['animal']
    requests.post(f"{BACKEND_URL}/vote", json={"animal": animal})
    return index()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

