import pytest
from develop import functoins

@pytest.mark.parametrize('a, b', [("Счет 38611439522855669794", "Счет 3861 1439 52** **** 9794"),
                                  ("Visa Platinum 1813166339376336", "Visa Platinum 1813 16** **** 6336")])
def test_mask_card_good(a, b):
    assert functoins.mask_card(a) == b



