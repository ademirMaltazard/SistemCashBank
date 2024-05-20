# -------------- DEFINIR LIVRO -------------------
class Book:
    def __init__(self, title, author, year, status:str = 'Disponivel'):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__status = status

    def getTitle(self):
        return self.__title
    
    def getAuthor(self):
        return self.__author
    
    def getYear(self):
        return self.__year
    
    def getStatus(self):
        return self.__status
    
    def setDisponible(self):
        self.__status = 'Disponivel'
    
    def setIndisponible(self):
        self.__status = 'Indisponivel'


#-------------------------- DEFINIR BIBLIOTECA -------------------------------------

class Library:
    def __init__(self):
        self.__books=[]

    def AddBooks(self, objectBook: Book):
        self.__books.append(objectBook)
        return 'O livro foi adicionado.'
    
    def listBooks(self):
        for book in self.__books:
            print(f'Titulo: {book.getTitle()} | ano: {book.getYear()} | autor: {book.getAuthor()} | Disponibiidade: {book.getStatus()}')

    def LendBook(self, bookTitle):
        for book in self.__books:
            if book.getTitle() == bookTitle:
                book.setIndisponible()

    def ReturnBook(self, bookTitle):
        for book in self.__books:
            if book.getTitle() == bookTitle:
                book.setDisponible()







# ------------------------ AREA DE TESTES -------------------------

livro1 = Book('Eu era', 'ademir', '2018')
livro2 = Book('Eu fui', 'maltazard', '2018', 'Indisponível')
livro3 = Book('Eu sou', 'zard', '2018')

biblioteca = Library()
biblioteca.AddBooks(livro1)
biblioteca.AddBooks(livro2)
biblioteca.AddBooks(livro3)

biblioteca.listBooks()
biblioteca.LendBook('Eu era')
print('--------- emprestar ------------')
biblioteca.listBooks()
biblioteca.ReturnBook('Eu fui')
print('--------- devolver ------------')
biblioteca.listBooks()
