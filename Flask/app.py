from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/page2")
def name():
    return "Page 2 "


app.run()
