import xml.etree.ElementTree as ET

tree = ET.parse('TERC_Adresowy_2024-02-28.xml')
root = tree.getroot()

# print(root)
"""
<Element 'teryt' at 0x000002452CF5B010>
"""

# print(*dir(root),sep="\n")
"""
__class__
__copy__
__deepcopy__
__delattr__
__delitem__
__dir__
__doc__
__eq__
__format__
__ge__
__getattribute__
__getitem__
__getstate__
__gt__
__hash__
__init__
__init_subclass__
__le__
__len__
__lt__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__setattr__
__setitem__
__setstate__
__sizeof__
__str__
__subclasshook__
append
attrib
clear
extend
find
findall
findtext
get
insert
items
iter
iterfind
itertext
keys
makeelement
remove
set
tag
tail
text
"""

# for child in root:
#     print(child.tag, child.attrib)
# """
# catalog {'name': 'TERC', 'type': 'ALL', 'date': '2024-01-01'}
# """


# XPath (XML Path Language)
# wyszukanie lementów
# for row in root.findall('.//catalog/row'):
#     print(row)

# ---------------------
# wojewodztwa = []
# for row in root.findall(".//catalog/row[POW='']"):
#     # print(row)
#
#     # Słownik do przechowywania danych z danego wiersza
#     row_data = {}
#     # Przejdź przez wszystkie elementy wewnątrz wiersza
#     for elem in row:
#         row_data[elem.tag] = elem.text
#     # Dodaj dane z wiersza do listy danych
#     wojewodztwa.append(row_data)
# print(*wojewodztwa, sep="\n")

"""
16 województw

{'WOJ': '02', 'POW': None, 'GMI': None, 'RODZ': None, 'NAZWA': 'DOLNOŚLĄSKIE', 'NAZWA_DOD': 'województwo', 'STAN_NA': '2024-01-01'}
{'WOJ': '04', 'POW': None, 'GMI': None, 'RODZ': None, 'NAZWA': 'KUJAWSKO-POMORSKIE', 'NAZWA_DOD': 'województwo', 'STAN_NA': '2024-01-01'}
{'WOJ': '06', 'POW': None, 'GMI': None, 'RODZ': None, 'NAZWA': 'LUBELSKIE', 'NAZWA_DOD': 'województwo', 'STAN_NA': '2024-01-01'}
{'WOJ': '08', 'POW': None, 'GMI': None, 'RODZ': None, 'NAZWA': 'LUBUSKIE', 'NAZWA_DOD': 'województwo', 'STAN_NA': '2024-01-01'}
{'WOJ': '10', 'POW': None, 'GMI': None, 'RODZ': None, 'NAZWA': 'ŁÓDZKIE', 'NAZWA_DOD': 'województwo', 'STAN_NA': '2024-01-01'}
{'WOJ': '12', 'POW': None, 'GMI': None, 'RODZ': None, 'NAZWA': 'MAŁOPOLSKIE', 'NAZWA_DOD': 'województwo', 'STAN_NA': '2024-01-01'}
{'WOJ': '14', 'POW': None, 'GMI': None, 'RODZ': None, 'NAZWA': 'MAZOWIECKIE', 'NAZWA_DOD': 'województwo', 'STAN_NA': '2024-01-01'}
{'WOJ': '16', 'POW': None, 'GMI': None, 'RODZ': None, 'NAZWA': 'OPOLSKIE', 'NAZWA_DOD': 'województwo', 'STAN_NA': '2024-01-01'}
{'WOJ': '18', 'POW': None, 'GMI': None, 'RODZ': None, 'NAZWA': 'PODKARPACKIE', 'NAZWA_DOD': 'województwo', 'STAN_NA': '2024-01-01'}
{'WOJ': '20', 'POW': None, 'GMI': None, 'RODZ': None, 'NAZWA': 'PODLASKIE', 'NAZWA_DOD': 'województwo', 'STAN_NA': '2024-01-01'}
{'WOJ': '22', 'POW': None, 'GMI': None, 'RODZ': None, 'NAZWA': 'POMORSKIE', 'NAZWA_DOD': 'województwo', 'STAN_NA': '2024-01-01'}
{'WOJ': '24', 'POW': None, 'GMI': None, 'RODZ': None, 'NAZWA': 'ŚLĄSKIE', 'NAZWA_DOD': 'województwo', 'STAN_NA': '2024-01-01'}
{'WOJ': '26', 'POW': None, 'GMI': None, 'RODZ': None, 'NAZWA': 'ŚWIĘTOKRZYSKIE', 'NAZWA_DOD': 'województwo', 'STAN_NA': '2024-01-01'}
{'WOJ': '28', 'POW': None, 'GMI': None, 'RODZ': None, 'NAZWA': 'WARMIŃSKO-MAZURSKIE', 'NAZWA_DOD': 'województwo', 'STAN_NA': '2024-01-01'}
{'WOJ': '30', 'POW': None, 'GMI': None, 'RODZ': None, 'NAZWA': 'WIELKOPOLSKIE', 'NAZWA_DOD': 'województwo', 'STAN_NA': '2024-01-01'}
{'WOJ': '32', 'POW': None, 'GMI': None, 'RODZ': None, 'NAZWA': 'ZACHODNIOPOMORSKIE', 'NAZWA_DOD': 'województwo', 'STAN_NA': '2024-01-01'}
"""
# -------------------------


# wojewodztwa = []
# for row in root.findall(".//catalog/row[NAZWA_DOD='województwo']"):
#     # print(row)
#
#     # Słownik do przechowywania danych z danego wiersza
#     row_data = {}
#     # Przejdź przez wszystkie elementy wewnątrz wiersza
#     for elem in row:
#         row_data[elem.tag] = elem.text
#     # Dodaj dane z wiersza do listy danych
#     wojewodztwa.append(row_data)
# # print(*wojewodztwa, sep="\n")


# dictionary województw

wojewodztwa_dict = {}
for row in root.findall(".//catalog/row[NAZWA_DOD='województwo']"):
    # print(row)

    # Słownik do przechowywania danych z danego wiersza
    row_data = {}
    # Przejdź przez wszystkie elementy wewnątrz wiersza
    for elem in row:
        row_data[elem.tag] = elem.text
    # Dodaj dane z wiersza do listy danych

    wojewodztwa_dict[row_data["WOJ"]] = row_data["NAZWA"]
print(wojewodztwa_dict)
"""
{'02': 'DOLNOŚLĄSKIE', '04': 'KUJAWSKO-POMORSKIE', '06': 'LUBELSKIE', '08': 'LUBUSKIE', '10': 'ŁÓDZKIE', '12': 'MAŁOPOLSKIE', '14': 'MAZOWIECKIE', '16': 'OPOLSKIE', '18': 'PODKARPACKIE', '20': 'PODLASKIE', '22': 'POMORSKIE', '24': 'ŚLĄSKIE', '26': 'ŚWIĘTOKRZYSKIE', '28': 'WARMIŃSKO-MAZURSKIE', '30': 'WIELKOPOLSKIE', '32': 'ZACHODNIOPOMORSKIE'}
"""

powiaty = []
for row in root.findall(".//catalog/row[NAZWA_DOD='powiat']"):
    # print(row)

    # Słownik do przechowywania danych z danego wiersza
    row_data = {}
    # Przejdź przez wszystkie elementy wewnątrz wiersza
    for elem in row:
        row_data[elem.tag] = elem.text
    row_data['WOJ']= wojewodztwa_dict[row_data["WOJ"]]
    # Dodaj dane z wiersza do listy danych
    powiaty.append(row_data)
print(*powiaty, sep="\n")

powiaty_dict = {}
for row in root.findall(".//catalog/row[NAZWA_DOD='powiat']"):
    # print(row)

    # Słownik do przechowywania danych z danego wiersza
    row_data = {}
    # Przejdź przez wszystkie elementy wewnątrz wiersza
    for elem in row:
        row_data[elem.tag] = elem.text
    # Dodaj dane z wiersza do listy danych
    powiaty_dict[row_data["POW"]] = row_data["NAZWA"]
print(powiaty_dict)
"""
{'01': 'białogardzki', '02': 'choszczeński', '03': 'drawski', '04': 'goleniowski', '05': 'gryficki', '06': 'gryfiński', '07': 'kamieński', '08': 'kołobrzeski', '09': 'koszaliński', '10': 'myśliborski', '11': 'policki', '12': 'pyrzycki', '13': 'sławieński', '14': 'stargardzki', '15': 'szczecinecki', '16': 'świdwiński', '17': 'wałecki', '18': 'łobeski', '19': 'pilski', '20': 'pleszewski', '21': 'poznański', '22': 'rawicki', '23': 'słupecki', '24': 'szamotulski', '25': 'średzki', '26': 'śremski', '27': 'turecki', '28': 'wągrowiecki', '29': 'wolsztyński', '30': 'wrzesiński', '32': 'warszawski zachodni', '33': 'węgrowski', '34': 'wołomiński', '35': 'wyszkowski', '36': 'zwoleński', '37': 'żuromiński', '38': 'żyrardowski', '31': 'złotowski'}
"""


"""

Aby odczytać dane z pliku XML i przekonwertować je do struktury list w języku Python, możesz użyć modułu xml.etree.ElementTree. Oto jak to zrobić:

python
Copy code
import xml.etree.ElementTree as ET

# Wczytaj plik XML
tree = ET.parse('teryt_data.xml')
root = tree.getroot()

# Lista do przechowywania danych
data_list = []

# Przejdź przez wszystkie elementy 'row' w drzewie XML
for row in root.findall('.//row'):
    # Słownik do przechowywania danych z danego wiersza
    row_data = {}
    # Przejdź przez wszystkie elementy wewnątrz wiersza
    for elem in row:
        row_data[elem.tag] = elem.text
    # Dodaj dane z wiersza do listy danych
    data_list.append(row_data)

# Wyświetl dane w strukturze listy
for item in data_list:
    print(item)
Ten kod wczytuje plik XML "teryt_data.xml", iteruje przez wszystkie elementy <row> w drzewie XML, a następnie dla każdego elementu <row> iteruje przez jego elementy potomne. Tworzy słownik row_data, który przechowuje dane dla danego wiersza, a następnie dodaje ten słownik do listy data_list. Na koniec wyświetla dane w strukturze listy.

Możesz dostosować ten kod do swoich potrzeb, jeśli chcesz przetwarzać lub wykorzystywać dane z pliku XML w inny sposób.
"""