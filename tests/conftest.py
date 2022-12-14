"""Testing fixtures."""


def pytest_make_parametrize_id(config, val, argname=None):
    """Stringify the id of parameterized tests."""
    return str(val)
