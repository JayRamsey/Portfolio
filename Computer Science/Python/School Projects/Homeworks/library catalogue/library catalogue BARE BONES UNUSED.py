import tkinter as tk

class Book:
    def __init__(self, title, author, genre):
        self.title, self.author, self.genre = title, author, genre
    
    def get_title(self): return self.title
    def get_author(self): return self.author
    def get_genre(self): return self.genre

class Library:
    def __init__(self):
        self.books = {"test": Book("test title", "test author", "test genre")}
    def add_book(self, book): 
        self.books[book.title] = book
    def remove_book(self, title): 
        del self.books[title]
    def search_book(self, title): 
        return f"Title: {self.books[title].title}, Author: {self.books[title].author}, Genre: {self.books[title].genre}" if title in self.books else f"No books with title '{title}'"
    def display_catalogue(self):
        text = ""
        for _, item in self.books.items():
            text += f"Title: {item.title}, Author: {item.author}, Genre: {item.genre}"
        tk.Label(tk.Tk(), text=text).pack()

def main():
    window = tk.Tk()
    window.config()
    library = Library()
    searchMenu = tk.Frame(window, relief=tk.GROOVE)
    addMenu = tk.Frame(window, relief=tk.GROOVE)
    removeMenu = tk.Frame(window, relief=tk.GROOVE)
    searchBox = tk.Entry(searchMenu)
    searchButton = tk.Button(searchMenu, text="Search", command=lambda: displayLabel.config(text=library.search_book(searchBox.get())))
    displayLabel = tk.Label(searchMenu, text="...")
    addTitleEntry = tk.Entry(addMenu)
    addAuthorEntry = tk.Entry(addMenu)
    addGenreEntry = tk.Entry(addMenu)
    addButton = tk.Button(addMenu, text="Add", command=lambda: library.add_book(Book(addTitleEntry.get(), addAuthorEntry.get(), addGenreEntry.get())))
    removeTitleEntry = tk.Entry(removeMenu)
    removeButton = tk.Button(removeMenu, text="Remove", command=lambda: library.remove_book(removeTitleEntry.get() if removeTitleEntry.get() in library.books else False), bg="pink")

    searchBox.pack(padx=10, pady=10)
    searchButton.pack(padx = 5, pady=5)
    displayLabel.pack(padx=5, pady=5)
    searchMenu.pack(padx=10, pady=10, expand=True, fill="both", side="left")
    tk.Label(addMenu, text="Title").pack()
    addTitleEntry.pack()
    tk.Label(addMenu, text="Author").pack()
    addAuthorEntry.pack()
    tk.Label(addMenu, text="Genre").pack()
    addGenreEntry.pack()
    addButton.pack(padx=5,pady=5)
    addMenu.pack(padx=10, pady=10, expand=True, fill="both", side="left")
    tk.Label(removeMenu, text="Title")
    removeTitleEntry.pack(padx=5, pady=5)
    removeButton.pack(padx=5, pady=5)
    removeMenu.pack(padx=10, pady=10, expand=True, fill="both", side="left")
    tk.Button(window, text="Display all books", command=library.display_catalogue, bg="lightblue", relief=tk.RIDGE).pack(padx=20,pady=20,expand=True,fill="both",side="right")
    window.mainloop()
main()