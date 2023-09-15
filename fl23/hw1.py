import duckdb
import pandas as pd


def filter_after_cutoff_age(people: pd.DataFrame, cutoff_age: int) -> pd.DataFrame:
    """Filter a data frame of people to only include people older than a cutoff age."""
    return people[people["Age"] >= cutoff_age]


def avg_per_state(people: pd.DataFrame) -> pd.DataFrame:  # noqa: ARG001
    """Compute the average age per state."""
    return duckdb.sql(
        """
        SELECT
            State,
            AVG(Age),
        FROM people
        GROUP BY State
        """,
    ).df()


def generate_people(n: int) -> pd.DataFrame:
    """Generate a data frame of people with random ages, states, names, and text."""
    return pd.DataFrame()
