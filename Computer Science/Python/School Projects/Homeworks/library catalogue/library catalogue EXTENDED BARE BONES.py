import tkinter as tk

def formatBook(book):
    return f"{book.title}- by {book.author}. ({book.genre})"

class Book:
    def __init__(self, title, author, genre): self.title, self.author, self.genre = title, author, genre
    def get_title(self): return self.title
    def get_author(self): return self.author
    def get_genre(self): return self.genre

class Library:
    def __init__(self): self.books = {}
    def add_book(self, book): 
        self.books[book.title] = book
    def remove_book(self, title): 
        if title in self.books:
            self.books.pop(title)
    def search_book(self, title): 
        if title in self.books:
            return formatBook(self.books[title])
        else:
            return f"No books with title '{title}'"
    def display_catalogue(self):
        text = ""
        for _, item in self.books.items():
            text += formatBook(item) + "\n"
        tk.Label(tk.Tk(), text=text).pack(padx=30,pady=30)

def main():
    labelFont = ("TrebuchetMS", 10, "bold")
    bgColor = "lemon chiffon"
    window = tk.Tk()
    window.config(bg=bgColor), window.title("Library Catalogue"), window.iconbitmap("library_icon.ico")
    library = Library()
    searchMenu = tk.Frame(window, relief=tk.GROOVE, bg=bgColor)
    addMenu = tk.Frame(window, relief=tk.GROOVE, bg=bgColor)
    removeMenu = tk.Frame(window, relief=tk.GROOVE, bg=bgColor)
    searchBox = tk.Entry(searchMenu, relief=tk.SOLID, bd=1)
    searchBox.bind("<KeyRelease>", lambda event: displayLabel.config(text=library.search_book(searchBox.get())))
    displayLabel = tk.Label(searchMenu, text="  ...  ", bg="white", relief=tk.SOLID, bd=1, height=8, anchor="n", font="TrebuchetMS 9")
    addTitleEntry = tk.Entry(addMenu, relief=tk.SOLID, bd=1)
    addAuthorEntry = tk.Entry(addMenu, relief=tk.SOLID, bd=1)
    addGenreEntry = tk.Entry(addMenu, relief=tk.SOLID, bd=1)
    addButton = tk.Button(addMenu, text="Add", font =labelFont, command=lambda: (library.add_book(Book(addTitleEntry.get(), addAuthorEntry.get(), addGenreEntry.get())), addTitleEntry.delete(0, "end"), addAuthorEntry.delete(0, "end"), addGenreEntry.delete(0, "end")), relief=tk.SOLID, bd=1, bg="lawn green")
    removeTitleEntry = tk.Entry(removeMenu, relief=tk.SOLID, bd=1)
    removeButton = tk.Button(removeMenu, text="Remove", font =labelFont, command=lambda: library.remove_book(removeTitleEntry.get()), bg="indian red", relief=tk.SOLID, bd=1)

    tk.Button(window, text="Display all books", font =labelFont, command=library.display_catalogue, bg="powder blue", fg="black", relief=tk.SOLID, bd=1).pack(padx=20,pady=20,expand=True,fill="both",side="bottom")
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
    tk.Button(addMenu, text="clear", bg="orange", font =labelFont, command=lambda: (addTitleEntry.delete(0, "end"), addAuthorEntry.delete(0, "end"), addGenreEntry.delete(0, "end")), relief=tk.SOLID, bd=1).pack(padx=5, pady=5, side="left", expand=True, fill="x")
    tk.Label(removeMenu, text="Title", bg=bgColor, font =labelFont)
    removeTitleEntry.pack(padx=5, pady=5)
    removeButton.pack(padx=5, pady=5)
    searchMenu.pack(padx=10, pady=10, expand=True, fill="both", side="top")
    addMenu.pack(padx=10, pady=10, expand=True, side="left")
    removeMenu.pack(padx=10, pady=10, side="left")
    window.mainloop()
main()