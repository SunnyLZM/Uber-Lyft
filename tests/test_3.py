# import pandas as pd

# from fl23 import hw1


# def test_large_states_adult_age():
#     people = pd.DataFrame({"State": ["Missouri","Missouri", "Missouri","Montana"], "Age": [17,18, 19, 19]})
#     pd.testing.assert_frame_equal(
#         hw1.large_states_adult_age(people),
#         pd.DataFrame({"State": ["Missouri"], "avg(Age)":[18.5]}),
#     )
