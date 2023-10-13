word = input("Enter a word: ")
vowel_count = 0

for char in word:
    if char in 'aeiouAEIOU':
        vowel_count += 1

print(f"The word '{word}' contains {vowel_count} vowels.")
