"""
PasswordChecker Module

This module defines a class for checking the strength of passwords.
"""

import re

class PasswordStrengthChecker:
    """
    This class checks the strength of a password.
    """

    COMMON_PASSWORDS = [
        "password", "123456", "qwerty", 
        "admin", "letmein", "welcome", 
        "monkey", "123456789", "1234567890"]

    def __init__(self):
        self.password_history = {}

    @staticmethod
    def check_strength(password):
        """
        Check the strength of a given password and return a rating.
        """
        if password in PasswordStrengthChecker.COMMON_PASSWORDS:
            return "very weak"

        length_score = len(password) >= 8
        upper_score = bool(re.search(r'[A-Z]', password))
        lower_score = bool(re.search(r'[a-z]', password))
        digit_score = bool(re.search(r'[0-9]', password))
        special_char_score = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

        strength_factors = [length_score, upper_score, lower_score, digit_score, special_char_score]

        if all(strength_factors):
            return "very strong"
        if strength_factors.count(True) == 4:
            return "strong"
        if strength_factors.count(True) == 3:
            return "moderate"
        if strength_factors.count(True) <= 2:
            return "weak"

        return "very weak"

def main():
    """
    Main function to run the password strength checker.
    """
    checker = PasswordStrengthChecker()

    while True:
        user_password = input("Enter a password (or 'quit' to exit): ")
        if user_password.lower() == "quit":
            break

        strength = checker.check_strength(user_password)
        print(f"Password strength: {strength}")

        checker.password_history[user_password] = strength

    print("\nPassword History:")
    for password, strength in checker.password_history.items():
        print(f"Password: {password}, Strength: {strength}")

if __name__ == "__main__":
    main()
