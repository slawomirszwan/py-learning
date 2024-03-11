from datetime import datetime

from openpyxl import Workbook
from openpyxl.styles import PatternFill

from collections import Counter

def extract_data_from_file(filename, transform_func):
    """
    zwraca dane z pliku txt
    pierwszy wiersz kolumny
    """
    with open(filename, 'r') as file:
        header_line = file.readline()
        columns_names = header_line.split()

        data = []
        for line in file:
            values = line.split()
            row = {columns_names[i]:value for i, value in enumerate(values)}

            x= Lekarz(columns_names, values)
            print(x)
            # print(row)
            row = transform_func(row)
            data.append(row)
        return data

def transform_lekarze(row):
    """
    transformuje dane
    map do nowej postaci
    :param row:
    :return:
    """
    row["Specjalnosc"] = row["Specjalnosc"].capitalize()
    row["Data_urodzenia"] = datetime.strptime(row["Data_urodzenia"], "%Y-%m-%d")
    return row

def transform_pacjenci(row):
    row["Data_urodzenia"] = datetime.strptime(row["Data_urodzenia"], "%Y-%m-%d")
    return row

def transform_wizyty(row):
    row["Data_wizyty"] = datetime.strptime(row["Data_wizyty"], "%Y-%m-%d")
    return row


def validate_pesel(pesel):
    """
    waliduje PESEL
    :param pesel: str
    :return: True/False
    """
    if not pesel.isdigit() or len(pesel) != 11:
        return False

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    checksum = 10 - sum(int(p) * w % 10 for p, w in zip(pesel[0:-1], weights)) % 10
    # print(f'{checksum=}  {pesel[-1]}')
    return checksum == int(pesel[-1])



class Lekarz:
    def __init__(self, names: list, values:list) -> None:

        for i,value   in enumerate(values):
            self[names[i]] = value
        # print(columns_names,columns_value)
        # pass

    def __str__(self):
       print(self)

##########################################################
def main():
    lekarze = extract_data_from_file("../data_files/lekarze.txt", transform_lekarze)
    # print(*lekarze, sep="\n")

    # pacjenci = extract_data_from_file("../data_files/pacjenci.txt", transform_pacjenci)
    # # print(*pacjenci, sep="\n")
    #
    # wizyty = extract_data_from_file("../data_files/wizyty.txt", transform_wizyty)
    # # print(*wizyty, sep="\n")

if __name__ == "__main__":
    main()
