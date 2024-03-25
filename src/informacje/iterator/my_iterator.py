"""

generator
iterator
"""

"""
iterator is an object 
that represents a stream of data. 
It enables iteration over elements in a sequence one at a time, without having to store them all in memory at once. 
Iterators are used in constructs like loops to iterate over elements of a collection.

To create an iterator, yoor object  typically implement two methods in a class:

__iter__: This method returns the iterator object itself and is invoked when the iterator is created.
__next__: This method returns the next item in the sequence. If there are no more items to return, it raises the StopIteration exception.



class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            item = self.data[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

# Example usage:
my_iter = MyIterator([1, 2, 3, 4, 5])

# Iterating over elements using a for loop
for item in my_iter:
    print(item)

# Or iterating using next() function
my_iter = MyIterator([1, 2, 3, 4, 5])
print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
print(next(my_iter))  # 4
print(next(my_iter))  # 5
# This will raise StopIteration as there are no more elements
print(next(my_iter))  # StopIteration

In Python, many built-in objects are iterable or can be converted into iterators using functions 
like iter() (for example, lists, tuples, dictionaries, etc.). 
Additionally, Python provides convenient ways to work with iterators, such as generator functions and comprehensions.


=======================================
In Python, a generator is a special type of iterator that generates values on-the-fly, 
instead of storing them in memory all at once. 

Nie mamy sekwencji danych !!!!!!!!
ale generujemy ją na bieżąco gdy potrzeba następnej wartości 

Generators are defined using functions that contain one or more yield statements. 
When the generator function is called, it returns a generator object, which can be iterated over to produce values.

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

# Using the generator
gen = my_generator()

# Iterating over the generator
for value in gen:
    print(value)

1
2
3
4
5

Generators are useful when you need to iterate over a large sequence of values, 
but you don't want to store them all in memory at once. 
They are memory efficient because they only produce values when requested and maintain their state between calls.

Generators can also be used to create infinite sequences or to represent stream processing tasks.

Here's an example of an infinite generator that generates Fibonacci numbers:

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the generator
fib_gen = fibonacci()

# Printing the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib_gen))

0
1
1
2
3
5
8
13
21
34

Generators are a powerful tool in Python for working with large datasets, stream processing, 
and implementing lazy evaluation. 
They provide a clean and efficient way to work with sequences of values without consuming excessive memory.

=====================================================

Iterator w Pythonie 

Iterator to obiekt,który reprezentuje strumień danych 
i umożliwia iterację po elementach sekwencji po jednym elementu w czasie, 
bez konieczności przechowywania wszystkich w pamięci na raz. 
Iteratory są wykorzystywane w konstrukcjach takich 
jak pętle do iteracji po elementach kolekcji.

Aby stworzyć iterator, zazwyczaj implementuje się dwa metody w klasie:
__iter__: Ta metoda zwraca sam obiekt iteratora i jest wywoływana podczas tworzenia iteratora.
__next__: Ta metoda zwraca następny element w sekwencji. Jeśli nie ma więcej elementów do zwrócenia, 
podnosi wyjątek StopIteration.
Oto prosty przykład iteratora w Pythonie:

class MojIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            item = self.data[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

# Przykład użycia:
moj_iter = MojIterator([1, 2, 3, 4, 5])

# Iterowanie po elementach za pomocą pętli for
for item in moj_iter:
    print(item)

# Lub iterowanie za pomocą funkcji next()
moj_iter = MojIterator([1, 2, 3, 4, 5])
print(next(moj_iter))  # 1
print(next(moj_iter))  # 2
print(next(moj_iter))  # 3
print(next(moj_iter))  # 4
print(next(moj_iter))  # 5
# To spowoduje podniesienie wyjątku StopIteration, ponieważ nie ma więcej elementów
print(next(moj_iter))  # StopIteration
W Pythonie wiele wbudowanych obiektów jest iterowalnych lub można je przekształcić w iteratory za pomocą funkcji 
takich jak iter() (na przykład listy, krotki, słowniki, itp.). Ponadto Python zapewnia wygodne sposoby pracy 
z iteratorami, takie jak funkcje generatorowe i składnie.

Iteratorzy są ważnym mechanizmem w Pythonie, umożliwiającym efektywne zarządzanie pamięcią i przetwarzanie 
dużych zbiorów danych w sposób leniwy. Dzięki nim możliwe jest efektywne przetwarzanie danych nawet wtedy, gdy nie można 
ich przechować w całości w pamięci.

===================================

"""










