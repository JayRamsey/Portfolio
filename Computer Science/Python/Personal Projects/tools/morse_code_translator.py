import tkinter as tk
from winsound import Beep
from icecream import ic
from time import sleep
import customtkinter as ctk


morse = ["._", "_...", "_._.", "_..", ".", ".._.", "__.", "....", "..", ".___", "_._", "._..", "__",
             "_.", "___", ".__.", "__._", "._.", "...", "_", ".._", "..._", ".__", "_.._", "_.__", "__..",
             ".____", "..___", "...__", "...._", ".....", "_....", "__...", "___..", "____.", ""]

def play(string: str, freq: int, timeUnit: int):
    for letter in string:
        if letter == "_":
            beep(3, freq, timeUnit)
        if letter == ".":
            beep(1, freq, timeUnit)
        if letter == "/":
            sleep(timeUnit * 7/ 1000)
        elif letter == " ":
            sleep(timeUnit * 3/ 1000)         
            
def beep(length: int, freq: int, timeUnit) -> None:
    Beep(freq, length * timeUnit)

def translate(chars: str, mode: str) -> list[int]:
    global morse
    alpha = list("abcdefghijklmnopqrstuvqxyz0123456789 ")
    
    output = ""
    chars = chars.lower()
    if mode == "ma":
        for i in chars.split("/"):
            for j in i.split(" "):
                if j in morse:
                    output += alpha[morse.index(j)]
            output += " "
        
    elif mode == "am":
        ic()
        for i in chars.split(" "):
            for j in i:
                ic(j)
                if j in alpha:
                    output += ic(morse[alpha.index(j)] + " ")
            output += "/"
    return output


def main():
    bg = "ivory3"
    window = tk.Tk()
    window.title("Morse code translator")
    window.config(bg=bg)
    textFrame = tk.Frame(window, bg=bg)
    textFrame.pack(padx=20, pady=20, expand=True, fill="both")
    
    textBoxAlpha = tk.Text(textFrame, wrap="word", relief="solid", bd=1, width=40, height=2, bg = "azure", font = "CascadiaCode 9")
    tk.Label(textFrame, bg=bg, text="Alpha numeric characters").pack()
    textBoxAlpha.pack(pady=10)
    textBoxMorse = tk.Text(textFrame, wrap="word", relief="solid", bd=1, width=40, height=4, bg = "linen", font = "bold")
    tk.Label(textFrame, bg=bg, text="Morse Code").pack()
    textBoxMorse.pack(pady=10)
    textBoxAlpha.bind("<KeyRelease>", lambda event:(textBoxMorse.delete("1.0", "end"), textBoxMorse.insert("end", translate(textBoxAlpha.get("1.0", "end"), "am"))))
    textBoxMorse.bind("<KeyRelease>", lambda event:(textBoxAlpha.delete("1.0", "end"), textBoxAlpha.insert("end", translate(textBoxMorse.get("1.0", "end"), "ma"))))
    optionsFrame = tk.Frame(window, bg=bg)
    optionsFrame.pack(padx=20, pady=20, expand=True, fill="both")
    
    timeSlider = ctk.CTkSlider(optionsFrame, from_=20, to=1000, number_of_steps=1000)
    timeSlider.pack(padx=10, pady=10)
    playButton = tk.Button(optionsFrame, text="Play Audio", command = lambda: play(textBoxMorse.get("1.0", "end"), 200, int(timeSlider.get())), relief="solid", bd=1, bg="medium slate blue")
    playButton.pack()
    
    window.mainloop()
main()
