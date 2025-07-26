from flask import Flask, render_template

import webbrowser

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def runlocalhost():
    webbrowser.open("http://127.0.0.1:5000/", new=2)
    app.run()

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000/", new=2)
    app.run()
    