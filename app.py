import streamlit as st

# Import helper modules
from src.csv_loader import load_file
from src.preprocess import preprocess_data
from src.analyzer import analyze_data

# Import charts
from src.charts import (
    expense_category_charts,
    income_vs_expense_chart,
    monthly_spending_chart,
    savings_chart,
)

# Import AI module
from src.ai_advisor import get_financial_advice

# Import database functions
from src.database import (
    create_table,
    save_analysis,
    get_history,
)

# Import PDF generator
from src.pdf_report import generate_pdf_report

# Import helper functions
from src.utils import (
    formate_currency,
    current_datetime,
    financial_health_score,
)

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="AI Financial Advisor",
    page_icon="💰",
    layout="wide",
)

# Create database table
create_table()

# ---------------- APPLICATION TITLE ----------------

st.title("💰 AI Financial Advisor")

st.markdown("""
Analyze your financial transactions, visualize your spending,
and receive AI-powered financial recommendations.
""")

# ---------------- SIDEBAR ----------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    ["Dashboard", "History"]
)

# ---------------- DASHBOARD ----------------

if page == "Dashboard":

    st.header("Upload Financial Transactions")

    uploaded_file = st.file_uploader(
        "Choose a CSV or Excel file",
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:

        try:
            # Load file
            df = load_file(uploaded_file)

            st.success("File loaded successfully.")

            st.subheader("Raw Data")
            st.dataframe(df)

            # Preprocess data
            df = preprocess_data(df)

            st.success("Data preprocessing completed.")

            st.subheader("Cleaned Data")
            st.dataframe(df)

            # Analyze data
            analysis = analyze_data(df)

            total_income = analysis["income"]
            total_expense = analysis["expenses"]
            savings = analysis["savings"]
            top_category = analysis["top_category"]
            monthly_data = analysis["monthly"]
            summary = analysis["summary"]

            # ---------------- METRICS ----------------

            st.header("Financial Summary")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Total Income",
                    formate_currency(total_income)
                )

            with col2:
                st.metric(
                    "Total Expense",
                    formate_currency(total_expense)
                )

            with col3:
                st.metric(
                    "Savings",
                    formate_currency(savings)
                )

            score = financial_health_score(
                total_income,
                total_expense
            )

            st.success(f"Financial Health Score: {score}/10")

            # ---------------- CHARTS ----------------

            st.header("Financial Charts")

            expense_category_charts(df)

            income_vs_expense_chart(
                total_income,
                total_expense
            )

            monthly_spending_chart(monthly_data)

            savings_chart(
                total_income,
                total_expense
            )

            # ---------------- AI ADVICE ----------------

            st.header("AI Financial Advice")

            with st.spinner("Generating AI Advice..."):
                ai_advice = get_financial_advice(summary)

            st.markdown(ai_advice)

            # ---------------- SAVE HISTORY ----------------

            save_analysis(
                current_datetime(),
                total_income,
                total_expense,
                savings,
                top_category,
                ai_advice,
            )

            # ---------------- PDF REPORT ----------------

            pdf_path = generate_pdf_report(
                total_income,
                total_expense,
                savings,
                top_category,
                ai_advice,
            )

            with open(pdf_path, "rb") as pdf_file:
                st.download_button(
                    "📄 Download PDF Report",
                    pdf_file,
                    file_name="Financial_Report.pdf",
                    mime="application/pdf",
                )

        except Exception as e:
            st.error(f"Error: {e}")

# ---------------- HISTORY ----------------

elif page == "History":

    st.header("Financial Analysis History")

    history = get_history()

    if history:
        st.dataframe(
            history,
            use_container_width=True
        )
    else:
        st.info("No history available.")