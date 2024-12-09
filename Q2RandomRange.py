
from random import randint

a= randint(0, 100)
b=randint(1, 100)

for _ in range(10):
    c = int(input(f"Enter your answer for {a} + {b}: "))
    if c == a + b:
        print("Correct!")
        break
else:
    print("Correct Solutions!")

