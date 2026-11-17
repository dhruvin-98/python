from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello..."

@app.route("/page2")
def name():
    return "Page 2 "


app.run()
