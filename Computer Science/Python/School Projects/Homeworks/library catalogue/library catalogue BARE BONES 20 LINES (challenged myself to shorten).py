import tkinter as tk
class Book:
    def __init__(self, title, author, genre): self.title, self.author, self.genre = title, author, genre
    def get_title(self): return self.title
    def get_author(self): return self.author
    def get_genre(self): return self.genre
class Library:
    def __init__(self): self.books = {"test": Book("test title", "test author", "test genre")}
    def add_book(self, book): self.books[book.get_title()] = book
    def remove_book(self, title): del self.books[title]
    def search_book(self, title): return f"Title: {self.books[title].get_title()}, Author: {self.books[title].get_author()}, Genre: {self.books[title].get_genre()}" if title in self.books else f"No books with title '{title}'"
    def display_catalogue(self):
        newWindow=tk.Tk()
        text = tk.Text(newWindow, bg="lightblue", font="ariel 10", width=75, height=10, wrap="word")
        for _, item in self.books.items(): text.insert("end",f"Title: {item.get_title()}, Author: {item.get_author()}, Genre: {item.get_genre()}\n")
        text.pack(padx=30, pady=30), newWindow.config(bg="lightyellow"),text.config(state="disabled")
window, library = tk.Tk(), Library()
searchMenu, addMenu, removeMenu, _ = tk.Frame(window,bg="lightyellow"), tk.Frame(window,bg="lightyellow"), tk.Frame(window,bg="lightyellow"), window.config(bg="lightyellow")
searchBox, searchButton, displayLabel, addTitleEntry, addAuthorEntry, addGenreEntry, addButton, removeTitleEntry, removeButton = tk.Entry(searchMenu), tk.Button(searchMenu, text="Search", command=lambda: displayLabel.config(text=library.search_book(searchBox.get())), bg="lightblue"),tk.Label(searchMenu, text="...", bg="lightyellow"),tk.Entry(addMenu),tk.Entry(addMenu),tk.Entry(addMenu), tk.Button(addMenu, text="Add", command=lambda: library.add_book(Book(addTitleEntry.get(), addAuthorEntry.get(), addGenreEntry.get())), bg="lightgreen"), tk.Entry(removeMenu), tk.Button(removeMenu, text="Remove", command=lambda: library.remove_book(removeTitleEntry.get() if removeTitleEntry.get() in library.books else False),bg="pink")
searchBox.pack(padx=10, pady=10),searchButton.pack(padx = 5, pady=5),displayLabel.pack(padx=5, pady=5),searchMenu.pack(padx=10, pady=10, expand=True, fill="both", side="left"), tk.Label(addMenu, text="Title", bg="lightyellow").pack(), addTitleEntry.pack(), tk.Label(addMenu, text="Author", bg="lightyellow").pack(), addAuthorEntry.pack(), tk.Label(addMenu, text="Genre", bg="lightyellow").pack(),addGenreEntry.pack(),addButton.pack(padx=5,pady=5),addMenu.pack(padx=10, pady=10, expand=True, fill="both", side="left"), tk.Label(removeMenu, text="Title", bg="lightyellow").pack(),removeTitleEntry.pack(padx=5),removeButton.pack(padx=5, pady=5, expand=True),removeMenu.pack(padx=10, pady=10, expand=True, fill="both", side="left"), tk.Button(window, text="Display all books", command=library.display_catalogue, bg="lightblue", relief=tk.RIDGE).pack(padx=20,pady=20,expand=True,fill="both",side="right"), window.mainloop()
