import pandas as pd


def analyze_data(df):
    """
    Analyze financial transaction data.
    """

    # Normalize column names
    df.columns = [col.lower().strip() for col in df.columns]

    # Normalize Type values
    df["type"] = df["type"].astype(str).str.lower().str.strip()

    # Ensure Amount is numeric
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0)

    # Convert Date column
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Remove invalid dates
    df = df.dropna(subset=["date"])

    # Split income and expense
    income = df[df["type"] == "income"]
    expenses = df[df["type"] == "expense"]

    # Calculate totals
    total_income = income["amount"].sum()
    total_expense = expenses["amount"].sum()
    savings = total_income - total_expense

    # Top spending category
    if not expenses.empty:
        top_category = (
            expenses.groupby("category")["amount"]
            .sum()
            .idxmax()
        )
    else:
        top_category = "No Expenses"

    # Monthly spending (expenses only)
    monthly = (
        expenses.groupby(expenses["date"].dt.to_period("M"))["amount"]
        .sum()
    )

    # Summary
    summary = f"""
Total Income: ₹{total_income:,.2f}
Total Expenses: ₹{total_expense:,.2f}
Savings: ₹{savings:,.2f}

Top Spending Category: {top_category}

Monthly Spending:
{monthly.to_string()}
"""

    return {
        "income": total_income,
        "expenses": total_expense,
        "savings": savings,
        "top_category": top_category,
        "monthly": monthly,
        "summary": summary,
    }