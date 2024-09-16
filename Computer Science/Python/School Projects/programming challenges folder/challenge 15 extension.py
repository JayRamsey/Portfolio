text = input("Enter a sentence")
splitText = text.split()
print("The sentence is", len(splitText), "words long")

backward  = ""
for i in range(len(splitText)):
    backward += splitText[-i]
    backward += " "
print("The sentence backwards is:", backward)
    
