import duckdb
import pandas as pd


def filter_after_cutoff_age(people: pd.DataFrame, cutoff_age: int) -> pd.DataFrame:
    """Filter a data frame of people to only include people older than a cutoff age."""
    con = duckdb.connect(database=":memory:")
    con.register("people", people)
    return duckdb.sql(
        f"""
        SELECT
            *
        FROM people
        where Age >= {cutoff_age}
        """,
    ).df()

def avg_per_state(people: pd.DataFrame) -> pd.DataFrame:
    """Compute the average age per state."""
    result = people.groupby("State")["Age"].mean().reset_index().rename(columns={"Age": "avg(Age)"})
    return result.reset_index(drop=True)

# def large_states_adult_age(people: pd.DataFrame, cutoff_population:int) -> pd.DataFrame:
#     """Compute the average age of state's population over 5000000."""
#     cutoff_age =18
#     state = pd.read_csv("data/state_populations.csv")
#     data = state.merge(people,on="State")
#     large_states = data[data["Population"] > cutoff_population]
#     adult = large_states[large_states["Age"]>=cutoff_age]
#     result = adult.groupby("State")["Age"].mean().reset_index().rename(columns={"Age": "avg(Age)"})
#     return result.reset_index(drop=True)


