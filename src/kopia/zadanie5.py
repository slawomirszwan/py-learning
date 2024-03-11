"""zadanie5"""
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

def convert_to_int(txt):
    try:
        number = int(txt)
    except ValueError:
        raise NotNUmberException("BŁĄD !!! Nie podano  liczby")
    return number

def read_int_in_range(prompt, min, max):
    text = read_data(prompt)
    try:
        if text == "quit":
            raise CancelReadNUmberException("Zrezygnowano z podania liczby")
        number = convert_to_int(text)
    except NotNUmberException:
        print("Nie podano liczby. Popraw dane lub Wpisz 'quit' aby zrezygnować")
        return read_int_in_range(prompt, min, max)

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

def read_age():
    min = 0
    max=125
    prompt = "Podaj wiek w pełnych latach (w zakresie {min}-{max}): "
    age = read_int_in_range(prompt, min,max)
    return age

def main():
    try:
        age = read_age()
    except CancelReadNUmberException:
        print("Zrezygnowano z podania dwóch liczb. Nie przeprowadzamy obliczeń")
        print("Bye, Bye")
        return


    print(f"Podano wiek {age}")

    return


main()