import pandas as pd

from fl23 import hw1


def test_join_after_filter(mocker):
    people = pd.DataFrame({"State": [], "Age": []})
    filter_spy = mocker.spy(people, "__getitem__")

    hw1.large_states_adult_age(people)

    filter_spy.assert_not_called()
