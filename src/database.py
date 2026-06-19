import sqlite3


# Create Database Connection
def create_connection():
    """
    Create a connection to the SQLite database.
    """
    connection = sqlite3.connect("database/finance.db")
    return connection


# Create Table
def create_table():
    """
    Create financial_history table if it doesn't already exist.
    """
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS financial_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            analysis_date TEXT,
            total_income REAL,
            total_expense REAL,
            savings REAL,
            top_category TEXT,
            ai_advice TEXT
        )
    """)

    connection.commit()
    connection.close()


# Save Financial Analysis
def save_analysis(
    analysis_date,
    income,
    expense,
    savings,
    category,
    advice,
):
    """
    Insert one financial analysis into the database.
    """
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO financial_history (
            analysis_date,
            total_income,
            total_expense,
            savings,
            top_category,
            ai_advice
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        analysis_date,
        income,
        expense,
        savings,
        category,
        advice,
    ))

    connection.commit()
    connection.close()


# Get History
def get_history():
    """
    Retrieve all previous analyses.
    """
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM financial_history
        ORDER BY id DESC
    """)

    history = cursor.fetchall()

    connection.close()

    return history


# Delete One Record
def delete_record(record_id):
    """
    Delete one analysis using its ID.
    """
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM financial_history
        WHERE id = ?
    """, (record_id,))

    connection.commit()
    connection.close()


# Delete Entire History
def delete_all_history():
    """
    Remove every record.
    """
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM financial_history
    """)

    connection.commit()
    connection.close()