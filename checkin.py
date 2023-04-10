#-----------------------
#1.
hi = int(input("How much can you brench press? "))
if hi < 10:
    print("Keep practicing...")
elif hi <= 50:
    print("Lookin good!")
else:
    print("damn..! you good!!")
    
#-----------------------
#2.
for i in range (20, 50, 2):
  print(i, end =" ")
print(" ")

#-------------------------
#3.
balls = False
while balls == False:
    ruhroh = input("ribbit! ")
    if ruhroh == "frog":
        balls = True
        print ("ribbit.")
    else:
        print("ribbit!!")
        
#-------------------------
#3.5.
ballin = 100
while (ballin > 50):
    ballin = ballin - 2
    print(ballin)

#-------------------------
#4.
def Avg(x, y):
    x = 8
    y = 4
    return x + y / 2
print(Avg)
