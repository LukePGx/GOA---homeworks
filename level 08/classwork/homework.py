#2)

print(10 != 20) #True
print(15 != 15) #False

print(10 <= 20) #True
print(10 <= 10) #True

print(15 >= 20) #False
print(20 >= 20) #True

#3)

print(10 == 10) #True
print(10 == 15) #False
print(20 == 10) #False
print(10 != 10) #False
print(10 != 15) #True
print(15 != 10) #True
print(10 >= 10) #True
print(10 >= 15) #False
print(10 <= 10) #True
print(10 <= 15) #True
print(10 > 5) #True
print(7 > 14) #False
print(10 < 5) #False
print(7 < 14) #true
print(False and True) #False
print(False or True) #True
print(False and False) #False
print(False or False) #False
print(True and True) #True
print(True or True) #True

#4)

#using 'and' operator, if there is even one False, we get False in the terminal, we only get True as long as there isnt False.
#using 'or' operator, if there is even one True, we get True in the terminal, we only get False as long as there are only False's.

#5)

num1 = input(int("enter first number: "))
num2 = input(int("enter second number: "))

print(num1 > num2)
print(num1 < num2)
print(num1 == num2)


