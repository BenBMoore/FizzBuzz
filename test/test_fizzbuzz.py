import pytest

import fizzbuzz


def test_fizzbuzz_factor_3():
    x = 33
    result = fizzbuzz.fizzbuzz(x)
    assert result == "Fizz"


def test_fizzbuzz_factor_5():
    x = 20
    result = fizzbuzz.fizzbuzz(x)
    assert result == "Buzz"


def test_fizzbuzz_factor_5_3():
    x = 30
    result = fizzbuzz.fizzbuzz(x)
    assert result == "FizzBuzz!"


def test_fizzbuzz_not_a_number():
    x = "ABC"
    with pytest.raises(ValueError):
        assert fizzbuzz.fizzbuzz(x)


def test_fizzbuzz_not_a_positive_number():
    x = -3
    with pytest.raises(AssertionError):
        assert fizzbuzz.fizzbuzz(x)
