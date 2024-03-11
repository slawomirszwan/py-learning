from datetime import datetime

class Appointment:
    def __init__(self, doctor_id, patient_id, appointment_date):
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d") #.date()

    def __str__(self):
        return f"Doctor ID: {self.doctor_id}, Patient ID: {self.patient_id}, Appointment Date: {self.appointment_date}"

appointments = []

# Otwórz plik tekstowy do odczytu
with open('..\data_files\wizyty.txt', 'r') as file:
    # Pomijamy nagłówek, zakładając, że pierwsza linia zawiera nagłówek
    # next(file)

    header_line = file.readline()
    headers = header_line.strip().split('\t')
    # print(headers)

    # Odczytujemy pozostałe linie pliku
    for line in file:
        # Rozdzielamy linię na kolumny
        data = line.strip().split('\t')

        # Tworzymy obiekt Appointment na podstawie danych
        appointment = Appointment(data[0], data[1], data[2])

        # Dodajemy obiekt do listy appointments
        appointments.append(appointment)

# Wyświetlamy listę obiektów
for appointment in appointments:
    print(appointment)