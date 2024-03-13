"""
wzorzec projektowy Iterator

umożliwia iterację - przechodzenie prze kolejne elementy sekwencji/ strumienia danych


"""

class IteratorListy:
    """iterator który robi to co wbudowany iterator obsługujący list"""
    def __init__(self, my_list:list):
        """
        inicjalizacja:
            okreslamy strumień danych
            oraz stan iteratora
        :param data:
        """
        # strumień danych
        self.data = my_list
        # stan iteratora - index w sekwencji danych (pierwszy element w sekwencji)
        self.index = 0

    def __next__(self):
        """
        metoda zwracająca kolejny element w sekwencji
        albo generująca wyjątek StopIteration w przypadku końca sekwencji danych
        :return:
        """
        # gdy brak kolejnego elementu w sekwencji wyjątek
        if self.index >= len(self.data):
            raise StopIteration

        # zwracamy kolejny element w sekwencji - kolejny element listy (na podstawie stanu)
        value = self.data[self.index]
        # zmieniamy stan iteratora
        self.index += 1
        return value


# Użycie niestandardowego iteratora
my_list = [1, 2, 3, 4, 5]
# iterator iterujący po liście my_list
my_iterator = IteratorListy(my_list)
print(my_iterator)
"""
<__main__.IteratorListy object at 0x0000029BC9754E10>
"""

try:
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
except StopIteration:
    print("koniec sekwencji danych")
"""
1
2
3
4
5
koniec sekwencji danych
"""


"""
my_iterator - jest obiektem iterującym po konkretnej liście 


klasa IteratorListy fabrykuje iteratory dla konkretnych sekwecji danych 

 
"""



my_list2 = [4,8,5]
# iterator iterujący po liście my_list2
my_iterator2 = IteratorListy(my_list2)
print(my_iterator2)

"""
dla iteratorów można użyć funkcji next() która zwraca metodę __next__
"""
try:
    print(next(my_iterator2))
    print(next(my_iterator2))
    print(next(my_iterator2))
    print(next(my_iterator2))
    print(next(my_iterator2))
except StopIteration:
    print("koniec sekwencji danych")

"""
<__main__.IteratorListy object at 0x00000160BAC44DD0>
4
8
5
otrzymujemy kolejne (next) elementy sekwencji
"""


# ===============================================================================================

""" 
w pytanie stworzono ogólne pojęcie obiektów iterowalnych

na przykład listy są iterowalne 
teksty sa iterowalne


Obiekty iterowalne to takie obiektó które można iterować

Wyróżniają się metodą  __iter__ 
która zwraca iterator po którym można obiekt iterować
"""


class IterableList():
    """
    tworzymy własny obiekt iterowalny
    """

    def __init__(self, my_list):
        self.data = my_list

    def __iter__(self):
        return IteratorListy(self.data)

# -----------------------------







moja_lista = IterableList([5,4,3,2,1,0])


"""
dla obiektów iterowalny można użyć funkcji iter()  która zwraca ich iterator
"""

iterator_moja_lista = iter(moja_lista)

print(iterator_moja_lista)
print(iterator_moja_lista ==  moja_lista.__iter__)
"""
<__main__.IteratorListy object at 0x00000196F15859D0>
False
"""


try:
    print(next(iterator_moja_lista))
    print(next(iterator_moja_lista))
    print(next(iterator_moja_lista))
    print(next(iterator_moja_lista))
    print(next(iterator_moja_lista))
    print(next(iterator_moja_lista))
    print(next(iterator_moja_lista))
    print(next(iterator_moja_lista))
except StopIteration:
    print("koniec sekwencji danych")

"""
5
4
3
2
1
0
koniec sekwencji danych
"""






"""
Python ma szeroko wbudowaną obsługę obiektór iterowalnych

Na przykład obsługa jest wbudowana w składnię for in 
"""
for n in  moja_lista:
    print(n)
"""
5
4
3
2
1
0
"""





"""
Często tworzy się obiekty iterowalne które jednocześnie sa iteratorami:

posiadają metody __iter__ zwracają ce same siebie
oraz metodę __next__

"""

# ========================================================
"""
przykład iteratora zwracającego odwróconą sekwencje tekstu

przykład idei iteratora

oczywiscie w pytonie prościej odwrócić tekst już wbudowanymi mechanizmami w klasę str   text[::-1]
"""
class ReverseIterator:
    def __init__(self, text):
        # sekwencja danych
        self.text = text
        # stan wewnętrzny iteratora
        self.index = len(text) - 1

    # zracany iterator - self - bo sam obiekt jest jednocześnie iteratorem
    # i obiektem po którym można iterować  (ma metodę __iter__)
    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            char = self.text[self.index]
            self.index -= 1
            return char
        else:
            raise StopIteration

# Użycie niestandardowego iteratora
my_text = "Hello, world!"
reverse_iterator = ReverseIterator(my_text)
for character in reverse_iterator:
    print(character)
"""
!
d
l
r
o
w
 
,
o
l
l
e
H
"""
