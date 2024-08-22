import pytest
from working import convert
def test_valueError():
    with pytest.raises(ValueError):
        convert("9am to 5pm")
    with pytest.raises(ValueError):
        convert("9 am - 5 pm")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("09:60 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM - 17:00 PM")

def test_normal():
    assert convert("12 AM TO 12 PM") == "00:00 to 12:00"
    assert convert("10 AM TO 8 PM") == "10:00 to 20:00"
    assert convert("11:23 am TO 4:32 pm") == "11:23 to 16:32"

def test_pmam():
    assert convert("9 PM TO 5 AM") == "21:00 to 05:00"
    assert convert("12 PM TO 2 AM") == "12:00 to 02:00"
    assert convert("11:23 PM TO 3:34 AM") == "23:34 to 03:23"
    assert convert("4:09 PM TO 5:06 AM") == "16:06 to 05:09"





