import pytest

class TestClass():

    def test_func(self):
        x=2
        return x+1

    def test_two(self):
        x="ania"
        assert 'i' in x

    def test_answer(self):
        assert 2==2