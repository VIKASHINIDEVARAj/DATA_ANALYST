import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# ---------------------------------------
# 1. Load dataset
# ---------------------------------------

df = pd.read_csv("data/student_placement_data.csv")


# ---------------------------------------
# 2. Convert categorical data
# ---------------------------------------

# Convert Gender into numbers
gender_encoder = LabelEncoder()
df["Gender"] = gender_encoder.fit_transform(df["Gender"])

# Convert Department into numbers
department_encoder = LabelEncoder()
df["Department"] = department_encoder.fit_transform(df["Department"])

# Convert Placement into numbers
placement_encoder = LabelEncoder()
df["Placement"] = placement_encoder.fit_transform(df["Placement"])


# ---------------------------------------
# 3. Select features
# ---------------------------------------

features = [
    "Age",
    "Gender",
    "Department",
    "CGPA",
    "Attendance",
    "Python_Skill",
    "Java_Skill",
    "DSA_Skill",
    "Projects",
    "Internships",
    "Communication_Score",
    "Aptitude_Score"
]

X = df[features]
y = df["Placement"]


# ---------------------------------------
# 4. Split the data
# ---------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ---------------------------------------
# 5. Create the model
# ---------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# ---------------------------------------
# 6. Train the model
# ---------------------------------------

model.fit(X_train, y_train)


# ---------------------------------------
# 7. Make predictions
# ---------------------------------------

y_pred = model.predict(X_test)


# ---------------------------------------
# 8. Evaluate the model
# ---------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("=" * 50)
print("STUDENT PLACEMENT PREDICTION MODEL")
print("=" * 50)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=placement_encoder.classes_
    )
)
# ---------------------------------------
# 9. Feature Importance
# ---------------------------------------

importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance:")
print(importance.to_string(index=False))
# ---------------------------------------
# 10. Save ML Predictions
# ---------------------------------------

# Predictions for test data
y_pred = model.predict(X_test)

# Prediction probabilities
probabilities = model.predict_proba(X_test)

# Find probability of class 1 = Placed
yes_index = list(model.classes_).index(1)
placement_probability = probabilities[:, yes_index]

# Convert 0/1 back to Yes/No
actual_placement = y_test.map({0: "No", 1: "Yes"})
predicted_placement = pd.Series(y_pred, index=y_test.index).map({
    0: "No",
    1: "Yes"
})

# Create prediction results
prediction_results = pd.DataFrame({
    "Student_ID": df.loc[X_test.index, "Student_ID"],
    "Actual_Placement": actual_placement.values,
    "Predicted_Placement": predicted_placement.values,
    "Placement_Probability": placement_probability
})

# Prediction correctness
prediction_results["Prediction_Correct"] = (
    prediction_results["Actual_Placement"]
    == prediction_results["Predicted_Placement"]
)

# Convert probability to percentage
prediction_results["Placement_Probability"] = (
    prediction_results["Placement_Probability"] * 100
).round(2)

# Save results
prediction_results.to_csv(
    "dashboard/ml_predictions.csv",
    index=False
)

print("\nML predictions saved successfully!")
print("Prediction records:", len(prediction_results))
print("File: dashboard/ml_predictions.csv")

print("\nFirst 5 predictions:")
print(prediction_results.head())

# Student information
#         ↓
#       Python
#         ↓
#    Random Forest
#         ↓
#    Prediction
#         ↓
#    YES / NO