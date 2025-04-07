import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Student Data Generator", layout="wide")
st.title("Student CSV File Generator")

names = ["Hammad", "Taha", "Salman", "Sufyan", "Adnan", "Huzaifa", "Sameer", "Ikhlas", "Abid", "Asim"]

students = []

for i in range( len(names)):
    student = {
        "Id": 1,
        "Name": random.choice(names),
        "Age": random.randint(15, 25),
        "Grade": random.choice(["A", "B", "C", "D", "E", "F"]),
        "Marks": random.randint(40, 100)
    }
    students.append(student)


df = pd.DataFrame(students)

st.subheader("Generated Student Data")
st.dataframe(df)

csv_file = df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV File", csv_file, "students.csv", "text/csv")

st.success("Students Record Generated Sucessfuly!")
