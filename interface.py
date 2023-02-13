from flask import Flask, jsonify, request, render_template
import config
from utilities import Diabetic

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/prediction", methods = ["Post"])
def get_prediction():
    glucose = float(request.form.get("glucose"))
    bloodpressure = float(request.form.get("bloodpressure"))
    skintickness =float(request.form.get("skintickness"))
    insulin =float(request.form.get("insulin"))
    bmi = float(request.form.get("bmi"))
    diabeticpfunction =float(request.form.get("diabeticpfunction"))
    age = float(request.form.get("age"))

    diabetes_test = Diabetic(glucose,bloodpressure,skintickness,insulin,bmi,diabeticpfunction,age)
    prediction = diabetes_test.predict_diabetes()
    # print("*************************")
    # print(prediction)
    # print("*************************")

    return render_template('after.html',result=prediction)

if __name__ == "__main__":
    app.run(debug = True, port = config.PORT_NUMBER, host = config.HOST)
