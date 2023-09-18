import duckdb
import pandas as pd
import pytest

from fl23 import hw1


@pytest.mark.xfail()
def test_uses_sql(mocker):
    people = pd.DataFrame()
    sql_spy = mocker.spy(duckdb, "sql")
    exec_spy = mocker.spy(duckdb, "execute")

    hw1.large_states_adult_age(people)

    assert sql_spy.called or exec_spy.called
