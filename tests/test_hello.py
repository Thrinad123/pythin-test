from hello import say_hello

def test_say_hello():
    assert say_hello("Alice") == "Hello, Alice!"
    assert say_hello("Bob") == "Hello, Bob!"
