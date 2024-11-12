import pytest

print("Loading global_fixture...")

@pytest.fixture
def global_fixture():
    print("global_fixture called")
    return "global"