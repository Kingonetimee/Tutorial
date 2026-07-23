alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def kesari(option, message_text, shift_amount): 
    text = ""
    while shift_amount > 20:
        shift_amount -= 10 
    print(shift_amount)

    for letter in message_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if option == "encode":
               new_position = position + shift_amount
            elif option == "decode":
               new_position = position - shift_amount
            new_letter = alphabet[new_position]
            text += new_letter
        else:
            text += letter
    if option == "encode":
        print(f"The encoded text is {text}")
    elif option == "decode":
        print(f"The decoded text is {text}")

    

should_continue = True

while should_continue:
    option = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    kesari(option, message, shift)

    go_on = input("Do you want to continue, Type 'Yes' or 'No':\n").lower() 
    if go_on == "no":
        should_continue = False
        print("Goodbye")




   

