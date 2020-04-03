import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--rhvurl", action="store", default="", help="rhv instance api url"
    )
    parser.addoption(
        "--cb_url", action="store", default="", help="cobbler api url",
    )


@pytest.fixture(scope="module")
def rhvurl(request):
    return request.config.getoption("--rhvurl")


@pytest.fixture(scope="module")
def cb_url(request):
    return request.config.getoption("--cb_url")
