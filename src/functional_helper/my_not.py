from functools import wraps
from add_decorator_to_docstring import add_decorator_to_docstring

def my_not(func):
    """"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return not result

    decorator_text = f"Ta funkcja jest dekoratorem negującym wynik logiczny funkcji '{func.__name__}()'."
    if func.__doc__:
        # jeśli func miała docstring - to go zawieramy w docstringu wrapper
        wrapper.__doc__ = f"{decorator_text}\n\n{func.__doc__}"

    else:
        # jeśli func nie miała docstring
        # to tylko docstring z wrapera
        wrapper.__doc__ = f"{decorator_text}."

    return wrapper


if __name__ == "__main__":
    def true():
        """Funkcja zawsze zwracająca True"""
        return True


    print(my_not(true))
    # <function true at 0x00000163CF1FB1A0>

    not_true_func = my_not(true)

    # # easy way
    # def not_true_func():
    # """This function negates the result of the 'true' function."""
    # return not true()

    print(not_true_func())
    # False

    # co z docstring przy wrapowaniu ?????????????????
    print(not_true_func.__doc__)
    """
    Ta funkcja jest dekoratorem negującym wynik logiczny funkcji 'true()'.

    Funkcja zawsze zwracająca True
    """
    """niby ok ale nie mamy docstringa wyjaśniającego dla funkcji not_true()"""


    my_false = add_decorator_to_docstring("""To jest funkcja zawsze wzracająca False.""")(my_not(true))

    print(my_false.__doc__)
    """  
    To jest funkcja zawsze wzracająca False.

    Ta funkcja jest dekoratorem negującym wynik logiczny funkcji 'true()'.

    Funkcja zawsze zwracająca True
    """

    """
    mamy docstring nowej utworzonej funkcji oraz dodatkowe docstring - jej dzieci  
    """