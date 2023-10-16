word = input("Enter a word: ")

vowel_count = 0

for char in word:
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1

print(f"The word '{word}' contains {vowel_count} vowels.")

#Perfect Numbers
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

def get_divisors(n):
    divisors = [1]
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

for num in range(start, end + 1):
    divisors = get_divisors(num)
    if num == sum(divisors):
        print(num)

#Multiplication Table
n = int(input("Enter the number for the multiplication table: "))
limit = int(input("Enter the limit for the multiplication table: "))

for i in range(1, limit + 1):
    result = n * i
    print(f"{n} x {i} = {result}")
