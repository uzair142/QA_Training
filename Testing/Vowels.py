def vowels(word):
    number_of_vowels = 0
    the_vowels = ["a", "e", "i", "o", "u"]
    for letter in word.lower():
        if letter in the_vowels:
            number_of_vowels += 1
    return number_of_vowels

def test_vowels_in_word():
    word = "hello"
    assert vowels(word) == 2

def test_no_vowels_in_word():
    word = "rhythm"
    assert vowels(word) == 0
