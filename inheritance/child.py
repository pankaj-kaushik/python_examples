class Book:
    def __init__(self, bookname):
        print "Book Class Object Created"
        self.name = bookname
    
    def read(self):
        print "Reading general book : ", self.name
        
class FictionBook(Book):
   
#case - 1 when init is redefined, you have to initialize 
#parent class member if not done explicitly otherwise it will generate attribute error
    def __init__(self, title, bookname):
        Book.__init__(self, bookname)
        self.title = title
        
    def get_name(self):
        return self.name

mybook = FictionBook("sachin", "The tribute")

#Note : if case-1 then it will generate attribute error 
mybook.read()
