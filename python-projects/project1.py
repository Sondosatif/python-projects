print("Welcome in the treasure island")
doors=input("There are two doors, a red one and a blue one; choose one of them.")
if doors=='blue':
   print('You’ve just stepped into a lake full of crocodiles.')
elif doors=='red':
     room=input('You have entered a room containing three boxes:\n white, black, and green.\n Choose one of the boxes.')
     if room=='white':
        print(' There are snakes in the box.')
     elif room=='black':
        print(' There are spiders in the box.')
     elif room=='green':
        print('The treasure is in the box.\n Congratulations—you’ve won!')
     else: 
        print('invalid choice')
else:
   print('invalid choice')   