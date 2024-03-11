"""
zadanie3
"""
def read_data(prompt):
    return input(prompt)

class NotNUmberException(Exception):
    """Not number"""

class CancelReadNUmberException(Exception):
    """cancel read number"""

def validate_bigger_than(min_value):
    def check(value):
        result = value > min_value
        return result
    return check

def validate_bigger_than_message(min_value):
    def message(value):
        print(f"Podana wartość {value} powinna być wieksza od {min_value} ")
        return
    return message

def get_int_range(prompt, validate, validate_message):
    while True:
        try:
            text = input(prompt)
            if text == "quit":
                raise CancelReadNUmberException("Zrezygnowano z podania liczby")

            value = int(text)
            if validate(value):
                return value
            else:
                validate_message(value)
        except ValueError:
            print("Nie podano liczby całkowitej. Spróbuj ponownie ...  lub wpisz quit aby zakończyć.")

def convert_to_number(txt):
    try:
        number = float(txt)
    except ValueError:
        raise NotNUmberException("BŁĄD !!! Nie podano  liczby")
    return number

def read_number(prompt):
    text = read_data(prompt)
    bigger_than_zero_validate = validate_bigger_than(0, )
    bigger_than_zero_message = validate_bigger_than_message(0)

    try:
        if text == "quit":
            raise CancelReadNUmberException("Zrezygnowano z podania liczby")

        value = get_int_range("Podaj długość trójkąta w postaci liczby całkowitej (wiekszej od 0) : ", bigger_than_zero_validate, bigger_than_zero_message)
    except CancelReadNUmberException():
         print("zrezygnowano z podania długości boku trójkąta")

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




def is_valid_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

def main():
    try:
        [a,b,c] = read_three_numbers()
        print(a,b,c)
    except CancelReadNUmberException:
        print("Zrezygnowano z podania trzech liczb. Nie przeprowadzamy obliczeń")
        print("Bye, Bye")
        return

    if is_valid_triangle(a, b, c):
        print(f"z podanych boków trójkąta o długości {a} {b} {c} można zbudować trójkąt")
    else:
        print(f"z podanych boków trójkąta o długości {a} {b} {c} nie można zbudować trójkąta")
    return


main()