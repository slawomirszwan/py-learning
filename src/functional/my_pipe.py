

# from toolz import pipe
#
# # Przykładowe funkcje
# def add(x, y):
#     return x + y
#
# def multiply(x, y):
#     return x * y
#
# def subtract(x, y):
#     return x - y
#
# # Składanie funkcji za pomocą pipe()
# result = pipe(5, add, multiply, subtract, 2)
# print(result)  # Wynik: 48

#
# def pipe(data, *functions):
#     """
#
#     :param data:
#     :param functions:
#     :return:
#     """
#     result = data
#     for func in functions:
#         result = func(result)
#     return result
#
# # Przykładowe funkcje
# def add(x, y):
#     return x + y
#
# def multiply(x, y):
#     return x * y
#
# def subtract(x, y):
#     return x - y
#
# # Wywołanie pipe() z funkcjami
# result = pipe(5, lambda x: add(x, 3), lambda x: multiply(x, 2), lambda x: subtract(x, 2))
# print(result)  # Wynik: 16




def pipe(*functions):
    def inner(data):
        result = data
        for func in functions:
            result = func(result)
        return result
    return inner

# Przykładowe funkcje
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def subtract(x, y):
    return x - y

# Wywołanie pipe() z funkcjami
complex_func = pipe(
    lambda x: add(x, 3),
    lambda x: multiply(x, 2),
    lambda x: subtract(x, 2)
)

result = complex_func(5)
print(result)  # Wynik: 16


"""
def pipe(data, *functions):
    result = data
    for func in functions:
        result = func(result)
    return result

# Przykładowe funkcje
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def subtract(x, y):
    return x - y

# Tworzenie złożonej funkcji
def complex_func(data):
    return pipe(data, 
                lambda x: add(x, 3), 
                lambda x: multiply(x, 2), 
                lambda x: subtract(x, 2))

# Użycie złożonej funkcji
result = complex_func(5)
print(result)  # Wynik: 16

"""