import string 
sentance=input("Please type a sentance\n")

new_sentence=""

for x in sentance:
    if x not in string.punctuation:
       new_sentence+=x
       
print('Here is the same sentance without punctuation\n',new_sentence)