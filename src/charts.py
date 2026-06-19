import streamlit as st
import matplotlib.pyplot as plt


def expense_category_charts(df):
    """Expense by category pie chart."""

    expense_df = df[df["type"] == "expense"]

    if expense_df.empty:
        st.warning("No expense data available.")
        return

    category = expense_df.groupby("category")["amount"].sum()

    fig, ax = plt.subplots()
    ax.pie(
        category,
        labels=category.index,
        autopct="%1.1f%%",
        startangle=90,
    )
    ax.set_title("Expense by Category")

    st.pyplot(fig)


def income_vs_expense_chart(income, expense):
    """Income vs Expense bar chart."""

    fig, ax = plt.subplots()

    ax.bar(
        ["Income", "Expense"],
        [income, expense]
    )

    ax.set_ylabel("Amount")
    ax.set_title("Income vs Expense")

    st.pyplot(fig)


def monthly_spending_chart(monthly):
    """Monthly spending line chart."""

    if monthly.empty:
        st.warning("No monthly spending data.")
        return

    fig, ax = plt.subplots()

    ax.plot(
        monthly.index.astype(str),
        monthly.values,
        marker="o"
    )

    ax.set_title("Monthly Spending")
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount")

    plt.xticks(rotation=45)

    st.pyplot(fig)


def savings_chart(income, expense):
    """Savings chart."""

    savings = income - expense

    fig, ax = plt.subplots()

    ax.bar(
        ["Savings"],
        [savings]
    )

    ax.set_ylabel("Amount")
    ax.set_title("Savings")

    st.pyplot(fig)