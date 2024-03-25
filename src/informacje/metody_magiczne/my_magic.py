
a = 1

x = int.__add__(a, 55)
print(x)
# 56

y = a + 55
print(y)
# 56

# realizuje operator +  __add__()

z = a.__add__(55)
print(z)
# 56


"""
Operatory:
    +  : __add__(self, other)
    -  : __sub__(self, other)
    *  : __mul__(self, other)
    /  : __truediv__(self, other)
    // : __floordiv__(self, other)
    %  : __mod__(self, other)
    ** : __pow__(self, other)

Operatory Porównawcze:
    <  : __lt__(self, other)
    >  : __gt__(self, other)
    <= : __le__(self, other)
    >= : __ge__(self, other)
    == : __eq__(self, other)
    != : __ne__(self, other)
"""
