import string 
def encrypt(message,shift):
    alphabet=string.ascii_lowercase

    encrypted_message=""

    for letter in message:
        if letter.lower() in alphabet:
            original_position=alphabet.index(letter.lower())
            new_position=(original_position+shift)%26
            encrypted_letter=alphabet[new_position]
            if letter.isupper():
                encrypted_letter=encrypted_letter.upper()
            encrypted_message+=encrypted_letter
        else:
            encrypted_message+=letter
    print(encrypted_message)        
user_message=input('please enter a message\n')   
user_shift=int(input('please enter a shift number')) 

encrypt(user_message,user_shift)




#فك التشفير
import string 
def deencrypt(message,shift):
    alphabet=string.ascii_lowercase

    deencrypted_message=""

    for letter in message:
        if letter.lower() in alphabet:
            original_position=alphabet.index(letter.lower())
            new_position=(original_position-shift)%26
            deencrypted_letter=alphabet[new_position]
            if letter.isupper():
                deencrypted_letter=deencrypted_letter.upper()
            deencrypted_message+=deencrypted_letter
        else:
            deencrypted_message+=letter
    print(deencrypted_message)        
user_message=input('please enter a message\n')   
user_shift=int(input('please enter a shift number')) 

deencrypt(user_message,user_shift)