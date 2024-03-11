
from datetime import datetime

def extract_data_from_file(filename, transform_func):
    """
    zwraca dane z pliku txt
    pierwszy wiersz kolumny
    """
    with open(filename, 'r') as file:
        header_line = file.readline()
        column_names = header_line.split()
        # print(f"{column_names=}")

        data = []
        for line in file:
            values = line.split()
            row = {column_names[i]:v for i, v in enumerate(values)}
            row = transform_func(row)
            data.append(row)
        return data

def transform_lekarze(row):
    row["Specjalnosc"] = row["Specjalnosc"].capitalize()
    row["Data_urodzenia"] = datetime.strptime(row["Data_urodzenia"], "%Y-%m-%d")
    return row

def transform_pacjenci(row):
    row["Data_urodzenia"] = datetime.strptime(row["Data_urodzenia"], "%Y-%m-%d")
    return row

def transform_wizyty(row):
    row["Data_wizyty"] = datetime.strptime(row["Data_wizyty"], "%Y-%m-%d")
    return row

def group_by(data, key_func):
    groups_dict = {}
    for row in data:
        # grouping key
        key = key_func(row)
        #actual group or []
        group = groups_dict.get(key, [])
        #new group
        group.append(row)
        groups_dict[key] = group
    return groups_dict


##########################################################
def main():
    lekarze = extract_data_from_file("../data_files/lekarze.txt", transform_lekarze)
    # print(*lekarze, sep="\n")

    pacjenci = extract_data_from_file("../data_files/pacjenci.txt", transform_pacjenci)
    # print(*pacjenci, sep="\n")

    wizyty = extract_data_from_file("../data_files/wizyty.txt", transform_wizyty)
    # print(*wizyty, sep="\n")

    # x= lookup(lekarze, "Id_lekarza")
    # # print(x)

    y = group_by(pacjenci, lambda row: row["Imie"])
    # lista imion
    # print(*y)

    #lista imion posortowana
    # print(sorted(y.keys()))

    # print(y)

    # ilu pacjentów ma na imie Ilona
    # print(len(y["Ilona"]))


    # lookup_lekarze = lookup(lekarze, lambda row: row["Id_lekarza"])
    #
    # print(lookup_lekarze)



    group_by_primary_id = group_by(pacjenci, lambda row: row["Id_pacjenta"])
    # print(group_by_primary_id)


    # def look_id_pacjenci(id):
    #     x = group_by_primary_id.get(id, None)
    #     if x == None:
    #         return x
    #     elif len(x)>0:
    #         return x[0]
    #     else return None
    #
    # x= look_id_pacjenci(('100')
    # if len
    # print(lookup1['100'][0])
    #

if __name__ == "__main__":
    main()