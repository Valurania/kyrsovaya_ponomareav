import pytest

from develop import functoins

@pytest.mark.parametrize('a, b', [("Счет 64686473678894779589", "Счет **9589"),
                                  ("Visa Platinum 8990922113665229", "Visa Platinum **5229")])
def test_mask_check_good(a, b):
    assert functoins.mask_check(a) == b



