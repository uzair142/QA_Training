number = 1

while True:
    square = number ** 2
    print(f"{number} squared is {square}")
    if square > 2000:
        break
    number += 1
