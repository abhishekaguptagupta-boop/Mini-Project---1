# ============================================================
# STUDENT PLACEMENT ELIGIBILITY & INSIGHTS APPLICATION
# ============================================================

from faker import Faker
import random
import pandas as pd

fake = Faker()

# ------------------ STUDENTS TABLE ------------------ #
students_table = []
for _ in range(100):
    student = {
        "student_id": fake.unique.random_int(min=1000, max=9999),
        "name": fake.name(),
        "age": fake.random_int(min=18, max=25),
        "gender": fake.random_element(elements=("Male", "Female")),
        "email": fake.email(),
        "phone_number": fake.random_number(digits=10, fix_len=True),
        "enrollment_year": fake.year(),
        "course_batch": fake.random_element(elements=("B.Tech", "M.Tech", "MBA", "BBA")),
        "city": fake.city(),
        "graduation_year": fake.year(),
    }
    students_table.append(student)

df_students = pd.DataFrame(students_table)
df_students.to_csv("students_data.csv", index=False)

# ------------------ PROGRAMMING TABLE ------------------ #
programming_table = []
for _ in range(100):
    programming = {
        "programming_id": fake.unique.random_int(min=1000, max=9999),
        "student_id": random.choice(df_students['student_id']),
        "language": fake.random_element(elements=("Python", "Java", "C++", "JavaScript", "SQL")),
        "problems_solved": fake.random_int(min=0, max=100),
        "assessments_completed": fake.random_int(min=0, max=50),
        "mini_projects": fake.random_int(min=0, max=10),
        "certifications_earned": fake.random_int(min=0, max=5),
        "latest_project_score": fake.random_int(min=0, max=10),
    }
    programming_table.append(programming)

pd.DataFrame(programming_table).to_csv("programming_data.csv", index=False)

# ------------------ SOFT SKILLS TABLE ------------------ #
soft_skills_table = []
for _ in range(100):
    soft_skills = {
        "soft_skills_id": fake.unique.random_int(min=1000, max=9999),
        "student_id": random.choice(df_students['student_id']),
        "communication_skills": fake.random_int(min=1, max=10),
        "teamwork_skills": fake.random_int(min=1, max=10),
        "presentation_skills": fake.random_int(min=1, max=10),
        "leadership_skills": fake.random_int(min=1, max=10),
        "critical_thinking": fake.random_int(min=1, max=10),
        "interpersonal_skills": fake.random_int(min=1, max=10),
    }
    soft_skills_table.append(soft_skills)

pd.DataFrame(soft_skills_table).to_csv("soft_skills_data.csv", index=False)

# ------------------ PLACEMENT TABLE ------------------ #
placement_table = []
for _ in range(100):
    placement = {
        "placement_id": fake.unique.random_int(min=1000, max=9999),
        "student_id": random.choice(df_students['student_id']),
        "mock_interviews_score": fake.random_int(min=0, max=10),
        "internships_completed": fake.random_int(min=0, max=5),
        "placement_status": fake.random_element(elements=("Placed", "Not Placed")),
        "company_name": fake.company(),
        "placement_package": fake.random_int(min=3, max=30) * 10000,
        "interview_rounds_cleared": fake.random_int(min=1, max=5),
        "placement_date": fake.date_between(start_date='-1y', end_date='today'),
    }
    placement_table.append(placement)

pd.DataFrame(placement_table).to_csv("placement_data.csv", index=False)