f_name = input("What is your first name?: ")
l_name = input("What is your last name?: ")

def format_name(f_name, l_name):
   if f_name == "" or l_name == "":
      return "Invalid Inputs"
   fname = f_name.title() 
   lname = l_name.title() 
   print(f"Welcome {fname} {lname}") 


should_run = True
while should_run:
   can_continue = input("Do you want to continue, Type 'Yes' or 'No'") .lower()
   if can_continue == "no":
      should_run = False
   
      
# post = format_name(f_name, l_name)

# print(post)