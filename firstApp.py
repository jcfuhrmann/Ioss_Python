# program 1
# prompt and get user's name
name = input("What's your name? ")
print ("Hello " + name + "!")

# prompt and get list of names from user
nameData = []
print ("Please enter ten names to sort, save, and shuffle")
for i in range(10):
    nameData.append(input("Enter data item #" + str(i) + " "))

# sort the list - there is a library function (which we will use later)
# but for this program, we will write our own method
#bubblesort
for j in range(9, -1, -1):
    for i in range(0, j):
        if nameData[i + 1] < nameData[i]:
            temp = nameData[i]
            nameData[i] = nameData[i + 1]
            nameData[i + 1] = temp
            
f = open("firstData.txt", "w")
for i in range(10):
    print(nameData[i])
    f.write(nameData[i] + "\n")    
f.close() 




 
