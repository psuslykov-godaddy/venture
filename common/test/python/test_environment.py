from environment import Environment


def test_all_environments_are_present():
    expected = ['dev', 'dev-private', 'test', 'stage']
    actual = [item.value for item in Environment]
    for env in expected:
        assert env in actual


def test_dev_private_environment():
    expected = Environment.DEV_PRIVATE
    actual = Environment('dev-private')
    assert actual == expected


def test_prod_environment():
    expected = Environment.PROD
    actual = Environment('prod')
    assert actual == expected
