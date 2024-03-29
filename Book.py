import os
import re

class Book:
    def __init__(self, title, publisher, isbn_10, isbn_13, otherinfo, n_copies=1):
        # Initialize the Book object with the given parameters
        self.title = title
        self.publisher = publisher
        self.isbn_10 = isbn_10
        self.isbn_13 = isbn_13
        self.otherinfo = otherinfo
        self.n_copies = n_copies

    def info(self):
        # Display the information about the book
        print("Title:", self.title)
        print("Publisher:", self.publisher)
        print("ISBN-10:", self.isbn_10)
        print("ISBN-13:", self.isbn_13)
        print("Number of copies:", self.n_copies)
        print(self.otherinfo)
