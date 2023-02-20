from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Marina!"


@app.route('/done')
def done():
    return '<h1>Student Name</h1>'


if __name__ == "__main__":
    app.run(port=7000, host='0.0.0.0')