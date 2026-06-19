def financial_analysis_prompt(financial_summary):
    """
    Create the prompt sent to the AI model.

    Parameters
    ----------
    financial_summary : str

    Returns
    -------
    str
        Complete prompt ready to send to Groq.
    """

    return f"""
You are an experienced financial advisor.

Your job is to analyze the user's financial data and provide practical, easy-to-understand advice.

Use the following format:

----------------------------------------

1. Financial Health Score (0-10)

2. Overall Financial Summary

3. Spending Analysis

- Highest spending category
- Unnecessary expenses
- Spending habits

4. Budget Recommendations

- Monthly budget
- Expense reduction ideas

5. Savings Suggestions

- Emergency fund
- Saving strategies

6. Investment Suggestions

- Beginner-friendly investment ideas
- Long-term wealth creation

7. Financial Risks

Mention any financial risks you notice.

8. 30-Day Action Plan

Give five practical steps.

----------------------------------------

Financial Data:

{financial_summary}

Keep the explanation simple and actionable.
"""


def budget_planner_prompt(income, expense):
    """
    Create a prompt for generating a personalized budget.
    """

    return f"""
You are a personal budgeting expert.

Income:
₹{income}

Expenses:
₹{expense}

Create:

1. Ideal monthly budget

2. Savings target

3. Expense reduction plan

4. Budget table

5. Money-saving tips

Make the advice practical.
"""


def investment_prompt(savings):
    """
    Create a prompt for investment suggestions.
    """

    return f"""
You are an investment advisor.

Monthly Savings:
₹{savings}

Suggest:

1. Beginner investment ideas

2. Low-risk investments

3. Medium-risk investments

4. Long-term wealth plan

5. Mistakes to avoid

Do not give guaranteed return promises.
"""