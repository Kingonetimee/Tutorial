print("welcome to love calculator!!!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

nam1 = name1.lower()
nam2 = name2.lower()

name = nam1 + nam2

true1 = name.count("t")
true2 = name.count("r")
true3 = name.count("u")
true4 = name.count("e")
love1 = name.count("l")
love2 = name.count("o")
love3 = name.count("v")
love4 = name.count("e")

true = true1 + true2 + true3 + true4
love = love1 + love2 + love3 + love4

score1 = str(true)
score2 = str(love)

calc = score1 + score2
final_calc = int(calc)

if final_calc < 10 or final_calc > 90:
    print(f"Your score is {final_calc}, you go together like coke and mentors")
elif final_calc > 40 and final_calc < 50:
    print(f"Your score is {final_calc}, you are alright together")
else:
     print(f"Your score is {final_calc}")