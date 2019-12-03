from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():

    html = "<h1>heading1</h1>\n<h2>heading2</h2>\n<h3>heading3</h3>"

    return html

@app.route("/hello")
@app.route("/hello2")
def hello():
    return "Hello"
