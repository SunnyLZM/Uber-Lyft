import duckdb
import pandas as pd
import pytest

from fl23 import hw1


def test_filter_after_cutoff_age():
    cutoff_age = 18
    people = pd.DataFrame({"Age": [17, 18]})
    adults = hw1.filter_after_cutoff_age(people)
    assert all(adults["Age"] >= cutoff_age)


@pytest.mark.xfail()
def test_1_uses_sql(mocker):
    sql_spy = mocker.spy(duckdb, "sql")

    hw1.filter_after_cutoff_age(pd.DataFrame({"Age": [17, 18]}), 18)

    assert sql_spy.call_count == 1