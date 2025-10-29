import pytest
from src.string_calculater import string_calculater

@pytest.mark.parametrize('n,expected_result', [('',0), ('0',0),('1',1)])
def test_n_returns_expected_result(n, expected_result):
    actual_result = string_calculater(n)
    assert actual_result == expected_result