class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
new_book =Book('Red Queen', 'Victoria Aveyard', 2015)
third_book = Book('The Hunger Games', 'Suzanne Collins', 2008)
fourth_book = Book('The Maze Runner', 'James Dashner', 2009)
class Student:
    def __init__(self, name, age, city, country, is_student, hobbies):
        self.name = name 
        self.age = age
        self.city = city
        self.country = country
        self.is_student = is_student
        self.hobbies = hobbies
first_student = Student(" Sondos", 20, "Gaza", "Palestine", True, ["Reading"])
print(f'The first students name is :{first_student.name}')

class Profile:
    def __init__(self, name, email, language):
        self.name = name
        self.email = email
        self.language = language
first_profile=Profile('Sondos', 'soondos2@gmail.com', 'Arabic')
print(f'The  Firstprofile  is :{first_profile.name}')
print(f'The  email of first profile  is :{first_profile.email}')
print(f'The  language of first profile  is :{first_profile.language}')

second_profile=Profile('Ahmed', 'ahmed@gmail.com', 'English')
print(f'The  Secondprofile  is :{second_profile.name}')
print(f'The email of second profile  is :{second_profile}')
print(f'The language of second profile is :{second_profile.language}')

third_profile=Profile('Ansam', 'anoosa@gmail.com', 'turkish')
print(f'The third profile is :{third_profile.name}')
print(f'The email of third profile is :{third_profile.email}')
print(f'The language of third profile is :{third_profile.language}')

first_profile=Profile('Sondos', 'soondos2@gmail.com', 'Arabic')
print(f'The  Firstprofile  is :\n {first_profile.name}')
print(first_profile.email)
print(first_profile.language)

second_profile=Profile('Ahmed', 'ahmed@gmail.com', 'English')
print(f'The  Secondprofile  is :\n{second_profile.name}')
print(second_profile.email)
print(second_profile.language)

third_profile=Profile('Ansam', 'anoosa@gmail.com', 'turkish')
print(f'The third profile is :\n{third_profile.name} \n{third_profile.email}\n {third_profile.language}')