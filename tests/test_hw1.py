import pandas as pd

from fl23 import hw1


def test_filter_after_cutoff_age():
    cutoff_age = 18
    people = pd.DataFrame({"Age": [17, 18]})
    adults = hw1.filter_after_cutoff_age(people, cutoff_age)
    assert all(adults["Age"] >= cutoff_age)


def test_avg_per_state():
    people = pd.DataFrame({"State": ["MO", "MO", "IL"], "Age": [17, 18, 19]})
    pd.testing.assert_frame_equal(
        hw1.avg_per_state(people),
        pd.DataFrame({"State": ["IL", "MO"], "avg(Age)": [19, 17.5]}),
    )

def test_large_states_adult_age():
    people = pd.DataFrame({"State": ["Missouri", "Missouri", "Montana"], "Age": [17, 18, 19]})
    pd.testing.assert_frame_equal(
        hw1.large_states_adult_age(people),
        pd.DataFrame({"State": ["Missouri"], "avg(Age)":[17.5]}),
    )
