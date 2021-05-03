class Book():

    def __init__(self, uniqueID, bookTitle):
        if 0 < uniqueID < 1000:
            self.UID = uniqueID
        else:
            print("ERROR: uniqueID must be between 1 and 999")
            newUID = int(input("please enter a new uniqueID: "))
            if 0 < newUID < 1000:
                self.UID = newUID
        self.title = bookTitle.capitalize()

    def print(self):
        print("UID:",self.UID,"Title:", self.title)

books = []
books.append(Book(12,"the impossible book"))
books.append(Book(13,"anything's possible"))
print("here")
print(books[0].title)
for book in books:
    book.print()