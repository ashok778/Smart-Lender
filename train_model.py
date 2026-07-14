import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset
data = pd.read_csv("loan.csv")

# Convert text to numbers
le = LabelEncoder()

data["Gender"] = le.fit_transform(data["Gender"])
data["Married"] = le.fit_transform(data["Married"])
data["Loan_Status"] = le.fit_transform(data["Loan_Status"])

# Inputs and Output
X = data.drop("Loan_Status", axis=1)
y = data["Loan_Status"]

# Train Model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save Model
joblib.dump(model, "model.pkl")

print("Model trained successfully!")