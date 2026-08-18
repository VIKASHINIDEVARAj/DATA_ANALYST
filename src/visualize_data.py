import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data/student_placement_data.csv")

# 1. Placement distribution
sns.countplot(data=df, x="Placement")

plt.title("Student Placement Distribution")
plt.xlabel("Placement")
plt.ylabel("Number of Students")
plt.show()


# 2. CGPA vs Placement
sns.boxplot(data=df, x="Placement", y="CGPA")

plt.title("CGPA vs Placement")
plt.xlabel("Placement")
plt.ylabel("CGPA")
plt.show()


# 3. Skills vs Placement
skill_columns = [
    "Python_Skill",
    "Java_Skill",
    "DSA_Skill"
]

skill_data = df.melt(
    id_vars="Placement",
    value_vars=skill_columns,
    var_name="Skill",
    value_name="Score"
)

sns.boxplot(
    data=skill_data,
    x="Skill",
    y="Score",
    hue="Placement"
)

plt.title("Technical Skills vs Placement")
plt.xlabel("Skill")
plt.ylabel("Skill Score")
plt.show()