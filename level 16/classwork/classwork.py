#task 1

list1 = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109]
#         0   1   2   3   4   5   6   7   8   9
#       -10  -9  -8  -7  -6  -5  -4  -3  -2  -1

#task 2

print(list1[:3])
print(list1[7:])
print(list1[3:7])

#task 3

print(list1[:-7])
print(list1[-3:])
print(list1[-7:-3])

#task 4

list2 = ["apple", "grape", "banana"]

for i in list2:
    print(i)

# task 5

fruit = "apple"

for i in fruit:
    print(list(i))

# task 6

str1 = "there are only 5 bottles"

word1 = str1[:6]
word2 = str1[6:10]
word3 = str1[10:15]
word4 = str1[15]
word5 = str1[17:]

print(word1)
print(word2)
print(word3)
print(word4)
print(word5)


