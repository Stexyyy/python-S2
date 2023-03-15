import random
#---------------------------------------

colors = ["Purple", "Blue", "Turquoise", "Iris", "Ocean"] #lists always start off with 0 instead of 1.
print(colors[0]) #prints just purple
print(colors[2]) #prints the middle slot
print(colors[4]) #prints out the last slot
colors.append("Indigo") #adds an item to the end of the list
print(colors)

#I love these colors they're so nice

#--------------------------------------------------------------
paychecks = [519.41, 199.57, 0, 0]
total = 0

for i in range(len(paychecks)):
    total = total + paychecks[i]
    
print("The sum of your 4 last paychecks are: ", total)

#--------------------------------------------------------------

foods = []

length = 3

for m in range(length):
    item = input("What food would you like on your trip to mars (preferably 3 choices): ")
    foods.append(item)
    
print(foods, "are the choices.")

#--------------------------------------------------------------
a = [random.randint(1, 10) for i in range (0, 12)]

b =[]
for s in range(12):
    b.append(a[11-s])
    
print("original list:", a)
print("reversed list but with for loop:", b)

#---------------------------------------------------------

a.sort()
print(a)
print("The largest element in this list is: ", max(a))

#-----------------------

for m in range(10):
    if a[m]+1 == a[m+1]:
        if a[m+1]+1 == a[m+2]:
            print("The list contains: ", a[m], a[m+1], a[m+2])
            
#-----------------------

a.sort(reverse=True)
print("Heres the list reversed aka decending order as well: ", a)

#------------------------------------------------------------
