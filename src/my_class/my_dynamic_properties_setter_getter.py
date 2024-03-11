"""
func property() umożliwia zdefiniowanie property dynamicznie
"""

class MyClass:
    def __init__(self):
        self.a = "Hello"
        pass

# Dynamically create a property named 'property_name' with a default value of None
property_name = "example_property"

# dodanie gettera i settera, wewnętrzene stan przechowywany zw zmiennej prywatnej _property_name
setattr(MyClass,
        property_name,
        property(
            lambda self: getattr(self, f'_{property_name}', None),
            lambda self, value: setattr(self, f'_{property_name}', value)
        )
        )

# Usage
obj = MyClass()
print(obj.example_property)  # None
print(obj)

obj.example_property = 555
print(obj.example_property)  # 555
print(obj._example_property)  # 555 private