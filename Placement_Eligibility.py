# ============================================================
# STUDENT PLACEMENT ELIGIBILITY & INSIGHTS APPLICATION
# ============================================================

import os
import streamlit as st
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

# ---------------- Load environment variables ----------------
load_dotenv()  # loads .env file

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = int(os.getenv("DB_PORT", 3306))

# ----------------- Check if password exists -----------------
if not DB_PASSWORD:
    st.error("❌ MySQL password not found in .env file. Please set DB_PASSWORD in your .env.")
    st.stop()  # stop the app if password is missing

# ============================================================
# DATABASE HANDLER (OOP)
# ============================================================
class DatabaseHandler:
    """Handles MySQL connection and query execution"""

    def __init__(self):
        self.host = DB_HOST
        self.user = DB_USER
        self.password = DB_PASSWORD
        self.database = DB_NAME
        self.port = DB_PORT
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
                auth_plugin="mysql_native_password"
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            st.error(f"❌ Failed to connect to MySQL: {err}")
            st.stop()

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

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

# ============================================================
# ELIGIBILITY CALCULATOR (OOP)
# ============================================================
class EligibilityCalculator:
    """Calculates eligibility score based on student inputs"""

    @staticmethod
    def calculate(programming, assessments, projects, certifications, skills_total, mock_score, internships):
        score = min(100, (
            (programming/100)*20 +
            (assessments/50)*10 +
            (projects/10)*10 +
            (certifications/5)*10 +
            (skills_total/60)*20 +
            (mock_score/10)*10 +
            (internships/5)*10
        ))
        return score

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
1. Navigate to the **Eligibility Calculation** section using the sidebar.  
2. Fill in the required fields with your academic and skill data.  
3. Click **Calculate Eligibility** to see your results.  

---

## ⚠️ Note
This application uses a simple **scoring algorithm** and does **not guarantee placement**.  
It is intended for **educational purposes only**.  

📧 Contact: **support@collegeplacements.com**
""", unsafe_allow_html=True)

# ============================================================
# STUDENTS INSIGHTS PAGE
# ============================================================
elif selected_page == "Students Insights":
    st.title("📊 Students Insights")

    with DatabaseHandler() as db:
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

    # Plot numeric data
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if numeric_cols:
        st.bar_chart(df.set_index(df.columns[0]))
    else:
        st.info("📌 No numeric data to plot for this selection.")

    # Allow download
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Data as CSV",
        data=csv,
        file_name=f"{selected_query.replace(' ', '_')}.csv",
        mime='text/csv'
    )

# ============================================================
# ELIGIBILITY CALCULATION PAGE
# ============================================================
elif selected_page == "Eligibility Calculation":
    st.title("🧮 Eligibility Calculation")

    st.markdown("Input your academic scores and skill assessments to calculate your placement eligibility.")

    with st.form("eligibility_form"):
        st.subheader("Academic Scores")
        col1, col2 = st.columns(2)
        with col1:
            twelfth_percentage = st.number_input("12th Grade %", 0.0, 100.0, 75.0)
            graduation_percentage = st.number_input("Graduation %", 0.0, 100.0, 70.0)
            certifications_earned = st.number_input("Certifications Earned", 0, step=1)
        with col2:
            programming_problems_solved = st.number_input("Programming Problems Solved", 0, step=1)
            assessments_completed = st.number_input("Assessments Completed", 0, step=1)
            mini_projects_completed = st.number_input("Mini Projects Completed", 0, step=1)

        st.subheader("Skill Assessments")
        col3, col4 = st.columns(2)
        with col3:
            communication_skills = st.slider("Communication (1-10)", 1, 10, 5)
            teamwork_skills = st.slider("Teamwork (1-10)", 1, 10, 5)
            presentation_skills = st.slider("Presentation (1-10)", 1, 10, 5)
        with col4:
            leadership_skills = st.slider("Leadership (1-10)", 1, 10, 5)
            critical_thinking = st.slider("Critical Thinking (1-10)", 1, 10, 5)
            interpersonal_skills = st.slider("Interpersonal (1-10)", 1, 10, 5)

        mock_interview_score = st.slider("Mock Interview Score (0-10)", 0, 10, 5)
        internships_completed = st.number_input("Internships Completed", 0, step=1)

        submitted = st.form_submit_button("Calculate Eligibility")

    if submitted:
        skills_total = communication_skills + teamwork_skills + presentation_skills + \
                       leadership_skills + critical_thinking + interpersonal_skills

        eligibility_score = EligibilityCalculator.calculate(
            programming_problems_solved,
            assessments_completed,
            mini_projects_completed,
            certifications_earned,
            skills_total,
            mock_interview_score,
            internships_completed
        )

        st.subheader("🎯 Eligibility Score")
        st.metric(label="Eligibility Score", value=f"{eligibility_score:.2f} / 100")

        if eligibility_score >= 70:
            st.success("✅ Congratulations! You are likely eligible for campus placements.")
        elif eligibility_score >= 50:
            st.warning("⚠️ Moderate chance of eligibility. Consider improving your skills.")
        else:
            st.error("❌ You may not be eligible at this time. Focus on academics and skills.")

# ============================================================
# CREATOR INFO
# ============================================================
elif selected_page == "Creator Info":
    st.markdown("""
## 📌 About the Creator
- **Name:** Abhishek Gupta
- **Role:** Developer & Data Enthusiast
- **Email:** support@collegeplacements.com

💡 *This application was built using **Streamlit, MySQL, and Python** to help students analyze placement eligibility.*
""", unsafe_allow_html=True)
