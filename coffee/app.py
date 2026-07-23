from menu import MENU, resources
want_coffee = True

water = resources['water']
coffee = resources['coffee']
milk = resources['milk']
profit = 0.0

menu = MENU

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

def calc(a, b):
   return a*b

def change(a, b):
   return a-b

def usercalc(a, b, c, d):
   return a+b+c+d

ewater = menu['espresso']["ingredients"]['water']
ecoffee = menu['espresso']["ingredients"]['coffee']
ecost = menu['espresso']['cost']

lwater = menu['latte']["ingredients"]['water']
lcoffee = menu['latte']["ingredients"]['coffee']
lmilk = menu['latte']["ingredients"]['milk']
lcost = menu['latte']["cost"]

cwater = menu['cappuccino']["ingredients"]['water']
ccoffee = menu['cappuccino']["ingredients"]['coffee']
cmilk = menu['cappuccino']["ingredients"]['milk']
ccost = menu['cappuccino']["cost"]

def pay():
   print("Please insert coins")

def resource():
   return f"Water:  {water}ml\nMilk:   {milk}ml\nCoffee: {coffee}g\nMoney:  ${profit}"

def money():
    qpay = int(input("How many quarters?: "))
    quser = calc(quarters, qpay)
    dpay = int(input("How many dimes?: "))
    duser = calc(quarters, dpay)
    npay = int(input("How many nickels?: "))
    nuser = calc(quarters, npay)
    ppay = int(input("How many pennies?: "))
    puser = calc(quarters, ppay)
    return usercalc(quser, nuser, puser, duser)
    
while want_coffee:
    want = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if want == "off":
     want_coffee = False
    elif want == "report":
       print(resource())
    elif want == "espresso":
       if water > ewater and coffee > ecoffee: 
          water = water - ewater
          coffee = coffee - ecoffee
          pay()
          user_money = money()
          print(f"Your money is ${user_money}")
          if ecost < user_money:
             user_change = change(user_money, ecost)
             print(f"You gave ${user_money},Here is ${user_change} in change\nHere is your Espresso ☕️ Enjoy! ")
             profit += ecost
          elif ecost > user_money:
              print(f"You gave ${user_money}, Sorry that's not enough money. Money refunded.")
       elif water < ewater:
          print("Sorry there is not enough water.")
       elif coffee < ecoffee:
          print("Sorry there is not enough coffee.")
    elif want == "latte":
       if water > lwater and coffee > lcoffee and milk > lmilk:
          water = water - lwater
          coffee = coffee - lcoffee
          milk = milk - lmilk
          pay()
          user_money = money()
          print(f"Your money is ${user_money}")
          if ecost < user_money:
             user_change = change(user_money, lcost)
             print(f"You gave ${user_money},Here is ${user_change} in change\nHere is your Latte ☕️ Enjoy! ")
             profit += lcost
          elif lcost > user_money:
              print(f"You gave ${user_money}, Sorry that's not enough money. Money refunded.")
       elif water < lwater:
          print("Sorry there is not enough water.")
       elif coffee < lcoffee:
          print("Sorry there is not enough coffee.")
       elif milk < lmilk:
          print("Sorry there is not enough milk")
    elif want == "cappuccino":
       if water > cwater and coffee > ccoffee and milk > cmilk:
          water = water - cwater
          coffee = coffee - ccoffee
          milk = milk - cmilk
          pay()
          user_money = money()
          print(f"Your money is ${user_money}")
          if ccost < user_money:
             user_change = change(user_money, ccost)
             print(f"You gave ${user_money},Here is ${user_change} in change\nHere is your Cappuccino ☕️ Enjoy! ")
             profit += ccost
          elif ccost > user_money:
              print(f"You gave ${user_money}, Sorry that's not enough money. Money refunded.")
       elif water < cwater:
          print("Sorry there is not enough water.")
       elif coffee < ccoffee:
          print("Sorry there is not enough coffee.")
       elif milk < cmilk:
          print("Sorry there is not enough milk")
    else:
       print("wrong input")