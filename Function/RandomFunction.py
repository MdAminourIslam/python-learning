import random

# print(help(random))
low = 1
high = 6
number = random.randint(low, high)
number = random.random()
number = int(random.random() * high)

# print(number)

choices = ["A", "B", "C", "D"]
choice = random.choice(choices)
random.shuffle(choices)

print(choice)
print(choices)

