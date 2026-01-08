# Mini-Project---1
Application to check the eligibility of candidates for placement.

**Student Placement Eligibility & Insights Application**

📌 **Overview**

The Student Placement Eligibility & Insights Application is a data-driven Streamlit web app that helps evaluate student placement readiness based on academic performance, technical skills, and soft skills.
It also provides SQL-based placement insights using data stored in a MySQL database.

👨‍💻 **Author**

Abhishek Gupta

🛠️ **Tech Stack**

Python
Streamlit
MySQL
Pandas
Matplotlib
Faker
SQL & OOP Principles

🎯 **Features**

🔐 Secure database access using environment variables
📊 SQL-driven placement insights with visualizations
🧮 Placement eligibility score (out of 100)
📈 Safe plotting to avoid numeric data errors
🧱 Object-Oriented database handling

🗂️ **Database Tables**
students_table
programming_table
soft_skills_table
placement_table
(All linked using student_id)

📊 **Students Insights (SQL Analysis)**

1.	Placement Status Count
2.	Average Package by Batch
3.	Gender-wise Placement
4.	Average Age by Batch
5.	Top Cities by Students
6.	Top Students by Problems Solved
7.	Average Soft Skills by Batch
8.	Top Internships Completed
9.	Package Distribution
10.	Not Placed by Batch


🧮 **Eligibility Calculation**

**Users input:**

12th Grade Percentage,
Programming Problems Solved,
Graduation Percentage,
Assessments Completed,
Certifications Earned,
Mini Projects Completed,
Skill Assesments Scores etc.

The app categorizes readiness as:

✅ Eligible
⚠️ Moderate
❌ Not Eligible
