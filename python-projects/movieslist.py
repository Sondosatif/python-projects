print("____MOVIES LIST________")
class Movie:
    def __init__(self, title, director, release_year, genre):
        self.title = title
        self.director = director
        self.release_year = release_year
        self.genre = genre
    def display_movie(self):
        print(f"Title: {self.title}\nDirector: {self.director}\nRelease Year: {self.release_year}\nGenre: {self.genre}")
    def update_director(self, new_director):
        self.director = new_director
        print(f"Director: {self.director}")



movie1=Movie("Inception", "Christopher Nolan", 2010, "Sci-Fi")
movie1.display_movie()
movie2=Movie("The Godfather", "Francis Ford Coppola", 1972, "Crime")
movie2.display_movie()
movie3=Movie("Parasite", "Bong Joon-ho", 2019, "Thriller")
movie3.display_movie()
print("Changing Movie Directors .....")
movie1.display_movie()
movie1.update_director("Shokry Sarhan")
movie2.display_movie()
movie2.update_director("Ahmed Mazhar")
movie3.display_movie()
movie3.update_director("Isamel Yassin")