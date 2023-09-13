import duckdb
import pandas as pd


def filter_after_cutoff_age(people: pd.DataFrame, cutoff_age: int) -> pd.DataFrame:
    """Filter a data frame of people to only include people older than a cutoff age."""
    # Register the dataframe as a temporary table in duckdb
    conn = duckdb.connect()
    conn.register("people", people)

    return duckdb.sql(
        f"""
        SELECT
            *
        FROM people
        WHERE Age >= {cutoff_age}
        """,
    ).df()


def avg_per_state(people: pd.DataFrame) -> pd.DataFrame:
    """Compute the average age per state."""
    result = people.groupby("State").agg({"Age": "mean"}).reset_index()
    result = result.rename(columns={"Age": "avg(Age)"})

    return result.reset_index(drop=True)
