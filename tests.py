from add import add

def test_empty_string():
    assert add("") == 0

def test_one_number():
    assert add("1") == 1

def test_two_numbers():
    assert add("1,5") == 6

def test_add_multiple_numbers():
    assert add("1,2,3,4") == 10

def test_add_new_lines_between_numbers():
    assert add("1\n2,3") == 6

def test_add_with_different_delimiters():
    assert add("//;\n1;2") == 3

def test_add_negative_numbers():
    try:
        add("-1,-2,3,-4")
    except ValueError as e:
        assert str(e) == "negative numbers not allowed: -1,-2,-4"
