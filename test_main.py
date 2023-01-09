from main import *


def test_main():
    # Test to see if basic method is working
    result = entry_point()
    assert result


# def test_mocking_main(mocker):
#     mocked_func = mocker.patch('main.entry_point')
#
#     mocked_func()
#     mocked_func.assert_called_once()
