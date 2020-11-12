""" Given the base class Book, define a derived class called Encyclopedia. Within the derived Encyclopedia class, define a print_info() method that overrides the Book class' print_info() method by printing not only the title, author, publisher, and publication date, but also the edition and number of volumes.

Ex: If the input is:

The Hobbit
J. R. R. Tolkien
George Allen & Unwin
21 September 1937
The Illustrated Encyclopedia of the Universe
James W. Guthrie
Watson-Guptill
2001
2nd
1
the output is:

Book Information: 
   Book Title: The Hobbit
   Author: J. R. R. Tolkien
   Publisher: George Allen & Unwin
   Publication Date: 21 September 1937
Book Information: 
   Book Title: The Illustrated Encyclopedia of the Universe
   Author: James W. Guthrie
   Publisher: Watson-Guptill
   Publication Date: 2001
   Edition: 2nd
   Number of Volumes: 1 """

class Book:
    def __init__(self, title, author, publisher, publication_date):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
   
    def print_info(self):
        print('Book Information:')
        print('   Book Title:', self.title)
        print('   Author:', self.author)
        print('   Publisher:', self.publisher)
        print('   Publication Date:', self.publication_date)


class Encyclopedia(Book):
    # TODO: Define constructor with attributes:
    #       title, author, publisher, publication_date, edition, num_volumes
    def __init__(self, title, author, publisher, publication_date, edition, num_volumes):
        Book.__init__(self, title, author, publisher, publication_date)
        self.edition = edition
        self.num_volumes = num_volumes
    # TODO: Define a print_info() method that overrides the print_info()
    #       in the Book class
    def print_info(self):
        self.print_info()
        print('Book Information:')
        print('   Book Title:', self.title)
        print('   Author:', self.author)
        print('   Publisher:', self.publisher)
        print('   Publication Date:', self.publication_date)
        print('   Edition:', self.edition)
        print('   Number of Volumes:', self.num_volumes)
        
if __name__ == "__main__":
    title = input()
    author = input()
    publisher = input()
    publication_date = input()
    
    e_title = input()
    e_author = input()
    e_publisher = input()
    e_publication_date = input()
    edition = input()
    num_volumes = int(input())
    
    my_book = Book(title, author, publisher, publication_date)
    my_book.print_info()
    
    my_encyclopedia = Encyclopedia(e_title, e_author, e_publisher, e_publication_date, edition, num_volumes)
    my_encyclopedia.print_info()
