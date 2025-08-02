from flask import Flask, render_template

import webbrowser

if __name__ == '__main__':
    from HTMLRequestsHandler import key, FileId
else :
    from scripts.HTMLRequestsHandler import key, FileId

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api-keys/JSONBIN")
def api_keys():
    return key

@app.route("/api-keys/FileID")
def FileID():
    return FileId

def runlocalhost(host, port):
    url = (f"http://{host}:{port}/")
    webbrowser.open(url, new=2)
    app.run(host, port)

def jsonbin_io():
    webbrowser.open('https://jsonbin.io/')
    

if __name__ == "__main__":
    runlocalhost("0.0.0.0", 5000)
    