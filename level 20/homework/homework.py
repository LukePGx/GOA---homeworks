# 2

int1 = 5
int2 = 25

print(int1 + int2)

# 3

str1 = "pine"
str2 = "apple"

print(str1 + str2)

# concatenation - merging few strings into a single one

# 4

int1 = 10
int2 = 2

print(int1 / int2)

# we get float type output because Python wants to provide the most precise result of the division operation

# 5

print(5 == 5)
print(5 != 5)
print(5 < 5)
print(5 > 5)
print(5 <= 5)
print(5 >= 5)

# 6

print(5 * 5 != 5 / 5)

# 7


True and True # True
True and False #False
False and True #False
False and False #False
True or True #True
True or False #True
False or True #True
False or False #False

# 8

5 == 5 and 5 != 5
10 > 5 or 5 > 10
25 >= 25 and 40 <= 41
50 > 50 and 20 < 20
50 == 5 or 50 != 5

# 9

for i in range(1, 10):
    print(i)


# 10

listn = [1, 2, 3, 4, 5]

total_sum = 0  


for number in listn:
    total_sum += number

print(total_sum)

# 11


str1 = "Hello, World!"

for i in str1:
    print(i)

# 12

number = 1

while number <= 10:
    print(number)
    number += 1

# 13

number = 1

while number <= 100:
    if 50 <= number <= 60:
        number += 1
        continue
    print(number)
    number += 1

# 14

total_sum = 0 
number = 1     


while total_sum < 50:
    total_sum += number  
    number += 1          
    number - 1
    total_sum

print(f"total sum: {total_sum}")

# 15

def check_divisibility():
    number = int(input("enter a number: "))


    if number % 3 == 0 and number % 5 == 0:
        print(f"number {number} divides on 3 and 5")
    elif number % 3 == 0:
        print(f"number {number} divides on 3")
    elif number % 5 == 0:
        print(f"number {number} divides on 5")
    else:
        print(f"number {number} does not divide on either 3 or 5")

check_divisibility()

# 16

# ??



# 17

# ??

# 18

str1 = "apple"

print(str1.upper())
print(str1.lower())
print(str1.capitalize())
print(str1.find("p"))

print(len(str1))

listn = [1, 2, 3, 4, 5]

listn.append(6)
print(listn)
listn.insert(2, 2.5)
print(listn)
listn.pop(2)
print(listn)






