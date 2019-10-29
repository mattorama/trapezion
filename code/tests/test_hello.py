""" test hello """

from hello import fun


def test_hello_fun():
    """ doc """
    assert fun(3, 2) == 5
