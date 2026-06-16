import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Remove customerID
if "customerID" in df.columns:
    df.drop("customerID", axis=1, inplace=True)

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Remove missing values
df.dropna(inplace=True)

# Convert ALL text columns to numbers
for col in df.columns:
    if df[col].dtype == "object" or str(df[col].dtype) == "str":
        df[col] = pd.factorize(df[col])[0]
        print(df.dtypes)

# Convert all text columns to numeric
for col in df.columns:
    if df[col].dtype == "object" or str(df[col].dtype) == "string":
        df[col] = pd.factorize(df[col])[0]

print("Data Types After Encoding:")
print(df.dtypes)

# Features and Target
print(df.head())
print("\nDATA TYPES:")
print(df.dtypes)
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy:.2f}")

# Save Model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\nModel trained successfully!")
print("model.pkl created successfully!")
print("Number of features:", X.shape[1])
print("Feature names:")
print(X.columns.tolist())
