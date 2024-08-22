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
    assert convert("9 AM TO 5 PM") == "09:00 to 17:00"
    assert convert("9 am to 4 pm") == "09:00 to 16:00"
    assert convert("12 am to 12 pm") == "00:00 to 12:00"
    assert convert("11:23 am to 4:32 pm") == "01:23 to 16:32"

def test_

