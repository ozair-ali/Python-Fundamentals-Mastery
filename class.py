# creating a class named book with title, author and genre as attributes
class book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

# creating a method to display information about the book
    def display_information(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Genre:", self.genre)

# Creating an instance of the class
my_book = book("Harry Potter", "J.K.Rowling", "Fiction")

# Displaying information about my book using the display information method
my_book.display_information()