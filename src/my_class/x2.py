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
    def __init__(self, patient_id, last_name, first_name, pesel, birth_date):
        self.patient_id = patient_id
        self.last_name = last_name
        self.first_name = first_name
        self.pesel = pesel
        self.birth_date = birth_date

    def __str__(self):
        return f"Patient ID: {self.patient_id}, Last Name: {self.last_name}, First Name: {self.first_name}, PESEL: {self.pesel}, Birth Date: {self.birth_date}"



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