# 🧠 Text-to-SQL with Gemini AI

This project is a simple Streamlit web app that converts natural language questions into SQL queries using Google Gemini API, and executes them on a connected **MySQL** or **SQLite** database.

---

## 🚀 Features
- Ask questions in plain English
- Converts to SQL using Gemini AI
- Executes the query on your database
- Displays results in a nice format

---

## 🛠️ Tech Stack
- Python 🐍
- Streamlit 📊
- Google Gemini API 🔮
- MySQL / SQLite 💾

---

## ⚙️ Setup Instructions
git clone https://github.com/your-username/text-to-sql-app.git
cd text-to-sql-app
pip install -r requirements.txt

## Add your Gemini API key in a .env file:
GOOGLE_API_KEY=your_api_key_here

## 🏁 Run the App
streamlit run app.py

## 📦 Folder Structure
├── app.py
├── mysql.py
├── MySQL
├── .env
├── requirements.txt
└── README.md
