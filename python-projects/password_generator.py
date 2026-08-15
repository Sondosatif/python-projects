import random
import string 

print("Welcome to the password Generator!")
total_number=int(input('Enter the total number of characters in the password:\n'))

password_letters=int(input('Enter the number of letters in the password\n'))
random_letters=random.choices(string.ascii_letters,k=password_letters)

password_numbers=int(input('Enter the number of numbers in the password\n'))
random_numbers=random.choices(string.digits,k=password_letters)

password_symbols=int(input('Enter the number of symbols in the password\n'))
random_symbols=random.choices(string.punctuation,k=password_symbols)

total=password_letters+password_symbols+password_numbers
total_random=random_letters+random_symbols+random_numbers
random.shuffle(total_random)

if total_number==total:
   print('the password is :'+''.join(total_random))
else:
   print("invalid input . The sum of letters, numbers, and symbols doesnt match the password ")