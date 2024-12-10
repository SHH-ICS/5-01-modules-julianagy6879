```python
import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
print("What is", num1, "+", num2, "?")
user_answer = int(input("Your answer: "))
if user_answer == num1 + num2:
    print("Correct!")
else:
    print("Incorrect. The answer is", num1 + num2)
```
