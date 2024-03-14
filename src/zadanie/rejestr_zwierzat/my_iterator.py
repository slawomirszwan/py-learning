"""
wzorzec projektowy Iterator

umożliwia iterację - przechodzenie prze kolejne elementy sekwencji/ strumienia danych

Przykład: obsługa klienta w sklepie - kolejka do kasy
przed kasą ustawia się sekwencja klientów
kasjerka obsługuje klienta
a potem następnego (next please)



według wikipedii:
Iterator – obiekt pozwalający na sekwencyjny dostęp do wszystkich elementów lub części zawartych w innym obiekcie,
zwykle kontenerze lub liście.
Iterator jest czasem nazywany kursorem, zwłaszcza w zastosowaniach związanych z bazami danych.

Podstawowym celem iteratora jest pozwolić użytkownikowi przetworzyć każdy element w kolekcji bez konieczności
zagłębiania się w jej wewnętrzną strukturę. Pozwala to kolekcji przechowywać elementy w dowolny sposób,
podczas gdy użytkownik może traktować ją jak zwykłą sekwencję lub listę.
Klasa iteratora jest zwykle projektowana wraz z klasą odpowiadającej mu kolekcji i jest z nią ściśle powiązana.
Zwykle to kolekcja dostarcza metod tworzących iteratory.

W pytonie wiele klas obiektów zostało zaptojektowanych jako iteratory
umożliwiając wielu funcjom dostep sekwencyjny do elementów kolekcji obiektów


"""
"""
Sprawdzenie czy klasa obiektów jest iteratorem
Można sprawdzić czy posiada metodę  __iter__ która zwraca iterator klasy obiektów
"""

"""
str nie jest iteratorem ale jest obiektem iterowalnym
"""
my_str = "Hello"

# Sprawdzenie, czy obiekt typu str jest iterowalny
print(hasattr(my_str, '__iter__'))
# True

# Pobranie iteratora z obiektu typu str
# mozemy użyć uniwersalnej funkcji  iter()
my_iterator = iter(my_str)

# Sprawdzenie, czy iterator jest iteratorem str
print(hasattr(my_iterator, '__next__'))
# True

# Iteracja po kolejnych znakach za pomocą iteratora
# używamy uniwersalnej funckcji next()
print(next(my_iterator))  # 'H'
print(next(my_iterator))  # 'e'
print(next(my_iterator))  # 'l'
print(next(my_iterator))  # 'l'
print(next(my_iterator))  # 'o'

#sekwencyjny dostep do elementów sekwencji (każdego znaku w strumieniu w stringu


"""
Obiekt iterowalny ma metodę __iter__() która zwraca iterator który umożliwia sekwencyjny dostep do kolekcji sekwencji

iterator jest obiektem który ma metodę __next__() która zwraca kolejny element w sekwencji

Obiekt może być jednocześnie iterowalny i być iteratorem. Wtedy ma 2 metody równocześnie __iter__ i __next__

"""
# ----------------------------------------

"""
wg wikipedii
Iteratory są jednym z podstawowych elementów Pythona i często są w ogóle niezauważalne, 
gdyż są niejawnie wykorzystywane w pętlach for. Wszystkie standardowe typy sekwencyjne w Pythonie, 
jak również wiele klas w bibliotece standardowej, udostępniają iterację. 
Poniższy przykład pokazuje typową niejawną iterację po kolekcji:

for value in sequence:
    print value
Możliwa jest również iteracja po kolekcjach niesekwencyjnych, jak np. dict (tablica asocjacyjna):

# Iteracja po kluczach
for key in dictionary:
    print key

# Iteracja po wartościach
for value in dictionary.itervalues():
    print value

# Iteracja po parach (klucz, wartość)
for key, value in dictionary.iteritems():
    print key, value
Iteratory można również definiować i używać jawnie. Do pobrania iteratora z kolekcji typu sekwencyjnego wykorzystuje się funkcję wbudowaną iter(). Tak utworzony iterator posiada metodę next(), która przy każdym wywołaniu zwraca kolejny element kolekcji. Gdy nie ma więcej elementów, metoda ta rzuca wyjątek StopIteration. Poniższy przykład pokazuje iterację po sekwencji z jawnym iteratorem, równoważną przedstawionej powyżej:

it = iter(sequence)
try:
    while True:
        val = it.next()
        print val
except StopIteration:
    pass
Dowolna zdefiniowana przez użytkownika klasa może udostępniać standardową iterację (niejawną lub jawną), jeśli posiada metodę __iter__() zwracającą iterator. Z kolei zwrócony iterator musi posiadać również metodę __iter__() oraz metodę next().

W Pythonie możliwe jest również użycie generatorów - specjalnego rodzaju iteratorów po niezrealizowanej kolekcji. Generatora używa się tak, jak iteratora, tyle, że sama iterowana kolekcja nie istnieje. Zamiast tego elementy obliczane są na bieżąco.
"""


"""
listy 

>>> [].__iter__
<method-wrapper '__iter__' of list object at 0x00000262E8E8A9C0>

lista ma metodę __iter__
>>> iter([])
<list_iterator object at 0x00000262E8C65210>

ale nie jest iteratorem !!
>>> next([])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not an iterator


>>> list_iterator = iter([1,2,3])
>>> next(liest_iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'liest_iterator' is not defined. Did you mean: 'list_iterator'?
>>> next(list_iterator)  
1
>>> next(list_iterator)
2
>>> next(list_iterator)
3
>>> next(list_iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

Wyjątek StopIteration informuje o końcu sekwencji po której iterujemy 
>>>

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


print(list())
