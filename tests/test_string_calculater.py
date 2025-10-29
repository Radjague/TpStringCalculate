from src.string_calculater import string_calculater


def test_empty_string_return_0():
    assert string_calculater('') == 0

def test_0_return_0():
    assert string_calculater('0') == 0