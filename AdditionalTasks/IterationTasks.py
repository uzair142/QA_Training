#Fibonacci Sequence
n = int(input("Enter the value of n: "))
a, b = 0, 1

while a <= n:
    print(a, end=" ")
    a, b = b, a + b

#Prime Numbers
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)
