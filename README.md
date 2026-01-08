# Mini-Project---1
Application to check the eligibility of candidates for placement.
# 🎓 Placement Eligibility Streamlit Application

## Project Overview
This project is a **data-driven Streamlit application** that evaluates students' eligibility for campus placements based on their academic performance, programming skills, and soft skills. It also provides insights and visualizations from the student database.

The project leverages:
- Python (OOP)
- MySQL Database
- Streamlit for interactive UI
- Faker library for synthetic data generation
- SQL queries for insights
- Matplotlib for visualizations

---

## 🛠️ Skills Gained
- Building **interactive data-driven applications** using Streamlit.
- Generating **synthetic datasets** with Faker.
- Implementing **Object-Oriented Programming (OOP)** principles in Python.
- Writing **SQL queries** for analytics and insights.
- Working with **MySQL relational databases**.
- Creating **dynamic visualizations** for business decisions.

---

## 📚 Domain
**EdTech / Student Placement Management**

---

## 🔹 Problem Statement
Develop an application that allows placement teams or students to input eligibility criteria. Based on these inputs, the system queries a database of students to display:
- Eligible candidates
- Performance insights
- Placement readiness scores

---

## ⚡ Business Use Cases
1. **Placement Management:** Shortlist students using customizable criteria.
2. **Student Performance Tracking:** Evaluate readiness for placement.
3. **Interactive Analytics:** Provide insights via interactive dashboards.

---

## 🚀 Approach
### Step 1: Dataset Creation
- Generated four related tables using the Faker library:
  - **Students Table**: Personal and enrollment details.
  - **Programming Table**: Performance in programming tasks.
  - **Soft Skills Table**: Communication, teamwork, and leadership scores.
  - **Placements Table**: Placement readiness, mock interviews, and internships.
- Established relationships among these tables via `student_id`.

### Step 2: Data Storage
- Stored data in **MySQL** database.
- Implemented **OOP** in Python for database operations.

### Step 3: Streamlit Application
- Users can:
  - Input eligibility criteria (e.g., programming problems solved, soft skills scores)
  - View eligible student details dynamically
  - Explore insights through visualizations

### Step 4: SQL Queries & Insights
- Created queries like:
  - Placement status count
  - Average package by batch
  - Gender-wise placement distribution

---

## 📊 Project Features
- **Interactive Dashboard:** Dynamic filtering of students based on input criteria.
- **Eligibility Score Calculation:** Combines technical and soft skills into a score.
- **Insights & Visualizations:** Understand student performance trends and placements.
- **Modular Code:** OOP-based structure for database handling and query execution.

---

## 🔧 Technology Stack
- **Frontend / Dashboard:** Streamlit
- **Backend:** Python 3.x
- **Database:** MySQL
- **Data Generation:** Faker
- **Visualization:** Matplotlib
- **Version Control:** Git / GitHub
