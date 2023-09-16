import duckdb
import pandas as pd
import pytest

from fl23 import hw1


@pytest.mark.xfail()
def test_avg_per_state():
    people = pd.DataFrame({"State": ["MO", "MO", "IL"], "Age": [17, 18, 19]})
    pd.testing.assert_frame_equal(
        hw1.avg_per_state(people),
        pd.DataFrame({"State": ["IL", "MO"], "avg(Age)": [19, 17.5]}),
    )


def test_2_uses_pandas(mocker):
    sql_spy = mocker.spy(duckdb, "sql")

    people = pd.DataFrame({"State": ["MO", "MO", "IL"], "Age": [17, 18, 19]})

    hw1.avg_per_state(people)

    assert sql_spy.call_count == 0
