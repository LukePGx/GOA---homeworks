# task 2

guess = int(input("enter your guess: "))



if guess == 5:
    print("your guess is right, congrants!")

elif guess == 1:
    print("your guess is wrong!")

elif guess == 2:
    print("your guess is wrong!")

elif guess == 3:
    print("your guess is wrong!")

elif guess == 4:
    print("your guess is wrong! close tho!")

elif guess == 6:
    print("your guess is wrong! close tho!")

else:
    print("your guess is out of range. guess in range of 1 to 6")



# task 4

# ?

# task 5

guess = int(input("enter your guess (1-10): "))


while guess != 5:
    print("wrong number!")
    guess = int(input("TRY AGAIN: " ))

if guess == 5:
    print("you won!")


# task 6

# ?

# task 7

num = int(input("enter your number: "))

if (num % 2 == 0):
    print("even")

else:
    print("odd")

# task 8

num = int(input("enter your final score: "))

if num in range(90, 100):
    print("A")

if num in range(80, 89):
    print("B")

if num in range(70, 79):
    print("C")

if num in range(60, 69):
    print("D")

if num in range(0, 59):
    print("F")

else:
    print("score can only be in range of 0 to 100! please try again.")


# task 3

i = 1
numbers_sum = 0

while i < 100:
    numbers_sum = numbers_sum + 1
    i += 1

print(numbers_sum)