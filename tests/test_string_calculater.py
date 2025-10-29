from src.string_calculater import string_calculater


def test_string_calculater_function_is_callable():
    string_calculater('')

def test_empty_string_return_0():
    assert string_calculater('') == 0