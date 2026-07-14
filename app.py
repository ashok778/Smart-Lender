from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    gender = 1 if request.form["Gender"] == "Male" else 0
    married = 1 if request.form["Married"] == "Yes" else 0
    income = int(request.form["ApplicantIncome"])
    loan = int(request.form["LoanAmount"])
    credit = int(request.form["Credit_History"])

    prediction = model.predict([[gender, married, income, loan, credit]])

    if prediction[0] == 1:
        result = "✅ Loan Approved"
    else:
        result = "❌ Loan Rejected"

    return render_template("result.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
    