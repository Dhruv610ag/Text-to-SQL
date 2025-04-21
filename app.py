# text_to_sql_app.py
from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to call Gemini and get SQL query
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')  # or gemini-pro, based on what’s available
    response = model.generate_content([prompt[0], question])
    return response.text.strip()

# Function to read and return rows from SQLite
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        curr = conn.cursor()
        curr.execute(sql)
        rows = curr.fetchall()
        conn.commit()
        conn.close()
        return rows
    except Exception as e:
        return [("Error", str(e))]

# SQL-to-text prompt for Gemini
prompt = ["""
You are an expert in converting English questions to SQL queries.
The SQL database is named student.db and the STUDENT table has these columns: NAME, CLASS, SECTION, MARKS.

Examples:
Q: How many entries are present?
A: SELECT COUNT(*) FROM STUDENT;

Q: Show all students in class 10?
A: SELECT * FROM STUDENT WHERE CLASS = "10";

Please return only the SQL query with no explanation, no triple quotes, and no extra text.
"""]

# Streamlit frontend
st.set_page_config(page_title="SQL Query Retriever using Gemini")
st.title("🔍 Text-to-SQL Gemini App")
st.write("Ask questions about the `STUDENT` database in natural language.")

# Input & button
question = st.text_input("Enter your question:")
if st.button("Ask"):
    sql_query = get_gemini_response(question, prompt)
    st.code(sql_query, language='sql')

    # Execute and show results
    result = read_sql_query(sql_query, "student.db")
    st.subheader("📊 Query Results:")
    if result:
        for row in result:
            st.write(row)
    else:
        st.write("No results found or invalid query.")
