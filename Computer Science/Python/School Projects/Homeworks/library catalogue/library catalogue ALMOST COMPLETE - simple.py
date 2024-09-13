import tkinter as tk

def formatBook(book):
    return f"{book.title}- by {book.author}. ({book.genre})"

def RIC(string: str, extraChars: str = ""): #"Remove Illegal Characters"
    tempStr = ""
    illegalChars = "|\$" + extraChars
    for char in string:
        if char not in illegalChars:
            tempStr += char
    return tempStr

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

class Book:
    def __init__(self, title, author, genre): self.title, self.author, self.genre = title, author, genre
    def get_title(self): return self.title
    def get_author(self): return self.author
    def get_genre(self): return self.genre

class Library:
    def __init__(self): self.books = {}
    def add_book(self, book): 
        self.books[book.title] = book
        saveBookData(self.books, "savedBooks.txt")
    def remove_book(self, title): 
        if title in self.books:
            self.books.pop(title)
            saveBookData(self.books, "savedBooks.txt")
    def search_book(self, searchedText): 
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
            result += formatBook(self.books[key]) + "\n"
        if result == "":
            result = "No books found."
        return result
    def display_catalogue(self):
        newWindow = tk.Tk()
        newWindow.config(bg="lemon chiffon")
        newWindow.title("Catalogue")
        newWindow.iconbitmap("library_icon.ico")
        txt = tk.Text(newWindow, font="TrebuchetMS 9", relief=tk.SOLID, bd=1, bg="light blue")
        for _, item in self.books.items():
            txt.insert("end", formatBook(item) + "\n\n")
        txt.config(state="disabled")
        txt.pack(padx=20, pady=20)

def main():
    labelFont = ("TrebuchetMS", 10, "bold")
    bgColor = "lemon chiffon"
    window = tk.Tk()
    window.config(bg=bgColor), window.title("Library Catalogue"), window.iconbitmap("library_icon.ico")
    library = Library()
    library.books = getSaveData("savedBooks.txt")
    searchMenu = tk.Frame(window, relief=tk.GROOVE, bg=bgColor)
    addMenu = tk.Frame(window, relief=tk.GROOVE, bg=bgColor)
    removeMenu = tk.Frame(window, relief=tk.GROOVE, bg=bgColor)
    searchBox = tk.Entry(searchMenu, relief=tk.SOLID, bd=1)
    searchBox.bind("<KeyRelease>", lambda event: displayLabel.config(text=library.search_book(searchBox.get())))
    displayLabel = tk.Label(searchMenu, text="  ...  ", bg="white", relief=tk.SOLID, bd=1, height=8, anchor="n", font="TrebuchetMS 9")
    addTitleEntry = tk.Entry(addMenu, relief=tk.SOLID, bd=1)
    addAuthorEntry = tk.Entry(addMenu, relief=tk.SOLID, bd=1)
    addGenreEntry = tk.Entry(addMenu, relief=tk.SOLID, bd=1)
    addButton = tk.Button(addMenu, text="Add", font =labelFont, command=lambda: (library.add_book(Book(RIC(addTitleEntry.get()), RIC(addAuthorEntry.get()), RIC(addGenreEntry.get()))), addTitleEntry.delete(0, "end"), addAuthorEntry.delete(0, "end"), addGenreEntry.delete(0, "end"), displayLabel.config(text=library.search_book(searchBox.get()))), relief=tk.SOLID, bd=1, bg="SkyBlue3")
    removeTitleEntry = tk.Entry(removeMenu, relief=tk.SOLID, bd=1)
    removeButton = tk.Button(removeMenu, text="Remove", font =labelFont, command=lambda: (library.remove_book(removeTitleEntry.get()), removeTitleEntry.delete(0, "end"), displayLabel.config(text=library.search_book(searchBox.get()))), bg="indian red", relief=tk.SOLID, bd=1)

    tk.Button(window, text="Display all books", font =labelFont, command=library.display_catalogue, bg="light sea green", fg="black", relief=tk.SOLID, bd=1).pack(padx=20,pady=20,expand=True,fill="both",side="bottom")
    tk.Label(searchMenu, text="search:", bg=bgColor, font = "TrebuchetMS 11 bold").pack()
    searchBox.pack(padx=10, pady=10)
    displayLabel.pack(padx=5, pady=5, expand=True, fill="both")
    tk.Label(addMenu, text="Title", bg=bgColor, font =labelFont).pack()
    addTitleEntry.pack()
    tk.Label(addMenu, text="Author", bg=bgColor, font =labelFont).pack()
    addAuthorEntry.pack()
    tk.Label(addMenu, text="Genre", bg=bgColor, font =labelFont).pack()
    addGenreEntry.pack()
    addButton.pack(padx=5,pady=5, side="left", expand=True, fill="x")
    tk.Button(addMenu, text="clear", bg="sandy brown", font =labelFont, command=lambda: (addTitleEntry.delete(0, "end"), addAuthorEntry.delete(0, "end"), addGenreEntry.delete(0, "end")), relief=tk.SOLID, bd=1).pack(padx=5, pady=5, side="left", expand=True, fill="x")
    tk.Label(removeMenu, text="Title", bg=bgColor, font =labelFont)
    removeTitleEntry.pack(padx=5, pady=5)
    removeButton.pack(padx=5, pady=5)
    searchMenu.pack(padx=10, pady=10, expand=True, fill="both", side="top")
    addMenu.pack(padx=10, pady=10, expand=True, side="left")
    removeMenu.pack(padx=10, pady=10, expand=True, side="left")
    window.mainloop()
main()