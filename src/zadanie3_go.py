
class CancelReadNUmberException(Exception):
    """cancel read number"""


def validate_bigger_than(min_value):
    def check(value):
        result = value > min_value
        if not result:
            print(f"Podana wartość {value} powinna być wieksza od {min_value} ")
        return result
    return check


def get_bok(prompt, validator):
    while True:
        try:
            text = input(prompt)
            if text == "quit":
                raise CancelReadNUmberException("Zrezygnowano z podania liczby")

            value = float(text)
            print(value)
            if validator(value):
                return value

        except ValueError:
            print("Nie podano liczby. Spróbuj ponownie ...  lub wpisz quit aby zakończyć.")

def get_trzy_boki():
    validator = validate_bigger_than(0)
    prompt = "Podaj długość trójkąta w postaci liczby (wiekszej od 0) : "
    a = get_bok(prompt, validator)
    b = get_bok(prompt, validator)
    c = get_bok(prompt, validator)
    return [a,b,c]

def is_valid_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False
def obliczenia(a,b,c):
    print(f"{a} {b} {c}")

    if is_valid_triangle(a, b, c):
        print(f"z podanych boków trójkąta o długości {a} {b} {c} można zbudować trójkąt")
    else:
        print(f"z podanych boków trójkąta o długości {a} {b} {c} nie można zbudować trójkąta")
    return


def main():
    try:
        [a,b,c] = get_trzy_boki()

        obliczenia(a,b,c)

    except CancelReadNUmberException:
        print("zrezygnowano z podania długości boków. Nie przeprowadzamy obliczeń. BYE BYE")


main()