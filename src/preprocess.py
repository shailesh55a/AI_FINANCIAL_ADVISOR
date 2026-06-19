# import pandas for data manipulation
import pandas as pd

# preprocess data

def preprocess_data(df):
    """
    Clean the uploaded financial dataset.
    
    Parameters
    ----------
    df : pandas.DataFrame
    
    Returns
    -------
    pandas.DataFrame
    """

    # make copy of the dataframe
    df = df.copy()

    # remove rows where all columns are empty.
    df.dropna(how="all", inplace=True)

    # remove duplicates

    df.drop_duplicates(inplace=True)

    # remove extra spaces from column names.

    df.columns = df.columns.str.strip().str.lower()

    # remove extra spaces inside text columns.

    text_columns = [
        "category",
        "type"
    ]

    for column in text_columns:

        if column in df.columns:

            df[column] = (
                df[column]
                .astype(str)
                .str.strip()
                .str.lower()
            )

    # convert amount column into numeric values.

    df["amount"] = pd.to_numeric(
        df["amount"],
        errors="coerce"
    )

    # remove rows where amount is missing
    df.dropna(subset=["amount"], inplace=True)

    # remove rows where amount is zero or negative
    df = df[df["amount"] > 0]

    # convert date column into datetime formae=te

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    # rows with invalid dates.
    df.dropna(subset=["date"], inplace=True)

    # sort data by date.

    df.sort_values(
        by="date",
        inplace=True
    )

    df.reset_index(
        drop=True,
        inplace=True
    )

    # return cleaned dataframe

    return df