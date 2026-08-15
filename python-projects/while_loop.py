#correct_password="a1b2c3"
#entered_password=input("Enter password:")
#while entered_password!=correct_password:
     # print('uncorrect password,TRY again')
     # entered_password=input("Enter password:")
#print('Access Grante'0)
import random 
print("")
secret=random.randint(1,10)
guess_number=int(input('Gess a number between 1 and 10'))
while guess_number!=secret:
    if guess_number>secret:
      guess_number=int(input('Too high !,guess again'))
    else:
       guess_number=int(input('Too low,guess again'))

print('Congratulation! you guess the number')