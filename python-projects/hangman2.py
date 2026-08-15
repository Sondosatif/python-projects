HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
print("Start the game ")
import random 

word=['call','office','dad','tomato','lemon']
random_word=random.choice(word)

display=['_']*len(random_word)

print(''.join(display) ) 
print(HANGMANPICS[0])
guessed_letters=[]
trys=6


while '_'in display and trys >0:
   guessed=input('guess a letter?').lower()

   if guessed in guessed_letters:
      print('you already guess that. Try again')
      print(f'you have {trys} more tries')
      print(''.join(display))
      continue
   guessed_letters.append(guessed)

   if guessed in random_word:
      for position in range(len(random_word)):
          if random_word[position]==guessed:
            display[position]=guessed
           

   else:
        trys-=1
        print(f'You lost a try ,Tries left {trys} ')
        print(HANGMANPICS[6-trys])
   print(''.join(display))
           



if  trys==0:
   print(f"You lose, The word was {random_word}")
else:
    print('congratulation , you win')

