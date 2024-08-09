#1

def arithmetic_mean(lst):
    return sum(lst) // len(lst)


print(arithmetic_mean([1, 2, 3]))

#2

def manual_abs(num):
    if num < 0:
        return -num
    return num


print(manual_abs(-35))

# 3

# def no_dupes(lst): didnt understand

# 4

#1.

def bmi(weight, height):
    bmi_value = weight / (height * height)
    
    if bmi_value <= 18.5:
        return "Underweight"
    elif bmi_value <= 25.0:
        return "Normal"
    elif bmi_value <= 30.0:
        return "Overweight"
    else:
        return "Obese"
    
#2.

def zero_fuel(distance_to_pump, mpg, fuel_left):
    
    max_distance = mpg * fuel_left
    
    return max_distance >= distance_to_pump

#3.

# ?

#4.

def reverse_seq(n):
    return list(range(n, 0, -1))

#5.

# ?

# 6

def count_sheep(n):
    for i in range(n):
        print(i)
        print("sheep...")

print(count_sheep(10))