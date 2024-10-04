# 1

lst = [1, 2, 3]

add_one = list(map(lambda a: a + 1, lst))

print(lst)

# 2

def sentence(*args):
    result = []
    for word in args:
        result.append(word)
    return ' '.join(result)

# 3

def filter_sentence(words):
    result = []
    bad_words = {"broke", "monkey", "lazy", "beach", "sheet"}
    word = filter(lambda word: word not in bad_words, words)
    return ' '.join(result)

print(filter_sentence("hello monkeys"))