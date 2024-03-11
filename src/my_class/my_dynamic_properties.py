"""
dynamicznie utworzony properties
"""

class MyClass:
    def __init__(self):
        pass

    def set_property(self, property_name, value):
        setattr(self, property_name, value)

# Creating an instance of MyClass
obj = MyClass()

# Setting a property dynamically
property_name = "some_property"
obj.set_property(property_name, 555)

# Accessing the dynamically set property
print(obj.some_property)  # Output: 555
print(obj)