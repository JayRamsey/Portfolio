weekA = open("weekA.txt", "r")
weekB = open("weekB.txt", "r")

#fileContentA = weekA.read()
#fileContentB = weekB.read()
indexA = 0
indexB = 0

for itemA in weekA:
    print("There was an attempt...")
    isUnique = True
    for itemB in weekB:
        print("Compare", itemA,"with",itemB)
        if itemA == itemB:
            isUnique = False
            print("We are the same")
        indexB += 1
        if indexB < 3:
            weekB.seek(0)
    if isUnique == True:
        print("Actual output:",itemA)
    indexA +=1
    if(index < 3):
        weekA.seek(0)
            
