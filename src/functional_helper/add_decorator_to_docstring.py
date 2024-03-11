from functools import wraps

def add_decorator_to_docstring(decorator_text):
    """
    Ta funkcja jest dekoratorem dodającym docstring
    :param decorator_text:
    :return:
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        # Update the docstring to include the decorator text
        if func.__doc__:
            # jesli func ma docstring to zawieramy go po docstringu dekorującym
            wrapper.__doc__ = f"{decorator_text}\n\n{func.__doc__}"
        else:
            #jesli nie ma to podmieniamy
            wrapper.__doc__ = decorator_text
        return wrapper
    return decorator

