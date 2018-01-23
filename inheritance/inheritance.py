class Book:
    def __init__(self, bookname):
        print "Book Class Object Created"
        self.name = bookname
    
    def read(self):
        print "Reading general book"
        
class FictionBook(Book):
    def __init__(self, bookname):
        print "Fiction Book Class Object Created"
        self.name = bookname
    
    def read(self):
        print "Reading Fiction book", self.name
        

mybook = FictionBook("sachin")
mybook.read()
mybook.pages = 7
print mybook.pages