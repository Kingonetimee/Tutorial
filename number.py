def prime(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

number = int(input("Which number do you want to check: "))

prime(number)