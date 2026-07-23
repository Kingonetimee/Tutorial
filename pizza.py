print("WELCOME TO PYTON PIZZA DELIVERY")
size = input("what size pizza do you want? S, M or L: ")
add_pepperonni = input("Do you want Pepperonni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill = 15
    if add_pepperonni == "Y":
        bill += 2
    if extra_cheese == "Y": 
        bill += 1
    print(f"Your final bill is ${bill}")
elif size == "M":
    bill = 20
    if add_pepperonni == "Y":
        bill += 3
    if extra_cheese == "Y": 
        bill += 1
    print(f"Your final bill is ${bill}")
elif size == "L":
    bill = 25
    if add_pepperonni == "Y":
        bill += 3
    if extra_cheese == "Y": 
        bill += 1
    print(f"Your final bill is ${bill}")