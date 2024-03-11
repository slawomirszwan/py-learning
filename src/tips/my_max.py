"""
max(iterable, key= func )

funkcja wbudowana max

key - funkcja która mapuje kazdy element z sekwencji (list, dict,iterator, generator)
na element który będzie analizowany jako maksymalna wartosć

obsługuje sekwencje w których można okreslić kolejnosć np liczby , strumień znaków

Można porównywa elementydla których można określić kolejność
na przykład liczby  - możemy okreslić która liczba jest większa

text - wiemy jaka litera nastepuje po jakiej na podstawie kolejności alfabetycznej

do porównywania wymagane są elementy tego samego typu
"""

# najprostrze użycie

list_data = [5, 6, 7, 2, 1, -2]
max_value = max(list_data)
print(f"{max_value=}")
# max_value=7


list_data = ['ala', 'ola', 'jola', 'Tola', 'Bolek']
max_value = max(list_data)
print(f"{max_value=}")
# max_value='ola'
"""
T jest przed o  w kodzie ascii najpierw duże litery , potem małe
"""

"""
elementy sa porównywane wg kodu liter
jesli chcemy porównac niezależnie od wielkości liter to przydaje się dodatkowy argument nazwany key
"""
list_text_data = ['ala', 'ola', 'jola', 'Tola', 'Bolek']
max_value = max(list_text_data, key=str.lower)
print(f"{max_value=}")
# max_value='Tola'
"""
t jest najwyższą literą w alfabecie spośród elementów
funkcja key dokonuje mapowania każdego elementu listy
do mapowania zostaje użyta funkcja 
i dopiero potem nastepuje porównanie

funckja ma zapewnić mapowanie do wartości która umożliwi porównanie i ustalenie maksymalnej wartości

na przykład sprawdzi się funkcja anonimowa
lambda item:  item.lower(x)

ale często podaje się jako funkcję key metodę porównywanych obiektów

dla obiektu str (string) można wykorzystać metodę

str.lower

każda metoda jest funkcją 
obiekt str ma metodę 

def lower(self):
    return  "lower_strong"

mozna odwołać się do funcji metody poprzez klasę 

str.lower(text_str) 

pierwszym argumentem metody jest obiekt (self)
więc możemy użytć funkcji będącej metoda równieź poza klasą

srt.lower('ABCD')  ==> "abcd"

"""

"""
Znalezienie nazwy klucza z maksymalną wartością
"""
# Przykładowy słownik z danymi
data = {'a': 10, 'b': 5, 'c': 20, 'd': 15}

max_key = max(data)
print(f"{max_key=}")
# max_key='d'


# Znalezienie nazwy klucza elementu z maksymalną wartością
# #################################################
max_key = max(data, key=data.get)

print("Maksymalny klucz:", f"{max_key=}")
# Maksymalny klucz: max_key='c'

"""
W powyższym przykładzie, max() porównuje wartości w słowniku, 
ale zamiast porównywać bezpośrednio wartości, używa funkcji data.get, która zwraca wartość dla danego klucza. W ten sposób, max() znajduje klucz, który ma najwyższą wartość zwracaną przez funkcję data.get.

Możesz dostosować funkcję key w zależności od potrzeb, na przykład, jeśli chcesz znaleźć maksymalny klucz na podstawie długości jego wartości, możesz użyć len jako funkcji klucza.

można użyć key w postaci lambda 
albo podać funkcję
podalimy jako key funkcję będącą metoda obiektu data


key = lambda x:  x.get(x)

czyli porównujemy wartoci

data.get('a')
data.get('b')
data.get('c')
data.get('d')

"""



"szukamy elementu który jest najdłuższy"
fruits = {'apple', 'banana', 'orange', 'kiwi', 'pear'}
longest_fruit = max(fruits, key=len)
print(f"Najdłuższy owoc: {longest_fruit=}")
# Najdłuższy owoc: longest_fruit='banana'

"""
jako key użyliśmy funkcji len zwracającą liczbę długości znaków
"""






"""
Znalezienie maksymalnej wartości w liście krotek na podstawie drugiego elementu:
pairs = [('apple', 5), ('banana', 10), ('orange', 8), ('kiwi', 3)]
max_value_pair = max(pairs, key=lambda x: x[1])
print("Krotka z największym drugim elementem:", max_value_pair)  # Wynik: ('banana', 10)
"""
pairs = [('apple', 5), ('banana', 10), ('orange', 8), ('kiwi', 3)]
# sprawdzamy każdy element listy - drugi element w tuple [1]
max_value_pair = max(pairs, key=lambda item: item[1])
print("Krotka z największym drugim elementem:", max_value_pair)
# Wynik: ('banana', 10)

print( *dir(("apple",5)),sep="\n")
"""
count - returns the number of times a specified value occurs in a tuple 
index - sench element , return first occurence or exception
"""





"""
wyszukiwanie w liście obiektów
szukamy najstarszą osobę w list 
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# list of objects
people = [Person('John', 30), Person('Alice', 25), Person('Bob', 35)]
oldest_person = max(people, key=lambda x: x.age)
print(f"Najstarsza osoba: {oldest_person.name=}")
# Najstarsza osoba: oldest_person.name='Bob'




"""
szukamy których produktów mamy najwięcej w magazynie
w dictionary magazynu
"""
inventory = {'apple': 5, 'banana': 10, 'orange': 8, 'kiwi': 3}
most_stocked_item = max(inventory, key=inventory.get)
print(f"Najwięcej na stanie: {most_stocked_item=}")
# Najwięcej na stanie: most_stocked_item='banana'



"""
Znalezienie maksymalnej liczby na podstawie ich kwadratów
"""
numbers = [5, 8, 3, 10, 6]
max_number = max(numbers, key=lambda x: x**2)

print(f"Liczba z listy o najwyższym kwadracie: {max_number=}")
# Liczba z listy o najwyższym kwadracie: max_number=10




"""
szukamy "najstarszą" literę wystęującą w sekwencji
"""
string_example = "python"
print(max(string_example))
# Output: y




"""
osoba o najwyższych zarobkach
"""
# Using max() to find the employee with the highest salary
employees = [
    {'name': 'John', 'salary': 50000},
    {'name': 'Jane', 'salary': 60000},
    {'name': 'Bob', 'salary': 70000}
]
print(max(employees, key=lambda employee: employee["salary"]))
# {'name': 'Bob', 'salary': 70000}









"""
dodatkowy argument default zwracany gdy nie można określić wartości max
"""
empty_list = []
print(max(empty_list, default="List is empty"))
# List is empty

# print(max(empty_list))
# ValueError: max() arg is an empty sequence




"""
nie można porównywać różnych
"""
print(max(5, '10'))  # Raises TypeError: '>' not supported between instances of 'str' and 'int