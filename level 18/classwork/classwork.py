#task 1

def greeting(name):
    print(f"hello {name}")

name = (input("enter your name: "))

greeting(name)


#task 2

def threesum(num1=0, num2=0, num3=0):
    if type (num1) is str:
        print("error")
    elif type (num2) is str:
        print("error")
    elif type (num3) is str:
        print("error")
    else: 
        print(num1 + num2 + num3)

threesum(10, 20, 30)

# task 3

def range_nums(num1=0, num2=0):
    for i in range(num1, num2):
        print(i)

number1 = int(input("enter first number: "))
number2 = int(input("enter second number: "))

range_nums(number1, number2)


# task 4

def info(name, lastname, academy):
    print(f"my name is {name}")
    print(f"my lastname is {lastname}")
    print(f"i study in {academy}")


name = input("enter your name: ")
lastname = input("enter yout lastname: ")
academy = input("enter your academy: ")


info(name, lastname, academy)

#task 5

# ?

# task 6

def discount(age):
    if age >= 18:
        print("you didnt get a discount!")
    elif age < 18:
        print("you got a discount")

age = int(input("enter your age: "))

discount(age)

# task 7

def threediv(num1=0, num2=0, num3=0):
    
    if type (num1) is str:
        print("error")
    elif type (num2) is str:
        print("error")
    elif type (num3) is str:
        print("error")
    else: 
        print(numbersum = num1 * num2 * num3)

threediv(1, 10, 10)

