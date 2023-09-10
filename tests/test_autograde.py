import duckdb
import pandas as pd

from fl23 import hw1


def test_1_uses_sql(mocker):
    sql_spy = mocker.spy(duckdb, "sql")
    pandas_spy = mocker.spy(pd.DataFrame, "query")

    hw1.filter_after_cutoff_age(pd.DataFrame({"Age": [17, 18]}), 18)

    assert sql_spy.call_count == 1
    assert pandas_spy.call_count == 0


def test_2_uses_pandas(mocker):
    sql_spy = mocker.spy(duckdb, "sql")
    pandas_spy = mocker.spy(pd.DataFrame, "query")

    people = pd.DataFrame({"State": ["MO", "MO", "IL"], "Age": [17, 18, 19]})

    hw1.avg_per_state(people)

    assert sql_spy.call_count == 0
    assert pandas_spy.call_count == 1
