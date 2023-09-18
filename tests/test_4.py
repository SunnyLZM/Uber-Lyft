from unittest.mock import ANY, MagicMock, call

import pandas as pd
import pytest

from fl23 import hw1


@pytest.mark.xfail()
def test_filter_after_join():
    people = MagicMock()
    mock_joined_df = MagicMock()

    mock_joined_df.__getitem__.return_value = pd.DataFrame({"State": [], "Age": []})
    people.join.return_value = mock_joined_df

    hw1.large_states_adult_age(people)

    people.assert_has_calls([call.join(ANY), call.join(ANY).__getitem__("Population")])
