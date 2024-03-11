"""
różnice między property a setter getter

Getters: These are the methods used in Object-Oriented Programming (OOPS) which helps to access the private attributes from a class.
Setters: These are the methods used in OOPS feature which helps to set the value to private attributes in a class.



enkapsulacja prywatnej zmiennej w klasie

zmienna prywatna oznacza tylko konwencję !!!!!!!!!  zproperties i zmienne sa nadal dostepne spoza klasy
"""

class SampleClass:

    def __init__(self, a):
        ## private varibale or property in Python __a
        self.__a = a

    ## getter method to get the properties using an object
    def get_a(self):
        return self.__a

    ## setter method to change the value 'a' using an object
    def set_a(self, a):
        self.__a = a

## creating an object
obj = SampleClass(10)

## getting the value of 'a' using get_a() method
print(obj.get_a())

## setting a new value to the 'a' using set_a() method
obj.set_a(45)

print(obj.get_a())


"""
prywatry atrybut , getter , setter
"""

# --------------------------------
class PythonicWay:

    def __init__(self, a):
        self.a = a


## Creating an object for the 'PythonicWay' class
obj = PythonicWay(100)

print(obj.a)

# ----------------------------------

class SampleClass1:

    def __init__(self, a):
        ## calling the set_a() method to set the value 'a' by checking certain conditions
        self.set_a(a)

    ## getter method to get the properties using an object
    def get_a(self):
        return self.__a

    ## setter method to change the value 'a' using an object
    def set_a(self, a):

        ## condition to check whether 'a' is suitable or not
        if a > 0 and a % 2 == 0:
            self.__a = a
        else:
            self.__a = 2  #default

## creating an object for the class 'SampleClass1'
obj = SampleClass1(16)

print(obj.get_a())

# ----------------------------------------------
"""
property() dekorator
"""
class Property:

    def __init__(self, var):
        ## initializing the attribute
        self.a = var

    @property
    def a(self):
        return self.__a

    ## the attribute name and the method name must be same which is used to set the value for the attribute
    #setter dla a
    @a.setter
    def a(self, var):
        if var > 0 and var % 2 == 0:
            self.__a = var
        else:
            self.__a = 2

## creating an object for the class 'Property'
obj = Property(23)

print(obj.a)
# 2
"""
@property 
bierze wartość prywatnej zmiennej 

do ustawianie prywatnej wartości używamy  @method_name.setter  tą funkcję użyjemy djak setter

"""



# --------------------------------------------------
"""
inny sposób ustawienia gettera i settera to użycie  property(getter,setter)
"""
class AnotherWay:

    def __init__(self, var):
        ## calling the set_a() method to set the value 'a' by checking certain conditions
        self.set_a(var)

    ## getter method to get the properties using an object
    def get_a(self):
        return self.__a

    ## setter method to change the value 'a' using an object
    def set_a(self, var):

        ## condition to check whether var is suitable or not
        if var > 0 and var % 2 == 0:
            self.__a = var
        else:
            self.__a = 2

    a = property(get_a, set_a)


## creating an object for the 'AnotherWay' class
# nie trzeba odwoływać się do metod
obj = AnotherWay(28)

print(obj.a)
# 28

# ----------------------------------------------
"""
zrobimy finkcje get set prywatne
"""

class FinalClass:

    def __init__(self, var):
        ## calling the set_a() method to set the value 'a' by checking certain conditions
        self.__set_a(var)

    ## getter method to get the properties using an object
    def __get_a(self):
        return self.__a

    ## setter method to change the value 'a' using an object
    def __set_a(self, var):

        ## condition to check whether var is suitable or not
        if var > 0 and var % 2 == 0:
            self.__a = var
        else:
            self.__a = 2

    a = property(__get_a, __set_a)

## creating an object for the 'AnotherWay' class
obj = FinalClass(12)


print(obj.a)
# 12
obj.a = 4
print(obj.a)