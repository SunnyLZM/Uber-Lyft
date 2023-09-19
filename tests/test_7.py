from fl23 import hw1


def test_generate_people():
    n = 10
    people = hw1.generate_people(n)
    assert people.columns.tolist() == ["First_Name", "Last_Name", "Age", "State", "Text"]
