import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--rhvurl", action="store", default="", help="rhv instance api url"
    )


@pytest.fixture(scope="module")
def rhvurl(request):
    return request.config.getoption("--rhvurl")
