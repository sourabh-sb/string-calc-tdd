from add import add
def test_empty_string():
    assert add("") == 0
def test_one_number():
    assert add("1") == 1
def test_two_numbers():
    assert add("1,5") == 6
