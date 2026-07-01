# 💰 AI Financial Advisor

An AI-powered financial analysis application that helps users understand their income, expenses, savings, and spending habits through interactive visualizations and personalized AI recommendations.

---

## 🚀 Features

- Upload CSV or Excel financial data  
- Automatic data cleaning and preprocessing  
- Income, Expense, and Savings analysis  
- Financial Health Score  
- Interactive charts and visualizations  
- AI-generated financial advice using Groq API  
- Downloadable PDF financial report  
- SQLite database for analysis history  
- Streamlit web interface  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Pandas  
- Matplotlib  
- Groq API (GPT-OSS 120B / LLM)  
- SQLite  
- ReportLab  
- python-dotenv  

---

## 📂 Project Structure

```text
ai-financial-advisor/
│── app.py
│── requirements.txt
│── .env
│── database/
│── reports/
│── src/
│   ├── analyzer.py
│   ├── ai_advisor.py
│   ├── charts.py
│   ├── csv_loader.py
│   ├── database.py
│   ├── pdf_report.py
│   ├── preprocess.py
│   └── utils.py
