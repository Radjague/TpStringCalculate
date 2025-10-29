import pytest
from src.string_calculater import string_calculater

@pytest.mark.parametrize('n,expected_result', [('',0), ('0',0),('1',1),('2',2),('3',3),('0,0',0),('0,1',1),('1,0',1),('1,1',2),('1,2',3),('100',100),('1999',1999),('200,39',239),('2000,25',2025),('90,10',100),('40,5',45),('33,5',38),('67,3',70)])
def test_n_returns_expected_result(n, expected_result):
    actual_result = string_calculater(n)
    assert actual_result == expected_result