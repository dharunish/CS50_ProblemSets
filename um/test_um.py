from um import count
import pytest


def test_start():
    assert count("um") == 1
    assert count("um hello")

def test_end():
    assert count("hi um") == 1

def test_only_ums():
    assert count("um um um") == 3
    assert count ("um...um...um") == 3
    assert count("Um, um um") == 3
def test_words():
    assert count("yummy albums um") == 1
    assert count("um yum um album dum um") == 3