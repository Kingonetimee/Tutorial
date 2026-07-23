fizz_total = 0
buzz_total = 0
fizzBuzz_total = 0
num_total = 0

fizz_num = []
buzz_num = []
fizzBuzz_num = []


for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        fizzBuzz_num.append(number)
        fizzBuzz_total += 1
        print("FizzBuzz") 
    elif number % 3 == 0:
        fizz_num.append(number)
        fizz_total += 1
        print("Fizz")   
    elif number % 5 == 0:
        buzz_num.append(number)
        buzz_total += 1
        print("Buzz")
    else:
        num_total += 1
        print(number)

print(f"Fizz Total Number is {fizz_total} and the numbers are {fizz_num}")
print(f"Buzz Total Number is {buzz_total} and the numbers are {buzz_num}")
print(f"FizzBuzz Total Number is {fizzBuzz_total} and the numbers are {fizzBuzz_num}")
print(f"Total Number is {num_total}")
