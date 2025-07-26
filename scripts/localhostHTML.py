from flask import Flask, render_template

import webbrowser

if __name__ == '__main__':
    from jsonmaker import api_file_path, JSONBINKEY
    from jsonbin import json_file_id
else:
    from scripts.jsonmaker import api_file_path, JSONBINKEY
    from scripts.jsonbin import json_file_id

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api-keys/JSONBIN")
def api_keys():
    return JSONBINKEY

@app.route("/api-keys/FileID")
def FileID():
    return json_file_id

def runlocalhost(host, port):
    url = (f"http://{host}:{port}/")
    webbrowser.open(url, new=2)
    app.run(host, port)
    

if __name__ == "__main__":
    runlocalhost("0.0.0.0", 5000)
    