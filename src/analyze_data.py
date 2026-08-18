import pandas as pd

# Load the dataset
df = pd.read_csv("data/student_placement_data.csv")

print("=" * 50)
print("STUDENT PLACEMENT ANALYSIS")
print("=" * 50)

# 1. Basic information
print("\n1. DATASET SIZE")
print(f"Students: {df.shape[0]}")
print(f"Features: {df.shape[1]}")

# 2. Placement statistics
print("\n2. PLACEMENT COUNT")
print(df["Placement"].value_counts())

print("\n3. PLACEMENT PERCENTAGE")
placement_percentage = df["Placement"].value_counts(normalize=True) * 100
print(placement_percentage.round(2))

# 3. Average CGPA
print("\n4. AVERAGE CGPA")
print(df.groupby("Placement")["CGPA"].mean().round(2))

# 4. Average attendance
print("\n5. AVERAGE ATTENDANCE")
print(df.groupby("Placement")["Attendance"].mean().round(2))

# 5. Average skills
print("\n6. AVERAGE SKILLS")
print(
    df.groupby("Placement")[
        ["Python_Skill", "Java_Skill", "DSA_Skill"]
    ].mean().round(2)
)

# 6. Average projects and internships
print("\n7. PROJECTS AND INTERNSHIPS")
print(
    df.groupby("Placement")[
        ["Projects", "Internships"]
    ].mean().round(2)
)

# 7. Average salary
print("\n8. AVERAGE SALARY")
print(
    df[df["Placement"] == "Yes"]["Salary_LPA"].mean().round(2)
)

# 8. Department-wise placement
print("\n9. DEPARTMENT-WISE PLACEMENT")
department_placement = pd.crosstab(
    df["Department"],
    df["Placement"],
    normalize="index"
) * 100

print(department_placement.round(2))