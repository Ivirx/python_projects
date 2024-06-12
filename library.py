class Library:
    def __init__(self):
        self.noOfBooks = 0
        self.store = []

    def addBook(self, bookName, author):
        self.store.append({
            'bookName': bookName,
            'author': author
        })
        self.noOfBooks = len(self.store)
        return 'Book Added'

    def removeBook(self, bookName):
        bookFound = False
        allBooks = []

        for book in self.store:
            if (book['bookName']).lower() == bookName.lower():
                bookFound = True
            else:
                allBooks.append(book)

        if bookFound:
            self.store = allBooks
            self.noOfBooks = len(self.store)
            return 'Book Removed'
        return '404, book_not_found'

    def searchBooks(self, bookName):
        booksFound = []
        for book in self.store:
            if (book['bookName']).lower() == bookName.lower():
                booksFound.append(book)

        if not len(booksFound):
            return {'bookName': bookName, 'author': '404, book_not_found'}
        return booksFound[0]

    def showAllBooks(self):
        if len(self.store):
            for book in self.store:
                print(book['bookName'], ' : ', book['author'])
        else:
            print('\t!! No Books to Show !!\n')


lib = Library()
lib.addBook('Wabi Sabi', 'Nobuo Suzuki')
lib.addBook('Ikigai', 'Hector Gracia')
lib.addBook('Subtle Fucks', 'Mark Manson')
lib.addBook('Everythink is Fucked', 'Mark Manson')

print('\t--- Welcome to The Library ---\n')
while True:
    choice = input('0->ShowAllBooks, 1->Add, 2->Remove, 3->Search, 4->NumberOfBooks, q->Quit\n')

    match choice:
        case '0':
            print('\nAll Books :', lib.noOfBooks)
            lib.showAllBooks()
            print()

        case '1':
            print('\nAdd book :')
            bookName = input('Book Name : ')
            author = input('Book Author : ')
            if len(bookName) and len(author):
                print(lib.addBook(bookName, author), end='\n\n')
            else:
                print('   !! Required fields must be present !!', end='\n\n')

        case '2':
            print('\nRemove book :')
            bookName = input('Book Name : ')
            if len(bookName):
                print(lib.removeBook(bookName), end='\n\n')
            else:
                print('   !! Required fields must be present !!', end='\n\n')

        case '3':
            print('\nSearch book :')
            bookName = input('Book Name : ')
            if len(bookName):
                bookFound = lib.searchBooks(bookName)
                print(f"\n{bookFound['bookName']} : {bookFound['author']}", end='\n\n')
            else:
                print('   !! Required fields must be present !!', end='\n\n')

        case '4':
            print(f'\nNo of books : {lib.noOfBooks}', end='\n\n')

        case 'q':
            print('\n\t--- Thank You ---\t\n')
            break

        case _:
            print('Oops! Wrong Input Entered!', end='\n\n')
