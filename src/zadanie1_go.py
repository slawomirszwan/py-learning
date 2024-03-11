"""
zadanie1
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

def read_two_numbers():
    prompt = "Podaj pierwszą liczbę : "
    number_one = read_number(prompt)
    prompt = "Podaj drugą liczbę : "
    number_two = read_number(prompt)
    return [number_one, number_two]

def main():
    try:
        [x,y] = read_two_numbers()
    except CancelReadNUmberException:
        print("Zrezygnowano z podania dwóch liczb. Nie przeprowadzamy obliczeń")
        print("Bye, Bye")
        return


    print(f"Podano liczby {x} {y}")
    print (f"Suma liczb : {x} + {y} wynosi {x+y}")
    print(f"Różnica liczb : {x} - {y} wynosi {x - y}")
    print(f"Iloczyn liczb : {x} * {y} wynosi {x * y}")

    return


main()