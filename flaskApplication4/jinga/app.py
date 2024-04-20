from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/guess/<name>')
def guess(name):
    url=f"https://api.agify.io?name={name}"
    gender_response=requests.get(url)
    gender_data=gender_response.json()
    gender=gender_data["gender"]
    return render_template("result.html", name=name)


if __name__ == '__main__':
    app.run(debug=True)
