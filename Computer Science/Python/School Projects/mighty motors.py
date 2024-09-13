help_list_manager = "The available commands are:\n help - shows this message\n all - displays all cars currently in stock\n new - registers a new car in your system\n delete - enter the index of which car you want to delete\n searchmodel - allows you  to search out of all registered models\n searchmake - filter a specific make\n sell - sell a car\n"
help_list_standard = "The available commands are:\n help - shows this message\n all - displays all cars currently in stock\n new - registers a new car in your system\n sell - sell a car\n"

data = [["index", "Make", "Model", "Colour", "Reg. Year", "Mileage", "Price (£)", "STATUS"],
        ["1", "Ford", "Fiesta", "Yellow", "2010", "50000", "3000", "AVAILABLE"],
        ["2", "Kia", "Sportage", "White", "2019", "3000", "17000", "AVAILABLE"],
        ["3", "Audi", "A3", "Black", "2020", "4000", "19000", "AVAILABLE"],
        ["4", "Ford", "Ka", "Red", "2007", "70000", "2000", "AVAILABLE"],
        ["5", "Kia", "Rio", "Blue", "2006", "16400", "7000", "AVAILABLE"],
        ["6", "Ford", "Mondeo", "Silver", "2000", "70000", "3000", "AVAILABLE"],
        ["7", "Audi", "TT", "Black", "2017", "6000", "12000", "AVAILABLE"],
        ["8", "Kia", "Picanto", "Orange", "2019", "4000", "8000", "AVAILABLE"],
        ["9", "Audi", "A6", "Black", "2019", "14000", "16000", "AVAILABLE"]]

highest_index = 9

def login():
    while True:
        entered_username = input("Username: ")
        entered_username = entered_username.lower()
        if entered_username == "manager" or entered_username == "standard":
            break
        else:
            print("Username invalid")

    while True:
        entered_password = input("Password: ")
        if entered_password == "Manager1234" and entered_username == "manager":
            return "Manager"
        if entered_password == "Standard1234" and entered_username == "standard":
            return "Standard user"
        else:
            print("Incorrect password, please try again.")

def print_table(data):
    print("\n\n")
    for row in range(len(data)):
        row_str = ""
        for column in range(len(data[0])):
            whitespace = ""
            for i in range(get_longest(data) + 2 - len(data[row][column])):
                whitespace += " "
            whitespace += "|"
            row_str += " " + data[row][column] + " " + whitespace
        print(row_str)
    print("\n\n")

def get_longest(data):
    longest = 0
    for row in range(len(data)):
        for column in range(len(data[0])):
            if int(len(data[row][column])) > longest:
                longest = len(data[row][column])
    return longest

def helpprint():
    if user_type == "Manager":
        print(help_list_manager)
    else:
        print(help_list_standard)

def new(highest_index):
    while True:
        make = input("Make: ")
        if make != "":
            break
    while True:
        model = input("Model: ")
        if model != "":
            break
    while True:
        colour = input("Colour: ")
        if colour != "":
            break
    while True:
        reg_year = input("Reg. Year: ")
        if reg_year != "":
            break
    while True:
        mileage = input("Mileage: ")
        if mileage != "":
            break
    while True:
        price = input("Price: ")
        if price != "":
            break

    new_car = [str(highest_index + 1), make, model, colour, reg_year, mileage, price, "AVAILABLE"]

    highest_index += 1
    
    data.append(new_car)
    print("New stock: \n")
    print_table(data)
    
def searchmodel():
    searchterm = input("Make and Model: ")
    search_results = [data[0]]
    for row in range(len(data)):
        if searchterm.lower() == (data[row][1] + " " + data[row][2]).lower():
            search_results.append(data[row])
    if len(search_results) > 1:
        print_table(search_results)
    else:
        print("No item found.")
def searchmake():
    searchterm = input("Make: ")
    search_results = [data[0]]
    for row in range(len(data)):
        if searchterm.lower() == (data[row][1]).lower():
            search_results.append(data[row])
    if len(search_results) > 1:
        print_table(search_results)
    else:
        print("No item found.")

def delete():
    print_table(data)
    while True:
        index = input("Enter the index of the item to delete: ")
        if index.isdigit():
            break
        else:
            print("Invalid value")
    del data[int(index)]
    for row in range(len(data) - 1):
        data[row + 1][0] = str(row + 1)
    print("New stock: \n")
    print_table(data)

def sell():
    print_table(data)
    while True:
        index = input("Enter the index of the item to sell: ")
        if index.isdigit():
            if int(index) <= highest_index:
                break
            else:
                print("Item does not exist")
        else:
            print("Invalid value")
    data[int(index)][-1] = "SOLD"
    print("Updated stock: \n")
    print_table(data)

def command(text):
    text = text.lower()
    if text == "help":
        helpprint()
    if text == "all":
        print_table(data)
    if text == "new":
        new(highest_index)
    if text == "sell":
        sell()
    if user_type == "Manager":
        if text == "searchmodel":
            searchmodel()
        if text == "searchmake":
            searchmake()
        if text == "delete":
            delete()
    if user_type == "Standard user":
        if text == "searchmodel" or text == "searchmake" or text == "delete":
            print("\nYou do not have permission to perform that action\n")

user_type = login()

print("Logged in as: " + user_type + "\n")

helpprint()

#mainloop
while True:
    command(input("Enter command: "))

        


    


    

