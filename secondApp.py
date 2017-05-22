# program 2
import random
import quicksort

# prompt and get user's name
name = input("What's your name? ")
print ("Hello " + name + "!")

# read list of names from disk file
f = open("firstData.txt", "r", newline=None)
nameData = f.readlines();
f.close

for i in range(len(nameData)):
    print(nameData[i], end = '')

# shuffle it
r = random.SystemRandom()
for j in range (len(nameData)-1, 0, -1):
    pick = r.randrange(0, j)
    temp = nameData[j]
    nameData[j] = nameData[pick]
    nameData[pick] = temp
    
# display new list
print("\n\n")
print("Shuffled")
for i in range(len(nameData)):
    print(nameData[i], end = '')
    
# sort it again, with a quicksort algorithm
quicksort.qsort(nameData, 0, len(nameData)-1)
print("\n\n")
print("after resorting with QuickSort")
for i in range(len(nameData)):
    print(nameData[i], end = '')

            
    

