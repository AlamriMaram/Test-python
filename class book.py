#Q3. Create a Library class that contains a list of Book objects. Include methods to add a book, display all books, and search for a book by title.

class Library:
    
    def __init__(self):
        
        self.library= []
        
    def add_book(self, book_title , book_auther , book_copies ):
        
        book={"title":book_title ,"Auther":book_auther,"copies": book_copies}
        
        self.library.append(book)
        
    def display_books(self):
         for i in self.library:
             print(i)
        
    def search_book(self, title):
        
        for i in range self.library:
            if (i["Title"] == title):
                print(i)
                          
lb1= Library()
lb1.add_book("python" , "A" , 4 )
lb1.add_book("c++" , "B" , 8 )
lb1.display_books()
lb1.search_book("python")