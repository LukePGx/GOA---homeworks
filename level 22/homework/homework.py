# 2

numbers = [5, 3, 8, 1, 2]

def manual_min(lst):
    min_value = lst[0]
    for number in lst[1:]:
        if number < min_value:
            min_value = number
    return min_value

print(manual_min(numbers))

# 3

def manual_max(lst):
    max_value = lst[0]
    for number in lst[1:]:
        if number > max_value:
            max_value = number
    return max_value

print(manual_max(numbers))

# 4

def manual_len(lst):
    count = 0
    for i in lst:
        count += 1
    return count

print(manual_len(numbers))

# 5

def manual_sum(lst):
    total = 0
    for number in lst:
        total += number
    return total

print(manual_sum(numbers))

# 6

def manual_find(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    

print(manual_find(numbers, 5))
