def test_example(sample_fixture):
    assert sample_fixture["key"] == "value"


# project/tests/test_example.py
def test_using_fixtures(global_fixture):
    assert global_fixture == "global"
    # assert test_fixture == "test"