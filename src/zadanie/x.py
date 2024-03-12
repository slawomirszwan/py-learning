"""
Napisz klasę Pracownik w języku Python z atrybutami takimi jak emp_id, emp_name, emp_salary i emp_department oraz metodami takimi jakkalkuluj_emp_salary, emp_przypisz_department i print_pracownik_details.
Przykładowe dane pracownika:
„ADAMS”, „E7876”, 50000, „KSIĘGOWOŚĆ”
„JONES”, „E7499”, 45000, „BADANIA”
„MARTIN”, „E7900”, 50000, „SPRZEDAŻ”
„SMITH”, „E7698”, 55000, „OPERACJE”
Użyj metody „przypisz_department”, aby zmienić dział pracownika.
Użyj metody „print_employee_details”, aby wydrukować dane pracownika.
Użycie metody 'calculate_emp_salary' przyjmuje dwa argumenty: wynagrodzenie oraz przepracowane godziny, czyli liczbę godzin przepracowanych przez pracownika. Jeżeli liczba przepracowanych godzin jest większa niż 50, metoda nalicza nadgodziny i dolicza je do wynagrodzenia. Nadgodziny oblicza się według następującego wzoru:
nadgodziny = przepracowane godziny - 50
Wysokość nadgodzin = (nadgodziny * (wynagrodzenie / 50))
ChatGPT
Oto implementacja klasy Pracownik zgodnie z podanymi wymaganiami:

python
Copy code
"""

class Pracownik:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def przypisz_department(self, new_department):
        self.emp_department = new_department

    def kalkuluj_emp_salary(self, worked_hours):
        if worked_hours > 50:
            overtime_hours = worked_hours - 50
            overtime_pay = overtime_hours * (self.emp_salary / 50)
            return self.emp_salary + overtime_pay
        else:
            return self.emp_salary

    def print_pracownik_details(self):
        print("ID Pracownika:", self.emp_id)
        print("Imię i nazwisko:", self.emp_name)
        print("Wynagrodzenie:", self.emp_salary)
        print("Dział:", self.emp_department)


# Przykładowe dane pracowników

pracownik1 = Pracownik("ADAMS", "E7876", 50000, "KSIĘGOWOŚĆ")
pracownik2 = Pracownik("JONES", "E7499", 45000, "BADANIA")
pracownik3 = Pracownik("MARTIN", "E7900", 50000, "SPRZEDAŻ")
pracownik4 = Pracownik("SMITH", "E7698", 55000, "OPERACJE")

# Przykładowe użycie metod
pracownik1.przypisz_department("HR")
pracownik1.print_pracownik_details()
print("Wynagrodzenie pracownika 1 po uwzględnieniu nadgodzin:", pracownik1.kalkuluj_emp_salary(55))



