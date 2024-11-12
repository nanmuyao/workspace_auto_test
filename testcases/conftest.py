import pytest

@pytest.fixture
def sample_fixture():
    print("sample_fixture")
    return {"key": "value"}

# conftest.py
def pytest_runtest_setup(item):
    print("pytest_runtest_setup")
    print(f"Setting up for {item.name}")

# teardown
def pytest_runtest_teardown(item):
    print("pytest_runtest_teardown")
    print(f"Tearing down for {item.name}")
