# 2

# The map() function applies a specified function to every element in an iterable, like lists or tuples. It produces a result that can be transformed into a list using the list() function for easy viewing or further use.

# 3

# The filter() function is particularly useful for extracting subsets of data that meet certain criteria.

# 4

lists = [[85, 62, 95], [78, 88, 92], [70, 80, 90]]

averages = list(map(lambda sublist: sum(sublist) / len(sublist), lists))
print(averages)

# 5

products = {
    "apple": True,
    "banana": False,
    "orange": True,
    "grapes": False,
    "kiwi": True
}

out_of_stock = dict(filter(lambda item: not item[1], products.items()))
print(out_of_stock)

