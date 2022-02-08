import pytest


def pytest_generate_tests(metafunc):
    if "fixture1" in metafunc.fixturenames:
        metafunc.parametrize("fixture1", ["1", "2", "3", "4", "5", "6", "7", "8"])
    if "fixture2" in metafunc.fixturenames:
        metafunc.parametrize("fixture2", ["9", "10", "11", "12"])


def test_foobar(fixture1, fixture2):
    assert type(fixture1) == type(fixture2)


@pytest.mark.parametrize("fil_1", ["1", "2", "3", "4", "5", "6", "7", "8"])
@pytest.mark.parametrize("fil_2", ["9", "10", "11", "12"])
def test_1(fil_1, fil_2):
    fil = [1, 2, 3, 4, 5, 6]
    print("len ", len(fil))
    assert fil_1 == fil_2, "HI THERE!!!"
