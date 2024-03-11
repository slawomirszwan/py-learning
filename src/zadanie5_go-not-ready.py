"""
zadanie 5
"""

# class NotNUmberException(Exception):
#     """Not number"""


class CancelReadNUmberException(BaseException):
    """cancel read number"""

class NumberOverrangeException(BaseException):
    """int to bit"""

class NumberUnderangeException(BaseException):
    """int to bit"""

def validate_range(min_value, max_value):
    def check(value):
        result = value >= min_value and value <= max_value
        return result
    return check
def validate_range_message(min_value, max_value):
    def message(value):
        print(f"Podana wartość {value} nie mieści się w wymaganym przedziale {min_value} do {max_value} ")
        return
    return message

def get_int_range(prompt, validate, validate_message):
    while True:
        try:
            text = input(prompt)
        except ValueError:
            print("Nie podano liczby całkowitej. Spróbuj ponownie ...  lub wpisz quit aby zakończyć.")

        if text == "quit":
            raise CancelReadNUmberException("Zrezygnowano z podania liczby")

        value = int(text)
        if validate(value):
            return value
        else:
            validate_message(value)

def obliczenia(value):
    """
    Wymagania biznesowe
    """
    print(f"obliczenia {value}")
    if value >= 18:
        print("jesteś pełnoletni")
        print("mozesz startować w wyborach na prezydenta miasta")
    if value>= 35:
        print("możesz startować w wyborach na prezydenta RP")
    if value >= 65:
        print("osiągnąłeś wirk 65lat")

def go():
    # try:
    range_validate = validate_range(0,125)
    range_error_message = validate_range_message(0,125)
    try:
        value = get_int_range("Podaj wiek w postaci liczby całkowitej : ", range_validate, range_error_message)
    except CancelReadNUmberException():
         print("zrezygnowano z podania wieku")
    obliczenia(value)
def main():
    go()



main()