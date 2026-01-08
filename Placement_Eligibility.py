# ============================================================
# STUDENT PLACEMENT ELIGIBILITY & INSIGHTS APPLICATION
# ============================================================

# from faker import Faker
# import random
# import pandas as pd
#
# fake = Faker()
#
# # ------------------ STUDENTS TABLE ------------------ #
# students_table = []
# for _ in range(100):
#     student = {
#         "student_id": fake.unique.random_int(min=1000, max=9999),
#         "name": fake.name(),
#         "age": fake.random_int(min=18, max=25),
#         "gender": fake.random_element(elements=("Male", "Female")),
#         "email": fake.email(),
#         "phone_number": fake.random_number(digits=10, fix_len=True),
#         "enrollment_year": fake.year(),
#         "course_batch": fake.random_element(elements=("B.Tech", "M.Tech", "MBA", "BBA")),
#         "city": fake.city(),
#         "graduation_year": fake.year(),
#     }
#     students_table.append(student)
#
# df_students = pd.DataFrame(students_table)
# df_students.to_csv("students_data.csv", index=False)
#
# # ------------------ PROGRAMMING TABLE ------------------ #
# programming_table = []
# for _ in range(100):
#     programming = {
#         "programming_id": fake.unique.random_int(min=1000, max=9999),
#         "student_id": random.choice(df_students['student_id']),
#         "language": fake.random_element(elements=("Python", "Java", "C++", "JavaScript", "SQL")),
#         "problems_solved": fake.random_int(min=0, max=100),
#         "assessments_completed": fake.random_int(min=0, max=50),
#         "mini_projects": fake.random_int(min=0, max=10),
#         "certifications_earned": fake.random_int(min=0, max=5),
#         "latest_project_score": fake.random_int(min=0, max=10),
#     }
#     programming_table.append(programming)
#
# pd.DataFrame(programming_table).to_csv("programming_data.csv", index=False)
#
# # ------------------ SOFT SKILLS TABLE ------------------ #
# soft_skills_table = []
# for _ in range(100):
#     soft_skills = {
#         "soft_skills_id": fake.unique.random_int(min=1000, max=9999),
#         "student_id": random.choice(df_students['student_id']),
#         "communication_skills": fake.random_int(min=1, max=10),
#         "teamwork_skills": fake.random_int(min=1, max=10),
#         "presentation_skills": fake.random_int(min=1, max=10),
#         "leadership_skills": fake.random_int(min=1, max=10),
#         "critical_thinking": fake.random_int(min=1, max=10),
#         "interpersonal_skills": fake.random_int(min=1, max=10),
#     }
#     soft_skills_table.append(soft_skills)
#
# pd.DataFrame(soft_skills_table).to_csv("soft_skills_data.csv", index=False)
#
# # ------------------ PLACEMENT TABLE ------------------ #
# placement_table = []
# for _ in range(100):
#     placement = {
#         "placement_id": fake.unique.random_int(min=1000, max=9999),
#         "student_id": random.choice(df_students['student_id']),
#         "mock_interviews_score": fake.random_int(min=0, max=10),
#         "internships_completed": fake.random_int(min=0, max=5),
#         "placement_status": fake.random_element(elements=("Placed", "Not Placed")),
#         "company_name": fake.company(),
#         "placement_package": fake.random_int(min=3, max=30) * 10000,
#         "interview_rounds_cleared": fake.random_int(min=1, max=5),
#         "placement_date": fake.date_between(start_date='-1y', end_date='today'),
#     }
#     placement_table.append(placement)
#
# pd.DataFrame(placement_table).to_csv("placement_data.csv", index=False)


# ============================================================
# MYSQL TABLE CREATION SCRIPT 
# ============================================================

# import mysql.connector
# import os
#
# conn = mysql.connector.connect(
#     host=os.getenv("DB_HOST"),
#     user=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASSWORD"),
#     port=int(os.getenv("DB_PORT", 3306))
# )
#
# cursor = conn.cursor()
#
# cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
# cursor.execute("USE student_db")
#
# cursor.execute("""
# CREATE TABLE students_table (
#     student_id INT PRIMARY KEY,
#     name VARCHAR(100),
#     age INT,
#     gender VARCHAR(10),
#     email VARCHAR(100),
#     phone_number BIGINT,
#     enrollment_year YEAR,
#     course_batch VARCHAR(20),
#     city VARCHAR(50),
#     graduation_year YEAR
# );
# """)
#
# cursor.execute("""
# CREATE TABLE programming_table (
#     programming_id INT PRIMARY KEY,
#     student_id INT,
#     language VARCHAR(30),
#     problems_solved INT,
#     assessments_completed INT,
#     mini_projects INT,
#     certifications_earned INT,
#     latest_project_score INT,
#     FOREIGN KEY (student_id) REFERENCES students_table(student_id)
# );
# """)
#
# cursor.execute("""
# CREATE TABLE soft_skills_table (
#     soft_skills_id INT PRIMARY KEY,
#     student_id INT,
#     communication_skills INT,
#     teamwork_skills INT,
#     presentation_skills INT,
#     leadership_skills INT,
#     critical_thinking INT,
#     interpersonal_skills INT,
#     FOREIGN KEY (student_id) REFERENCES students_table(student_id)
# );
# """)
#
# cursor.execute("""
# CREATE TABLE placement_table (
#     placement_id INT PRIMARY KEY,
#     student_id INT,
#     mock_interviews_score INT,
#     internships_completed INT,
#     placement_status VARCHAR(20),
#     company_name VARCHAR(100),
#     placement_package INT,
#     interview_rounds_cleared INT,
#     placement_date DATE,
#     FOREIGN KEY (student_id) REFERENCES students_table(student_id)
# );
# """)
#
# conn.commit()
# conn.close()


# ============================================================
# APPLICATION CODE STARTS HERE
# ============================================================

import os
import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt


# ============================================================
# DATABASE HANDLER (OOP)
# ============================================================

class DatabaseHandler:
    """Handles MySQL connection and query execution"""

    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")
        self.port = int(os.getenv("DB_PORT", 3306))
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        return pd.DataFrame(rows, columns=columns)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

selected_page = st.sidebar.radio(
    "Navigation",
    ["Introduction", "Students Insights", "Eligibility Calculation", "Creator Info"]
)


# ============================================================
# INTRODUCTION PAGE
# ============================================================

if selected_page == "Introduction":
    st.title("🎓 Student Placement Eligibility Application")
    st.markdown("""
    Welcome to the **Student Placement Prediction Application**!  
This tool helps students understand their eligibility for **campus placements** based on academic and skill-based parameters.  

---

## ✨ Features
- 📊 Input your **academic scores** and **skill assessments**.  
- 🧮 Calculate your **eligibility score** for campus placements.  
- 💡 Get **personalized insights** into areas of improvement.  

---

## 🛠️ How to Use
1. Navigate to the **Eligibility Calculation** section using the navigation bar.  
2. Fill in the required fields with your academic and skill data.  
3. Click **Calculate Eligibility** to see your results.  

---

## ⚠️ Note
This application uses a simple **scoring algorithm** and does **not guarantee placement**.  
It is intended for **educational purposes only**.  

---

📧 For any questions or feedback, please contact us at:  
**support@collegeplacements.com**
""", unsafe_allow_html=True)


# ============================================================
# STUDENTS INSIGHTS PAGE
# ============================================================

elif selected_page == "Students Insights":
    st.title("📊 Students Insights")

    db = DatabaseHandler()
    db.connect()

    queries = {
        "Placement Status Count": """
            SELECT placement_status, COUNT(*) AS total_students
            FROM placement_table
            GROUP BY placement_status;
        """,
        "Average Package by Batch": """
            SELECT s.course_batch, ROUND(AVG(pl.placement_package),2) AS avg_package
            FROM students_table s
            JOIN placement_table pl ON s.student_id = pl.student_id
            WHERE pl.placement_status='Placed'
            GROUP BY s.course_batch;
        """,
        "Gender-wise Placement": """
            SELECT s.gender, COUNT(*) AS total_students
            FROM students_table s
            JOIN placement_table pl ON s.student_id = pl.student_id
            GROUP BY s.gender;
        """,
        "Average Age by Batch": """
            SELECT course_batch, ROUND(AVG(age),2) AS avg_age
            FROM students_table
            GROUP BY course_batch;
        """,
        "Top Cities by Students": """
            SELECT city, COUNT(*) AS total_students
            FROM students_table
            GROUP BY city
            ORDER BY total_students DESC
            LIMIT 10;
        """,
        "Top Students by Problems Solved": """
            SELECT s.name, p.problems_solved
            FROM students_table s
            JOIN programming_table p ON s.student_id = p.student_id
            ORDER BY p.problems_solved DESC
            LIMIT 5;
        """,
        "Average Soft Skills by Batch": """
            SELECT s.course_batch,
            ROUND(AVG(
                ss.communication_skills +
                ss.teamwork_skills +
                ss.presentation_skills +
                ss.leadership_skills +
                ss.critical_thinking +
                ss.interpersonal_skills
            ) / 6, 2) AS avg_soft_skills
            FROM students_table s
            JOIN soft_skills_table ss ON s.student_id = ss.student_id
            GROUP BY s.course_batch;
        """,
        "Top Internships Completed": """
            SELECT s.name, pl.internships_completed
            FROM students_table s
            JOIN placement_table pl ON s.student_id = pl.student_id
            ORDER BY pl.internships_completed DESC
            LIMIT 5;
        """,
        "Package Distribution": """
            SELECT placement_package, COUNT(*) AS students
            FROM placement_table
            WHERE placement_status='Placed'
            GROUP BY placement_package;
        """,
        "Not Placed by Batch": """
            SELECT s.course_batch, COUNT(*) AS not_placed
            FROM students_table s
            JOIN placement_table pl ON s.student_id = pl.student_id
            WHERE pl.placement_status='Not Placed'
            GROUP BY s.course_batch;
        """
    }

    selected_query = st.selectbox("Select Insight", list(queries.keys()))
    df = db.execute_query(queries[selected_query])

    st.dataframe(df)

    # ---------------- SAFE PLOTTING ----------------
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if numeric_cols:
        fig, ax = plt.subplots()
        df.plot(kind="bar", x=df.columns[0], y=numeric_cols, ax=ax, legend=True)
        ax.set_title(selected_query)
        st.pyplot(fig)
    else:
        st.info("📌 No numeric data to plot for this selection.")

    db.close()


# ============================================================
# ELIGIBILITY CALCULATION PAGE
# ============================================================

elif selected_page == "Eligibility Calculation":
    st.title("🧮 Eligibility Calculator")

    with st.form("eligibility_form"):
        problems = st.number_input("Problems Solved", 0)
        assessments = st.number_input("Assessments Completed", 0)
        projects = st.number_input("Mini Projects", 0)
        certifications = st.number_input("Certifications", 0)

        communication = st.slider("Communication Skills", 1, 10, 5)
        teamwork = st.slider("Teamwork Skills", 1, 10, 5)
        presentation = st.slider("Presentation Skills", 1, 10, 5)
        leadership = st.slider("Leadership Skills", 1, 10, 5)
        critical = st.slider("Critical Thinking", 1, 10, 5)
        interpersonal = st.slider("Interpersonal Skills", 1, 10, 5)

        mock = st.slider("Mock Interview Score", 0, 10, 5)
        internships = st.number_input("Internships Completed", 0)

        submitted = st.form_submit_button("Calculate")

    if submitted:
        score = (
            problems * 0.05 +
            assessments * 0.05 +
            projects * 0.05 +
            certifications * 0.05 +
            ((communication + teamwork + presentation +
              leadership + critical + interpersonal) / 60) * 20 +
            mock * 0.1 +
            internships * 0.1
        )

        eligibility = min(score * 2.5, 100)

        st.metric("Eligibility Score", f"{eligibility:.2f} / 100")

        if eligibility >= 70:
            st.success("High Placement Readiness")
        elif eligibility >= 50:
            st.warning("Moderate Readiness")
        else:
            st.error("Low Readiness")


# ============================================================
# CREATOR INFO
# ============================================================

elif selected_page == "Creator Info":
    st.markdown("""
    ## 📌 About the Creator  
    - **Name:** Abhishek Gupta  
    - **Role:** Developer & Data Enthusiast  
    - **Email:** support@collegeplacements.com  
    ---
    💡 *This application was built using **Streamlit, MySQL, and Python** to help students analyze placement eligibility.*  
    """, unsafe_allow_html=True)
