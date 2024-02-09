from flask import Flask, render_template
import pickle
app = Flask(__name__)

rfc = pickle.load(open("rfc.pickle", "rb"))

@app.route("/")

def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)