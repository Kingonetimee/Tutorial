import random

names_string = input("Give me everybody's name separated by comma: \n")
names = names_string.split(", ")
count = len(names) - 1
rand = random.randint(0, (count))
random_name = names[rand]
message = f"{random_name} is going to buy the meal today"
print(names)
print(message)
print(rand)