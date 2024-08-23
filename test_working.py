import pytest
from working import convert
def test_valueError():
    with pytest.raises(ValueError):
        convert("9am to 5pm")
    with pytest.raises(ValueError):
        convert("9 am - 5 pm")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
def test_valueError2():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("09:60 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM - 17:00 PM")

def test_normal():
    assert convert("9 AM to 10 PM") == "09:00 to 22:00"
    assert convert("11 AM to 5 PM") == "11:00 to 17:00"
    assert convert("11:23 AM to 4:32 PM") == "11:23 to 16:32"







