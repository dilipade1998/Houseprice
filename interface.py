from flask import Flask , render_template , jsonify ,request
from project_app.utils import Price_prediction
import pickle
import json
import config

app=Flask(__name__)

@app.route("/")
def base():
    return render_template("home.html")

@app.route("/predict",methods=["POST"])

def home():
    CRIM = request.form["CRIM"]
    ZN = request.form["ZN"]
    INDUS = request.form["INDUS"]
    CHAS = request.form["CHAS"]
    NOX = request.form["NOX"]
    RM = request.form["RM"]
    AGE = request.form["AGE"]
    DIS = request.form["DIS"]
    RAD = request.form["RAD"]
    TAX = request.form["TAX"]
    PTRATIO = request.form["PTRATIO"]
    B = request.form["B"]
    LSTAT = request.form["LSTAT"]
    
    x=Price_prediction(CRIM,ZN,INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX,PTRATIO, B, LSTAT)

    result=x.predict_price()

    return render_template("next.html",data=result)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=True)