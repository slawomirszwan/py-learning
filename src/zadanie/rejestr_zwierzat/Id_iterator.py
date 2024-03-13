"""
Iterator to obiekt,który reprezentuje strumień danych i umożliwia
iterację po elementach sekwencji po jednym elementu w czasie, bez konieczności przechowywania wszystkich w pamięci na raz.
Iteratory są wykorzystywane w konstrukcjach takich jak pętle do iteracji po elementach kolekcji.


*metoda __iter__  : zwraca  obiekt iteratora  który posiada metodę __next__
*metoda __next__  : zwraca kolejny element w sekwencji (jest metoda iteratora)
"""
class Id_iterator:
    """
    klasa która spełnia 2 role jednocześnie:
    * wzorzec FABRYKA - produkująca iterator w zależności od argumentu start zwracany  w  metodzie __iter__
    * wzorzec ITERTOR - zwraca w
    Iterator dający kolejne id - kolejny numer or 0,1,2,3,....
    """
    def __init__(self, start=0):
        self.current = start

    """
    zwraca iterator - akurat tutaj iteratorem  (z metoda __next__  jest cała klasa
    """
    def __iter__(self):
        return self

    """
    metoda iteratora dająca nastepną wartość w sekwencji , strumieniu danych
    """
    def __next__(self):
        num = self.current
        self.current += 1   # zmiana stanu iteratora
        return num

if __name__ == "__main__":

    # Przykładowe użycie:
    id = Id_iterator(100)

    for _ in range(10):
        print(next(id))


    next_id = next(id)
    print(next_id)

    """
    100
    101
    102
    103
    104
    105
    106
    107
    108
    109
    
    110
    """