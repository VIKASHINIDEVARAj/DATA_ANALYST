import pandas as pd
import numpy as np

# Make the results reproducible
np.random.seed(42)

# Number of students
num_students = 1000

# Generate student data
data = {
    "Student_ID": range(1, num_students + 1),

    "Age": np.random.randint(19, 23, num_students),

    "Gender": np.random.choice(
        ["Male", "Female"],
        num_students
    ),

    "Department": np.random.choice(
        ["Computer Science", "Information Technology",
         "Data Science", "Electronics"],
        num_students
    ),

    "CGPA": np.round(
        np.random.uniform(5.5, 10.0, num_students), 2
    ),

    "Attendance": np.round(
        np.random.uniform(60, 100, num_students), 1
    ),

    "Python_Skill": np.random.randint(1, 11, num_students),

    "Java_Skill": np.random.randint(1, 11, num_students),

    "DSA_Skill": np.random.randint(1, 11, num_students),

    "Projects": np.random.randint(0, 5, num_students),

    "Internships": np.random.randint(0, 4, num_students),

    "Communication_Score": np.random.randint(
        40, 101, num_students
    ),

    "Aptitude_Score": np.random.randint(
        40, 101, num_students
    )
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate a placement score
placement_score = (
    df["CGPA"] * 10
    + df["Attendance"] * 0.2
    + df["Python_Skill"] * 2
    + df["Java_Skill"] * 1.5
    + df["DSA_Skill"] * 2
    + df["Projects"] * 3
    + df["Internships"] * 4
    + df["Communication_Score"] * 0.1
    + df["Aptitude_Score"] * 0.1
)

df["Placement"] = np.where(
    placement_score >= 145,
    "Yes",
    "No"
)

# Generate salary for placed students
df["Salary_LPA"] = np.where(
    df["Placement"] == "Yes",
    np.round(
        np.random.uniform(3.0, 12.0, num_students),
        2
    ),
    0
)

# Save dataset
df.to_csv(
    "data/student_placement_data.csv",
    index=False
)

print("Dataset created successfully!")
print(f"Number of students: {len(df)}")
print("\nFirst 5 students:")
print(df.head())