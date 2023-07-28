import pytest
from lib.password_checker import *

def test_password_checker_correct_length():
    example = PasswordChecker()
    result = example.check("12345678")
    assert result == True


def test_password_checker_error():
    example = PasswordChecker()
    with pytest.raises(Exception) as e:
        example.check("1234")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."
    
