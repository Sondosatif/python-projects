import random 
print("""Welcome to the coin guessing game.
      choose a method to toss the coin .
      1-using random.random()
      2-using random.randint(0,1)
      """)
user = int(input("please enter your choice 1 or 2 : "))
if user == 1 :
    random1=random.random()
    if random1 >= 0.5:
        computer_guess= "heads"
    else:
        computer_guess= "tails"
elif user == 2 :
    random2=random.randint(0,1)
    if random2 == 1 :
        computer_guess = "heads"
    else:
        computer_guess = "tails"
else:
    print("Your choice is not available.")
user_guess=input('Enter your guess. heads or tails:').lower()
if user_guess==computer_guess:
    print("Excellent. you win")
else:
    print("Sorry, you lost")
print(f'The computer guess is:{computer_guess}')