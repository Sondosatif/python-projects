import random
computer_choice=random.randint(1000,9999)
user_pin       =int(input("enter a number of a 4 digits:\n"))
user_pin_len   =len(str(user_pin))
if user_pin_len !=4 :
    print("Please enter 4 digits")
else :
    if user_pin == computer_choice:
        print("pin matched.")
    else:
        print(f"pin not matched. The computer choice is {computer_choice}")