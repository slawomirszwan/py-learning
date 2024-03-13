"""
W przeciwieństwie do iteratora, generator jest funkcją, która zawiera instrukcję yield,
co pozwala na generowanie kolejnych wartości bez potrzeby utrzymywania stanu pomiędzy wywołaniami.
nie musimy martwić się o ręczne zarzadzanie stanem
"""

def next_number_generator(start=0):
    """
    generator zaczyna od liczby start
    i zwraca kolejne liczby
    :param start:
    :return:
    """

    while True:
        yield start
        start += 1  # wyliczenie następnej generowanej wartości

if __name__ == "__main__":
    # Przykładowe użycie:
    id_generator = next_number_generator(200)

    for _ in range(10):
        print(next(id_generator))

    print(next(id_generator))
    print(next(id_generator))
    print(next(id_generator))

    """
    200
    201
    202
    203
    204
    205
    206
    207
    208
    209
    210
    211
    212
    """