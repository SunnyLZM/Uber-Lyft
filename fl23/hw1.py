import duckdb
import pandas as pd
from faker import Faker


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

def large_states_adult_age(people: pd.DataFrame) -> pd.DataFrame:
    """Compute the average age of state's population over 5000000."""
    #Problem 4
    cutoff_age =18
    cutoff_population = 5000000
    state = pd.read_csv("data/state_populations.csv")
    data = state.merge(people,on="State")
    large_states = data[data["Population"] > cutoff_population]
    adult = large_states[large_states["Age"]>=cutoff_age]
    result = adult.groupby("State")["Age"].mean().reset_index().rename(columns={"Age": "avg(Age)"})
    return result.reset_index(drop=True)
    
    # #Problem 5
    # cutoff_age =18
    # cutoff_population = 5000000
    # state = pd.read_csv("data/state_populations.csv")
    # large_states = state[state["Population"] > cutoff_population]
    # adult = people[people["Age"]>=cutoff_age]
    # data = adult.merge(large_states, on="State")
    # result = data.groupby("State")["Age"].mean().reset_index().rename(columns={"Age": "avg(Age)"})
    # return result.reset_index(drop=True)

    # #Problem 6
    # state = pd.read_csv("data/state_populations.csv")
    # cutoff_population = 5000000
    # cutoff_age =18
    # con = duckdb.connect(database=":memory:")
    # con.register("people", people)
    # con.register("state", state)
    # return duckdb.sql(
    #     f"""
    #     SELECT
    #     people.State,
    #     avg(Age)
    #     FROM people
    #     Inner JOIN state on people.State = state.State
    #     WHERE Age >={cutoff_age} and Population > {cutoff_population}
    #     GROUP BY people.State
    #      """,
    #  ).df()

#Problem 8
def generate_people(n: int) -> pd.DataFrame:
    """Gnerate fake people table."""
    fake = Faker()
    data = {
        "first_name": [fake.first_name() for _ in range(n)],
        "last_name": [fake.last_name() for _ in range(n)],
        "Age": [fake.random_int(min=0, max=100) for _ in range(n)],
        "State": [fake.state() for _ in range(n)],
        "random_sentence": [fake.sentence() for _ in range(n)],
    }
    return pd.DataFrame(data)





