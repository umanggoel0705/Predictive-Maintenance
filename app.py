from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import classification_report

app = Flask(__name__)

df = pd.read_csv(r'D:\Umang\AI & ML\Predictive Maintenance\submitted1.csv')
rfc_pred = df['Predicted Failure'].values
y_true = df['Ground Truth'].values

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/result", methods = ["GET","POST"])
def result():
    if request.method == 'POST':
        air_temp = request.form.get("a_t")
        pro_temp = request.form.get("p_t")
        rot_speed = request.form.get("r_s")
        tor = request.form.get("to")
        tool_wear = request.form.get("t_w")
        Type = request.form.get("T")
        match Type:
            case 'L':
                Type_H = 0
                Type_L = 1
                Type_M = 0
            case 'M':
                Type_H = 0
                Type_L = 0
                Type_M = 1
            case 'H':
                Type_H = 1
                Type_L = 0
                Type_M = 0
        user_inp = [air_temp,pro_temp,rot_speed,tor,tool_wear,Type_H,Type_L,Type_M]
        X_user = pd.DataFrame([user_inp])
        loaded_model = pickle.load(open("rfc.pickle", "rb"))
        result = loaded_model.predict(X_user)[0]
        report = classification_report(rfc_pred, y_true)
        # return "Failure Type: " + result
    return render_template("result.html", result = result, report = report)

if __name__ == "__main__":
    app.run(debug = True)
