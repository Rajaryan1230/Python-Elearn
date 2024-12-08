import pandas as pd

df = pd.read_csv('students.csv')

print("First 10 students:")
print(df.head(10))

df['total_marks'] = df[['S1', 'S2', 'S3']].sum(axis=1)
print("All students with total marks:")
print(df)

female_students = df[df['gender'] == 'F']

female_total_marks = female_students[['student_name', 'total_marks']]
print("Female students' total marks:")
print(female_total_marks)

unique_records = df[['roll_number', 'S1']].drop_duplicates()
print("Unique records (roll number and S1 marks):")
print(unique_records)

female_s2_marks = df[df['gender'] == 'F'][['student_name', 'S2']]
print("Female students and their S2 marks:")
print(female_s2_marks)

male_s1_marks_ascending = df[df['gender'] == 'M'][['student_name', 'S1']].sort_values(by='S1')
print("Male students' S1 marks in ascending order:")
print(male_s1_marks_ascending)

students_starting_with_s = df[df['student_name'].str.startswith('S')]
print("Student names starting with 'S':")
print(students_starting_with_s)

students_ending_with_n = df[df['student_name'].str.endswith('n')]
print("Student names ending with 'n':")
print(students_ending_with_n)

df['percentage'] = df['total_marks'] / 3
print("Students with percentage:")
print(df[['student_name', 'percentage']])

def assign_grade(percentage):
    if (percentage >= 80):
        return 'A'
    elif (percentage >= 60):
        return 'B'
    elif (percentage >= 40):
        return 'C'
    else:
        return 'FAIL'

df['grade'] = df['percentage'].apply(assign_grade)
print("Students with grades:")
print(df[['student_name', 'percentage', 'grade']])

import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x='gender', y='percentage', data=df)
plt.title("Male and Female Students' Percentage")
plt.show()

pass_fail_counts = df['grade'].value_counts()
pass_fail_counts.plot.pie(autopct='%1.1f%%', startangle=90, colors=['#4CAF50', '#FFC107'])
plt.title("PASS and FAIL Percentage")
plt.ylabel('')
plt.show()