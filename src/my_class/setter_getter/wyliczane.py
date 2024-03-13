class Person:
    def __init__(self, first_name, last_name):
        self._firstName = first_name
        self._lastName = last_name

    @property
    def firstName(self):
        return self._firstName

    @property
    def lastName(self):
        return self._lastName
    @property
    def fullName(self):
        return f"{self._firstName=} {self._lastName=}"
    @firstName.setter
    def firstName(self, value):
        self._firstName = value
    @lastName.setter
    def lastName(self, value):
        self._lastName = value

    @lastName.setter
    def fullName(self, value):
        first, last = value.split()
        self._firstName = first
        self._lastName = last

    def show(self):
        print(f"{self._firstName=} {self._lastName=}")

osoba1 = Person('Jan','Kowalski')
Person.show(osoba1)

osoba1.firstName= 'Zenek'
Person.show(osoba1)

osoba1.fullName = "Antoni Zubek"
Person.show(osoba1)