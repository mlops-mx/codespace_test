from hello import more_hello, more_goodbye


def test_more_hello():
    assert "hi" == more_hello()


def test_more_goodbye():
    assert "goodbye" == more_goodbye()
