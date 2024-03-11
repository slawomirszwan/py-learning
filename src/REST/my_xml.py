import xml.etree.ElementTree as ET



"""
import xml.etree.ElementTree as ET

# Tworzymy główny element XML - teryt
teryt = ET.Element('teryt')

# Tworzymy podkatalog TERC
catalog_terc = ET.SubElement(teryt, 'catalog')
catalog_terc.set('name', 'TERC')
catalog_terc.set('type', 'ALL')
catalog_terc.set('date', '2024-01-01')

# Tworzymy kolejne wiersze dla poszczególnych danych
data_rows = [
    {'WOJ': '02', 'POW': '', 'GMI': '', 'RODZ': '', 'NAZWA': 'DOLNOŚLĄSKIE', 'NAZWA_DOD': 'województwo', 'STAN_NA': '2024-01-01'},
    {'WOJ': '02', 'POW': '01', 'GMI': '', 'RODZ': '', 'NAZWA': 'bolesławiecki', 'NAZWA_DOD': 'powiat', 'STAN_NA': '2024-01-01'},
    {'WOJ': '02', 'POW': '01', 'GMI': '01', 'RODZ': '1', 'NAZWA': 'Bolesławiec', 'NAZWA_DOD': 'gmina miejska', 'STAN_NA': '2024-01-01'},
    {'WOJ': '02', 'POW': '01', 'GMI': '02', 'RODZ': '2', 'NAZWA': 'Bolesławiec', 'NAZWA_DOD': 'gmina wiejska', 'STAN_NA': '2024-01-01'},
    {'WOJ': '02', 'POW': '01', 'GMI': '03', 'RODZ': '2', 'NAZWA': 'Gromadka', 'NAZWA_DOD': 'gmina wiejska', 'STAN_NA': '2024-01-01'}
]

# Tworzymy wiersze dla każdego elementu w data_rows
for data_row in data_rows:
    row = ET.SubElement(catalog_terc, 'row')
    for key, value in data_row.items():
        child = ET.SubElement(row, key)
        child.text = value

# Tworzymy drzewo XML
xml_tree = ET.ElementTree(teryt)

# Zapisujemy drzewo XML do pliku
xml_tree.write('teryt_data.xml', encoding='utf-8', xml_declaration=True)
Ten kod tworzy strukturę XML zgodną z podanymi danymi i zapisuje ją do pliku o nazwie teryt_data.xml w bieżącym katalogu. Każdy wiersz danych jest reprezentowany jako element <row>, a poszczególne pola danych są reprezentowane jako elementy wewnątrz wiersza.


"""