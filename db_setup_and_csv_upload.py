# ============================================================ 
#  MYSQL TABLE CREATION + CSV UPLOAD SCRIPT 
# ============================================================

import mysql.connector
import os
import pandas as pd
from dotenv import load_dotenv

# ---------------- Load environment variables ----------------
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_NAME = os.getenv("DB_NAME")

# ---------------- Create connection ----------------
conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    port=DB_PORT
)
cursor = conn.cursor()

# ---------------- Create and use database ----------------
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
cursor.execute(f"USE {DB_NAME}")

# ---------------- TABLE CREATION ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS students_table (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    email VARCHAR(100),
    phone_number BIGINT,
    enrollment_year YEAR,
    course_batch VARCHAR(20),
    city VARCHAR(50),
    graduation_year YEAR
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS programming_table (
    programming_id INT PRIMARY KEY,
    student_id INT,
    language VARCHAR(30),
    problems_solved INT,
    assessments_completed INT,
    mini_projects INT,
    certifications_earned INT,
    latest_project_score INT,
    FOREIGN KEY (student_id) REFERENCES students_table(student_id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS soft_skills_table (
    soft_skills_id INT PRIMARY KEY,
    student_id INT,
    communication_skills INT,
    teamwork_skills INT,
    presentation_skills INT,
    leadership_skills INT,
    critical_thinking INT,
    interpersonal_skills INT,
    FOREIGN KEY (student_id) REFERENCES students_table(student_id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS placement_table (
    placement_id INT PRIMARY KEY,
    student_id INT,
    mock_interviews_score INT,
    internships_completed INT,
    placement_status VARCHAR(20),
    company_name VARCHAR(100),
    placement_package INT,
    interview_rounds_cleared INT,
    placement_date DATE,
    FOREIGN KEY (student_id) REFERENCES students_table(student_id)
);
""")

conn.commit()

# ============================================================
# CSV UPLOAD SECTION
# ============================================================

def load_csv_to_table(csv_file, table_name, columns):
    df = pd.read_csv(csv_file)
    placeholders = ",".join(["%s"] * len(columns))
    column_names = ",".join(columns)

    query = f"""
        INSERT INTO {table_name} ({column_names})
        VALUES ({placeholders})
    """

    cursor.executemany(query, df[columns].values.tolist())
    conn.commit()
    print(f"✅ Data loaded into {table_name}")

# ---- Load students FIRST (foreign key dependency) ----
load_csv_to_table(
    "students_data.csv",
    "students_table",
    [
        "student_id", "name", "age", "gender", "email",
        "phone_number", "enrollment_year",
        "course_batch", "city", "graduation_year"
    ]
)

# ---- Load dependent tables ----
load_csv_to_table(
    "programming_data.csv",
    "programming_table",
    [
        "programming_id", "student_id", "language",
        "problems_solved", "assessments_completed",
        "mini_projects", "certifications_earned",
        "latest_project_score"
    ]
)

load_csv_to_table(
    "soft_skills_data.csv",
    "soft_skills_table",
    [
        "soft_skills_id", "student_id",
        "communication_skills", "teamwork_skills",
        "presentation_skills", "leadership_skills",
        "critical_thinking", "interpersonal_skills"
    ]
)

load_csv_to_table(
    "placement_data.csv",
    "placement_table",
    [
        "placement_id", "student_id",
        "mock_interviews_score", "internships_completed",
        "placement_status", "company_name",
        "placement_package", "interview_rounds_cleared",
        "placement_date"
    ]
)

# ---------------- Close connection ----------------
cursor.close()
conn.close()

print("🎉 All CSV files uploaded successfully!")
