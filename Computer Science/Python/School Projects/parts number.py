total_old = 0
total = 0

while True:
    part_num = ""
    while part_num.len() != 4:
        part_num = input("Enter part number")
        if part_num.len() != 4 and part_num.isdigit():
            print("Enter a value that is 4 digits long")
    for i in range(6, 9):
        if part_num[3] = i:
            total_old += 1
    total += 1
    print("There are", total, "and", total_old, "of them are old")
 
