import pandas as pd


def load_file(uploaded_file):
    """
    Load and validate a CSV or Excel file.

    Parameters:
        uploaded_file: Uploaded file object

    Returns:
        pandas.DataFrame
    """

    # Check if a file was provided
    if uploaded_file is None:
        raise ValueError("No file uploaded.")

    # Get filename
    filename = uploaded_file.name.lower()

    # Read CSV
    if filename.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    # Read Excel
    elif filename.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    # Reject unsupported file types
    else:
        raise ValueError("Only CSV and Excel files are supported.")

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Standardize column names
    df.columns = [column.lower().strip() for column in df.columns]

    # Required columns
    required_columns = [
        "date",
        "category",
        "amount",
        "type"
    ]

    # Check for missing columns
    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}"
        )

    return df