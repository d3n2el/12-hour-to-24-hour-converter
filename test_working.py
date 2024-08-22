import pytest
from working import convert
def test_valueError():
    assert convert("9am to 5pm") == ValueError
    assert convert("9 am 5 pm") == ValueError
    assert convert("9 am - 5 pm") == ValueError
    assert convert("9:60 AM to 5:60 PM") == ValueError
    assert convert("09:00 AM - 17:00 PM") == ValueError

