# z list comprehension
from datetime import datetime

class Wizyta:
    def __init__(self, Id_lekarza, Id_pacjenta, Data_wizyty):
        self.Id_lekarza = Id_lekarza
        self.Id_pacjenta = Id_pacjenta
        self.Data_wizyty = datetime.strptime(Data_wizyty, "%Y-%m-%d") #.date()

    def __str__(self):
        return f"ID lekarza: {self.Id_lekarza}, ID pacjenta: {self.Id_pacjenta}, Data wizyty: {self.Data_wizyty}"


class Pacjent:
    def __init__(self, Id_pacjenta, Nazwisko, Imie, PESEL, Data_urodzenia):
        self.Id_pacjenta = Id_pacjenta
        self.Nazwisko = Nazwisko
        self.Imie = Imie
        self.PESEL = PESEL
        self.Data_urodzenia = datetime.strptime(Data_urodzenia, "%Y-%m-%d") #.date()

    def __str__(self):
        return f"ID pacjenta: {self.Id_pacjenta}, Nazwisko: {self.Nazwisko}, Imie: {self.Imie}, PESEL: {self.PESEL}, Data urodzenia: {self.Data_urodzenia}"


class Lekarz:
    def __init__(self, Id_lekarza, Nazwisko, Imie, Specjalnosc, Data_urodzenia, NIP, PESEL):
        self.Id_lekarza = Id_lekarza
        self.Nazwisko = Nazwisko
        self.Imie = Imie
        self.Specjalnosc = Specjalnosc.capitalize()
        self.Data_urodzenia = datetime.strptime(Data_urodzenia, "%Y-%m-%d")
        self.NIP = NIP
        self.PESEL = PESEL

    def __str__(self):
        return f"ID lekarza: {self.Id_lekarza}, Nazwisko: {self.Nazwisko}, Imię: {self.Imie}, Specjalność: {self.Specjalnosc}, Data urodzenia: {self.Data_urodzenia}, NIP: {self.NIP}, PESEL: {self.PESEL}"


def  list_objects_from_file(file_name, class_name):
    with open(file_name, 'r') as file:

        # header_line = file.readline()
        # headers = header_line.strip().split('\t')
        # pomijamy linię nagłówków
        next(file)

        list_objects = [class_name(*line.strip().split('\t')) for line in file.readlines()]
        return list_objects


wizyty = list_objects_from_file("..\data_files\wizyty.txt", Wizyta)
print(*wizyty, sep="\n")


pacjenci = list_objects_from_file("..\data_files\pacjenci.txt", Pacjent)
print(*pacjenci, sep="\n")

lekarze = list_objects_from_file("..\data_files\lekarze.txt", Lekarz)
print(*lekarze, sep="\n")