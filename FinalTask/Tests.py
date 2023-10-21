from PasswordChecker import PasswordStrengthChecker

def test_common_password():
    checker = PasswordStrengthChecker()
    assert checker.check_strength("password") == "very weak"

def test_very_weak_password():
    checker = PasswordStrengthChecker()
    assert checker.check_strength("abc123") == "weak"

def test_weak_password():
    checker = PasswordStrengthChecker()
    assert checker.check_strength("Abcdef") == "weak"

def test_moderate_password():
    checker = PasswordStrengthChecker()
    assert checker.check_strength("Abc123") == "moderate"

def test_strong_password():
    checker = PasswordStrengthChecker()
    assert checker.check_strength("Abc123@") == "strong"

def test_very_strong_password():
    checker = PasswordStrengthChecker()
    assert checker.check_strength("Abc@123defGHI") == "very strong"

if __name__ == "__main__":
    import pytest
    pytest.main()
