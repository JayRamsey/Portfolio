import tkinter as tk
WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_NAME = 600, 400, "Library Catalogue"

window = tk.Tk()
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.maxsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

window.title(WINDOW_NAME)
window.iconbitmap("library_icon.ico")

def RIC(string: str, extraChars: str = ""): #"Remove Illegal Characters"
    tempStr = ""
    illegalChars = "|\$" + extraChars
    for char in string:
        if char not in illegalChars:
            tempStr += char
    return tempStr

class Book:
    def __init__(self, title: str, author: str, genre: str):
        self.title = title
        self.author = author
        self.genre = genre

    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_genre(self): #get the genre of the book
        return self.genre

class Library:
    def __init__(self, books: dict = {}):
        self.books = books

    def remove_book(self):
        title = self.removalTitle
        del self.books[title]
        saveBookData(self.books, "savedBooks.txt")
        self.removeBookWindow.destroy()

    def call_remove_book(self):
        self.removalTitle = ""
        removeBookWindow = tk.Tk()
        removeBookWindow.title("Remove book")

        tk.Label(removeBookWindow, text="Book title").pack(padx=10, pady=2)
        removalTitleEntry = tk.Entry(removeBookWindow)

        def removalTitleEntryUpdate(event):
            self.removalTitle = removalTitleEntry.get()
            if self.removalTitle in self.books:
                self.removeButton.config(state="active")
            else:
                self.removeButton.config(state="disabled")

        removalTitleEntry.bind("<KeyRelease>", removalTitleEntryUpdate)
        removalTitleEntry.pack(padx=10, pady=10)

        self.removeButton = tk.Button(removeBookWindow, text="Remove", command=lambda: self.remove_book())
        self.removeButton.pack(side="left", expand=True, fill="x", padx=10, pady=10)
        tk.Button(removeBookWindow, text="cancel", command=removeBookWindow.destroy).pack(side="left", expand=True, fill="x", padx=10, pady=10)
    
        removalTitleEntryUpdate(None)
        self.removeBookWindow = removeBookWindow

    def call_add_book(self):
        addBookWindow = tk.Tk()
        addBookWindow.title("New book")

        tk.Label(addBookWindow, text="Book title").pack(padx=10, pady=2)
        self.titleEntry = tk.Entry(addBookWindow)
        self.titleEntry.pack(padx=10, pady=10)
        tk.Label(addBookWindow, text="Author").pack(padx=10, pady=2)
        self.authorEntry = tk.Entry(addBookWindow)
        self.authorEntry.pack(padx=10, pady=10)
        tk.Label(addBookWindow, text="Book genre").pack(padx=10, pady=2)        
        self.genreEntry = tk.Entry(addBookWindow)
        self.genreEntry.pack(padx=10, pady=10)

        tk.Button(addBookWindow, text="Add book", command = self.validateAdding).pack(side="left", expand=True, fill="x", padx=5, pady=5)
        tk.Button(addBookWindow, text="cancel", command=addBookWindow.destroy).pack(side="left", expand=True, fill="x", padx=5, pady=5)

        self.addBookWindow = addBookWindow

    def validateAdding(self):
        self.add_book(Book(RIC(self.titleEntry.get()), RIC(self.authorEntry.get()), RIC(self.genreEntry.get())))
        self.addBookWindow.destroy()

    def add_book(self, book: Book):
        self.books[book.title] = book
        saveBookData(self.books, "savedBooks.txt")
 
    def search_book(self, searchedText: str):
        addedTitles = {}
        result = ""
        searchedString = RIC(searchedText.lower(), '"!£%^&*();.<>@:-=_+')

        for title in self.books:
            objString = RIC((f"{self.books[title].title}, {self.books[title].author} {self.books[title].genre}").lower(), '"!£%^&*();.<>@:-=_+')
            if len(objString) - len(searchedString) > 0:
                for i in range(len(objString) - len(searchedString) + 1):
                        if objString[i:i+len(searchedString)] == searchedString:
                            if title in addedTitles:
                                addedTitles[title] += i
                            else:
                                addedTitles[title] = i
        sortedBooks = dict(sorted(addedTitles.items(), key=lambda x: x[1], reverse=True))
        for key in sortedBooks:
            result += formatBookDisplay(self.books[key]) + "\n"
        if result == "":
            result = "No books found."
        return result
    
    def display_catalogue(self):
        dispWindow = tk.Tk()
        dispWindow.title("Entire Catalogue")
        bookDisplay = tk.Text(dispWindow, relief=tk.GROOVE, wrap="word", state="normal", font="trebuchetms 10", bg="lightyellow")
        if len(self.books) > 0:
            for key in self.books:
                book = self.books[key]
                bookDisplay.insert("end", formatBookDisplay(book) + "\n")
        else:
            bookDisplay.insert("end", "There are no books in the catalogue.")
        bookDisplay.config(state="disabled")
        bookDisplay.pack(side="right")


class SearchBox(tk.Entry):
    def __init__(self, root, resultsBox, dataHolder, kwargs = {}):
        super().__init__(root, **kwargs)
        self.value = ""
        self.resultsBox = resultsBox
        self.dataHolder = dataHolder
        self.bind("<KeyRelease>", self.update)
        self.pack(padx=10, pady=5)

    def update(self, event):
        self.value = self.get().lower()
        result = ""
        if self.value != "":
            result = self.dataHolder.search_book(self.value)
        else:
            result = "..."
        self.resultsBox.config(state="normal")
        self.resultsBox.delete(1.0, "end")
        self.resultsBox.insert("end", result)
        self.resultsBox.config(state="disabled")

def formatBookDisplay(book: Book):
    return f"{book.title} -by {book.author}. ({book.genre})"

def getSaveData(filename: str):
    with open(filename, "r") as file:
        text = file.read()
        if len(text) > 0:
            bookData = text.split("\n")
            books = {}
            for data in bookData:
                if len(data) > 0:
                    try:
                        values = data.split("|")
                        books[values[0]] = Book(values[0], values[1], values[2])
                    except:
                        pass
        else:
            books = {}
    return books

def saveBookData(books: dict, filename: str):
    with open(filename, "w") as file:
        tempString = ""
        for key in books:
            book = books[key]
            tempString += f"{book.title}|{book.author}|{book.genre}\n"
        file.write(tempString)

def main(window):
    library = Library(books=getSaveData("savedBooks.txt"))

    tk.Label(window, text="Enter a book to search for:").pack(padx = 10)
    searchResultsDisplay = tk.Text(relief=tk.GROOVE, wrap="word", state="disabled", width=1, height=1, font="trebuchetms 10", bg="lightyellow")
    searchBox = SearchBox(window, searchResultsDisplay, library)
    searchBox.update(None)
    searchResultsDisplay.pack(padx=10, pady=10, expand=True, fill="both")

    displayCatalogueButton = tk.Button(window, text="Display entire catalogue", command=library.display_catalogue)
    displayCatalogueButton.pack(padx=10, pady=5, expand=False, fill="x")

    addBookButton = tk.Button(window, text="Add book", command=library.call_add_book)
    addBookButton.pack(padx=10, pady=10, expand=False, fill="x")

    removeBookButton = tk.Button(window, text="remove book", command=library.call_remove_book)
    removeBookButton.pack(padx=10, pady=10, expand=False, fill="x")

    window.mainloop()

main(window)