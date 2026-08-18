import pandas as pd

# Load the student dataset
df = pd.read_csv("data/student_placement_data.csv")

# Create placement numeric value
df["Placement_Flag"] = df["Placement"].map({
    "Yes": 1,
    "No": 0
})

# Create skill average
df["Average_Technical_Skill"] = (
    df["Python_Skill"]
    + df["Java_Skill"]
    + df["DSA_Skill"]
) / 3

# Create total experience
df["Total_Experience"] = (
    df["Projects"] + df["Internships"]
)

# Create CGPA category
df["CGPA_Category"] = pd.cut(
    df["CGPA"],
    bins=[0, 6, 7, 8, 9, 10],
    labels=[
        "Below 6",
        "6 - 7",
        "7 - 8",
        "8 - 9",
        "9 - 10"
    ]
)

# Save Power BI dataset
df.to_csv(
    "dashboard/student_placement_powerbi.csv",
    index=False
)

print("Power BI dataset created successfully!")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")