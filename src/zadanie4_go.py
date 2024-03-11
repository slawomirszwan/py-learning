"""
zadanie4
"""
def read_data(prompt):
    return input(prompt)

class NotNUmberException(Exception):
    """Not number"""

class CancelReadNUmberException(Exception):
    """cancel read number"""

def convert_to_number(txt):
    try:
        number = float(txt)
    except ValueError:
        raise NotNUmberException("BŁĄD !!! Nie podano  liczby")
    return number

def read_number(prompt):
    text = read_data(prompt)
    try:
        if text == "quit":
            raise CancelReadNUmberException("Zrezygnowano z podania liczby")
        number = convert_to_number(text)
    except NotNUmberException:
        print("Nie podano liczby. Popraw dane lub Wpisz 'quit' aby zrezygnować")
        return read_number(prompt)
    return number


def read_three_numbers():
    prompt = "Podaj pierwszą liczbę : "
    number_one = read_number(prompt)
    prompt = "Podaj drugą liczbę : "
    number_two = read_number(prompt)
    prompt = "Podaj trzecią liczbę : "
    number_three = read_number(prompt)
    return [number_one, number_two,number_three]


def search_max(numbers):
    ''''search max przy użyciu if'''
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

def search_min(numbers):
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number
    return min


def main():
    try:
        numbers = read_three_numbers()
    except CancelReadNUmberException:
        print("Zrezygnowano z podania trzech liczb. Nie przeprowadzamy obliczeń")
        print("Bye, Bye")
        return

    print(f"Podano liczby {numbers}")
    max = search_max(numbers)
    print(f"Największa liczba : {max}")
    min = search_min(numbers)
    print(f"Najmniejsza : {min}")

    return


main()