import pytest

from develop import functoins

@pytest.mark.parametrize('a, b', [("2019-08-26T10:50:58.294041", "26.08.2019"), ("2019-03-23T01:09:46.296404", "23.03.2019")])
def test_transformation_date_good(a, b):
    assert functoins.transformation_date(a) == b



