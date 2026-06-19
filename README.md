# 💰 AI Financial Advisor

An AI-powered financial analysis application that helps users understand their income, expenses, savings, and spending habits through interactive visualizations and personalized AI recommendations.

## 🚀 Features

* Upload CSV or Excel financial data
* Automatic data cleaning and preprocessing
* Income, Expense, and Savings analysis
* Financial Health Score
* Interactive charts and visualizations
* AI-generated financial advice using Groq LLM
* Downloadable PDF financial report
* SQLite database for analysis history
* Streamlit web interface

## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* Matplotlib
* Groq API (Llama 3.3)
* SQLite
* ReportLab
* Python-dotenv

## 📂 Project Structure

```
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
```

## ⚙️ Installation

```bash
git clone https://github.com/your-username/ai-financial-advisor.git

cd ai-financial-advisor

pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Run the application:

```bash
streamlit run app.py
```

## 📊 Sample Workflow

1. Upload a CSV or Excel file.
2. Review cleaned financial data.
3. Analyze income, expenses, and savings.
4. View charts and financial insights.
5. Receive AI-generated financial recommendations.
6. Download a PDF report.

## 🎯 Skills Demonstrated

* Data Analysis
* Data Preprocessing
* Python Development
* Streamlit
* SQLite Database
* API Integration
* Generative AI
* Prompt Engineering
* Data Visualization
* PDF Report Generation

## 📄 License

This project is created for learning, portfolio, and demonstration purposes.
