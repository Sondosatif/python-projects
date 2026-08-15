name=input(
    "Enter the first and last name of your friends separated by a comma :\n").split(", ")

abbreviated_names=[]

for x in name:
    name_parts=x.split()
    print(name_parts)

    first_name=name_parts[0]
    last_name=name_parts[1]

    first_letter1=first_name[0]
    first_letter2=last_name[0]

    abbreviation=first_letter1+'.'+first_letter2+'.'

    abbreviated_names.append(abbreviation)
    
print("\n".join(abbreviated_names))