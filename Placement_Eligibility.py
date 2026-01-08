# #------------------ Data Generation Script ------------------ #

# from faker import Faker
# import random
# import pandas as pd

# fake = Faker()

# # ------------------ Students Table ------------------ #
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

# df_students = pd.DataFrame(students_table)
# print("Students Table:\n", df_students.head(), "\n")
# df_students.to_csv("students_data.csv", index=False)

# # ------------------ Programming Table ------------------ #
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

# df_programming = pd.DataFrame(programming_table)
# print("Programming Table:\n", df_programming.head(), "\n")
# df_programming.to_csv("programming_data.csv", index=False)

# # ------------------ Soft Skills Table ------------------ #
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

# df_soft_skills = pd.DataFrame(soft_skills_table)
# print("Soft Skills Table:\n", df_soft_skills.head(), "\n")
# df_soft_skills.to_csv("soft_skills_data.csv", index=False)

# # ------------------ Placement Table ------------------ #
# placement_table = []
# for _ in range(100):
#     placement = {
#         "placement_id": fake.unique.random_int(min=1000, max=9999),
#         "student_id": random.choice(df_students['student_id']),
#         "mock_interviews_score": fake.random_int(min=0, max=10),
#         "internships_completed": fake.random_int(min=0, max=5),
#         "placement_status": fake.random_element(elements=("Placed", "Not Placed")),
#         "company_name": fake.company(),
#         "placement_package": fake.random_int(min=3, max=30) * 10000,  # in thousands
#         "interview_rounds_cleared": fake.random_int(min=1, max=5),
#         "placement_date": fake.date_between(start_date='-1y', end_date='today'),
#     }
#     placement_table.append(placement)

# df_placement = pd.DataFrame(placement_table)
# print("Placement Table:\n", df_placement.head(), "\n")
# df_placement.to_csv("placement_data.csv", index=False)

# #------------------ MySQL Table Creation Script ------------------ #

# import mysql.connector

# conn_mysql = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="Hope@3103"
# )

# cursor_mysql = conn_mysql.cursor()
# print("MySQL Connection Successful")

# # Create Database
# cursor_mysql.execute("CREATE DATABASE IF NOT EXISTS student_db")
# cursor_mysql.execute("USE student_db")

# # ------------------ STUDENTS TABLE ------------------
# cursor_mysql.execute("""
# CREATE TABLE IF NOT EXISTS students_table (
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

# # ------------------ PROGRAMMING TABLE ------------------
# cursor_mysql.execute("""
# CREATE TABLE IF NOT EXISTS programming_table (
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

# # ------------------ SOFT SKILLS TABLE ------------------
# cursor_mysql.execute("""
# CREATE TABLE IF NOT EXISTS soft_skills_table (
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

# # ------------------ PLACEMENT TABLE ------------------
# cursor_mysql.execute("""
# CREATE TABLE IF NOT EXISTS placement_table (
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

# conn_mysql.commit()
# cursor_mysql.close()
# conn_mysql.close()

# print("✅ All tables created successfully")

# import mysql.connector

# conn_mysql = mysql.connector.connect(
#     host="127.0.0.1",       # or "localhost"
#     user="root",
#     password="Hope@3103",   # your password
#     database="student_db",
#     port=3306               # default MySQL port
# )

# cursor_mysql = conn_mysql.cursor()
# print("Connected to student_db successfully")

#Application Code Starts Here
# ------------------------ IMPORTS ------------------------ #
import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# ------------------------ DATABASE HANDLER ------------------------ #
class DatabaseHandler:
    """OOP class to handle MySQL database connection and queries."""
    def __init__(self, host="127.0.0.1", user="root", password="", database="student_db", port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
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


# ------------------------ SIDEBAR NAVIGATION ------------------------ #
st.navigation_bar = st.sidebar.radio(
    "Navigation",
    ["Introduction", "Students Insights", "Eligibility Calculation", "Creator Info"]
)

# ------------------------ INTRODUCTION ------------------------ #
if st.navigation_bar == "Introduction":
    st.markdown("""
# 🎓 Student Placement Eligibility Application  

Welcome to the **Student Placement Prediction Application**!  
This tool helps students understand their eligibility for **campus placements** based on academic and skill-based parameters.  

---  
## ✨ Features
- 📊 Input your **academic scores** and **skill assessments**.  
- 🧮 Calculate your **eligibility score** for campus placements.  
- 💡 Get **personalized insights** into areas of improvement.  

---  
## 🛠️ How to Use
1. Navigate to the **Eligibility Calculation** section.  
2. Fill in the required fields.  
3. Click **Calculate Eligibility** to see results.  

---  
## ⚠️ Note
This application uses a **scoring algorithm** and does **not guarantee placement**.  
It is intended for **educational purposes only**.  

📧 Contact: **support@collegeplacements.com**
""", unsafe_allow_html=True)

# ------------------------ STUDENTS INSIGHTS ------------------------ #
elif st.navigation_bar == "Students Insights":
    st.title("📊 Students Insights")
    st.write("Insights from student database with dynamic visualizations.")

    try:
        db = DatabaseHandler(password="Hope@3103")
        db.connect()

        # SQL queries dictionary
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
                SELECT s.gender, COUNT(*) AS total,
                       SUM(CASE WHEN pl.placement_status='Placed' THEN 1 ELSE 0 END) AS placed_students
                FROM students_table s
                JOIN placement_table pl ON s.student_id = pl.student_id
                GROUP BY s.gender;
            """
        }

        selected_query = st.selectbox("Select Insight", list(queries.keys()))
        df = db.execute_query(queries[selected_query])
        st.subheader(selected_query)
        st.dataframe(df)

        # ------------------------ VISUALIZATIONS ------------------------ #
        if selected_query == "Placement Status Count":
            fig, ax = plt.subplots()
            ax.bar(df['placement_status'], df['total_students'], color=['green','red'])
            ax.set_xlabel("Placement Status")
            ax.set_ylabel("Number of Students")
            ax.set_title("Placement Status Distribution")
            st.pyplot(fig)

        elif selected_query == "Average Package by Batch":
            fig, ax = plt.subplots()
            ax.bar(df['course_batch'], df['avg_package'], color='skyblue')
            ax.set_xlabel("Batch")
            ax.set_ylabel("Average Package")
            ax.set_title("Average Placement Package by Batch")
            st.pyplot(fig)

        elif selected_query == "Gender-wise Placement":
            fig, ax = plt.subplots()
            df.plot(kind='bar', x='gender', y=['total','placed_students'], ax=ax)
            ax.set_title("Gender-wise Placement Count")
            st.pyplot(fig)

        db.close()

    except mysql.connector.Error as err:
        st.error(f"Database Error: {err}")

# ------------------------ ELIGIBILITY CALCULATION ------------------------ #
elif st.navigation_bar == "Eligibility Calculation":
    st.title("🧮 Eligibility Calculation")
    st.markdown("Input your academic and skill scores to calculate placement eligibility.")

    with st.form("eligibility_form"):
        st.subheader("Academic Scores")
        col1, col2 = st.columns(2)
        with col1:
            twelfth_percentage = st.number_input("12th Grade %", min_value=0.0, max_value=100.0, step=0.1)
            graduation_percentage = st.number_input("Graduation %", min_value=0.0, max_value=100.0, step=0.1)
            certifications_earned = st.number_input("Certifications Earned", min_value=0, step=1)
        with col2:
            programming_problems_solved = st.number_input("Programming Problems Solved", min_value=0, step=1)
            assessments_completed = st.number_input("Assessments Completed", min_value=0, step=1)
            mini_projects_completed = st.number_input("Mini Projects Completed", min_value=0, step=1)

        st.subheader("Skill Assessments")
        skills_col1, skills_col2 = st.columns(2)
        with skills_col1:
            communication_skills = st.slider("Communication Skills",1,10,5)
            teamwork_skills = st.slider("Teamwork Skills",1,10,5)
            presentation_skills = st.slider("Presentation Skills",1,10,5)
        with skills_col2:
            leadership_skills = st.slider("Leadership Skills",1,10,5)
            critical_thinking = st.slider("Critical Thinking",1,10,5)
            interpersonal_skills = st.slider("Interpersonal Skills",1,10,5)

        mock_interview_score = st.slider("Mock Interview Score",0,10,5)
        internships_completed = st.number_input("Internships Completed", min_value=0, step=1)

        submitted = st.form_submit_button("Calculate Eligibility")

    if submitted:
        # Raw scoring formula
        raw_score = (
            programming_problems_solved*0.05 +
            assessments_completed*0.05 +
            mini_projects_completed*0.05 +
            certifications_earned*0.05 +
            ((communication_skills + teamwork_skills + presentation_skills + leadership_skills + critical_thinking + interpersonal_skills)/60)*20 +
            mock_interview_score*0.1 +
            internships_completed*0.1
        )
        eligibility_score = min(raw_score*2.5,100)

        st.subheader("Your Eligibility Score")
        st.metric("Eligibility Score", f"{eligibility_score:.2f} / 100")

        if eligibility_score >= 70:
            st.success("✅ High chance of campus placement eligibility.")
        elif eligibility_score >= 50:
            st.warning("⚠️ Moderate chance. Improve technical and soft skills.")
        else:
            st.error("❌ Low chance currently. Focus on skill enhancement.")

# ------------------------ CREATOR INFO ------------------------ #
elif st.navigation_bar == "Creator Info":
    st.title("👨‍💻 Creator Information")
    st.markdown("""
    ## 📌 About the Creator  
    - **Name:** Abhishek Gupta  
    - **Role:** Developer & Data Enthusiast  
    - **Email:** support@collegeplacements.com  
    ---  
    💡 *Built using Streamlit, MySQL, Python, and OOP principles for student placement eligibility analysis.*
    """, unsafe_allow_html=True)