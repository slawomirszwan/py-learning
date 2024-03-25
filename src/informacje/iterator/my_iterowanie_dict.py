# Możliwa jest również iteracja po kolekcjach niesekwencyjnych, jak np. dict (tablica asocjacyjna):
# pojedynczy obiekt nie tworzacy sekwencji danych może iterować

dictionary = {'a':1,"b":2,"c":3}

# Iteracja po kluczach
for key in dictionary:
    print(f"{key=}")
"""
key='a'
key='b'
key='c'
"""

# Iteracja po wartościach
for value in dictionary.values():
    print(f"{value=}")
"""
value=1
value=2
value=3
"""

# Iteracja po parach (klucz, wartość)
for key, value in dictionary.items():
    print(f"{key=} {value=}")
"""
key='a' value=1
key='b' value=2
key='c' value=3
"""


iterator = iter(dictionary)
try:
    while True:
        next_value = next(iterator)
        print(next_value)
except StopIteration:
    pass
"""
a
b
c
"""

"""
next(iterator) ----  iterator.__next__()
iter(object_iterable) ---  object_iterable.__iter__()

"""