from datetime import datetime


def formate_currency(amount):
    """
    Convert a number into Indian Rupee formate.
    
    Example
    -------
    Input:
        25000
        
    Output:
         ₹25,000.00
    """
    # return formatted currency
    return f"₹{amount:,.2f}"

# calculate percentage

def calculate_percentage(part , total):
    """
    Calculate percentage.
    
    Formula
    
    Perecntage = (Part / Total) × 100
    """

    # avoid divison by zero
    if total == 0:
        return 0
    return round((part /total) * 100, 2)

# formate date

def formate_date(date):
    """
    Convert datetime object into readable formate.
    
    Example
    
    Input:
        2026-07-15
    
    Output:
        15 jul 2026
    """

    return date.strftime("%d %b %Y")

# financial health score

def financial_health_score(income, expense):
    """
    Calculate financial health score.

    Formula

    Savings = Income - Expense

    Savings %

    = Savings / Income

    Score

    >=40%  → 10

    >=30%  → 8

    >=20%  → 6

    >=10%  → 4

    else → 2
    """
    # prevent divison by zero
    if income == 0:
        return 0
    
    # calculate savings
    savings = income - expense

    # calculate savings ratio
    ratio = savings / income

    # assign score
    if ratio >= 0.40:
        return 10
    
    elif ratio >= 0.30:
        return 8
    
    elif ratio >= 0.20:
        return 6
    
    elif ratio >= 0.10:
        return 4
    
    else:
        return 2
    
# validate uploaded file

def validate_file(filname):
    """
    Check wheather uploaded file
    is CSV or Execl.
    
    Returns
    
    True
    
    False
    """

    # convert filname to lowercase
    filname = filname.lower()

    # check extension
    if filname.endswith(".csv"):
        return True
    
    if filname.endswith(".xlsx"):
        return True
    
    return False

# current date & time

def current_datetime():
    """
    Return current system date and time.
    
    Example
    
    15 Jul 2026 10:45 AM
    """

    return datetime.now().strftime("%d %b %Y %I:%M %p")