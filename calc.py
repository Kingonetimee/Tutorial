
def add(n1, n2):
 """"This adds any number given to it"""
 return n1 + n2

def subtract(n1, n2):
 """"This subtracts any number given to it"""
 return n1 - n2

def multiply(n1, n2):
 """"This multiplys any number given to it"""
 return n1 * n2

def divide(n1, n2):
 """"This divides any number given to it"""
 return n1 / n2


operation = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide ,
}

def calculate():
    num_1 = int(input("What is the first number: "))

    for keys in operation:
      print(keys)
    
   

    should_continue = True

    while should_continue:
      operation_symbol = input("Pick an operation from above: ")
      num_2 = int(input("What is the next number: "))
      calc = operation[operation_symbol]  
      final_result = calc(num_1, num_2)

      print(f"{num_1} {operation_symbol} {num_2} = {final_result}")

      if input(f"Type 'y' to continue calculating with the {final_result}, or type 'n' to start a new calculation: ") == "y":
           for keys in operation:
             print(keys)
           num_1 = final_result
      else:
        should_continue = False
        # calculate()
       

calculate()    
    


