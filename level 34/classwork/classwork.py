# 1

#IndexError - incorrect index, or its over the range of the list.
#TypeError - the variable you are trying to use is not defined
#SyntaxError - invalid syntax in the code
#ValueError - inncorrect value type

# 2

name = "luka"
try:
    print(age)
except NameError:
    print("wrong variable name")

# 3

lst = [1, 2, 3, 4, 5]
try:
    print(lst[8])
except IndexError:
    print("wrong index number")


# 4

word = "hello"
try:
    int(word)
except ValueError:
    print("invalid value type!")


# 5

# try/except are really useful when we except an error, but we must continue executing the code
# using try/except, doesnot stop code execution while there is an error in a certain line of a code