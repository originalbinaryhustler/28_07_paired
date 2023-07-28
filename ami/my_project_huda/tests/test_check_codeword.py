from lib.check_codeword import * 

def test_password_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_password_close():
    result = check_codeword("hole")
    assert result == "Close, but nope."

def test_password_wrong():
    result = check_codeword("FLOWER")
    assert result == "WRONG!"
