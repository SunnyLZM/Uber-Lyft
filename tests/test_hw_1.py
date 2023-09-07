import pandas as pd
from fl23 import hw1


def test_get_adults():
    people = pd.DataFrame({"Age": [17, 18]})
    assert hw1.get_adults(people) == pd.DataFrame({"Age": [18]})


def test_avg_per_state():
    people = pd.DataFrame({"State": ["MO", "MO", "IL"], "Age": [17, 18, 19]})
    assert hw1.avg_per_state(people) == {"MO": 17.5, "IL": 19}
