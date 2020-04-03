import pytest


@pytest.fixture(scope="module")
def cobbler(cb_url: str, credential: tuple = ("cobbler", "cobbler")):
    from rhvhauto_common_utils.cobbler.cobbler import Cobbler
    return Cobbler(url=cb_url, credential=credential)


def test_cobbler_profiles(cobbler):
    profiles = cobbler.profiles
    assert profiles is list
