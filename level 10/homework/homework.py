#task 2

for i in range(0, 101, 2):
    print(i)

# task 3

num = 1

while num < 1001:
    print(num)
    num += 1


# task 4
    
num = 0

while num < 10:
    print(num + 1)
    print(num + 2)
    print(num + 3)
    print(num + 4) 
    print(num + 5)
    print(num + 6)
    print(num + 7)
    print(num + 8)
    print(num + 9)
    print(num + 10)
    num += 1


# task 5

#for loops
#--------------------------------------------
print()
print("for loop example #1")
print()

for i in range(100, 0, -1):
    print(i)
    print("^- minus 1 =")

#--------------------------------------------
print()
print("for loop example #2")
print()

for i in range(1):
    print("░▄▄▄▄░")
    
    print("▀▀▄██►")
    
    print("▀▀███►")
    
    print("░▀███►░█►")
    
    print("▒▄████▀▀")

#--------------------------------------------
print()
print("for loop example #3")
print()

fruit = ["apple", "banana", "watermelon"]
for x in fruit:
  print(x)
  if x == "banana": break

#--------------------------------------------
print()
print("for loop example #4")
print()

num = [11, 59, 110]
for x in num:
  print(x)
  if x == 59: continue

#--------------------------------------------
print()
print("for loop example #5")
print()

for i in range(1, 100):
   print(i)
   if i == 66: break


# while loops
#--------------------------------------------

print()
print("while loop example #1")
print()

i = 1
while i < 11:
  print(i)
  if i == 6:
    break
  i += 1

#--------------------------------------------
print()
print("while loop example #2")
print()

num = 0
while num < 101:
  print(num)
  num += 1
else:
  print("number is no longer less than 100")



#--------------------------------------------
print()
print("while loop example #3")
print()


number = 0

while number != 100:
   number += 1
   print(number)
 

#--------------------------------------------
print()
print("while loop example #4")
print()

number = 100

while number > 10:
   number -= 1
   print(number)

#--------------------------------------------
print()
print("while loop example #5")
print()

number = int(input('Enter a number: '))


total = 0


while number != 0:
    total += number
    print("███████████████ +")

    number = int(input('Enter a number: '))

print("The total is", total)



