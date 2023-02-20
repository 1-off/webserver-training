from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Marina!"


@app.route('/done/')
def done():
    return '<h1>Student Name</h1>'

@app.route('/wiki/')
def wiki():
    return redirect('https://www.wikipedia.org/')


if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0')