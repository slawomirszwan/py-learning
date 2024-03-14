# from Id_iterator import Id_iterator
from next_number_generator import next_number_generator

from Zwierze import Zwierze

class RejestrZwierzat:
    def __init__(self, id_start):
        self.zwierzeta = []
        # self.ostatnie_id = 0
        # self.id_iterator = Id_iterator(id_start)
        self.id_generator = next_number_generator(id_start)

    def nadaj_kolejny_id(self):
        # return next(self.id_iterator)
        return next(self.id_generator)

    def dodaj_zwierze(self, nazwa, gatunek, data_urodzenia, waga, wzrost):
        zwierze_id = self.nadaj_kolejny_id()
        zwierze = Zwierze(zwierze_id,nazwa, gatunek, data_urodzenia, waga, wzrost)
        self.zwierzeta.append(zwierze)
        return zwierze

    def view(self):
        text = ""
        for item in self.zwierzeta:
            text += f"{item.view()} \n"
        return text

if __name__ == "__main__":
    # Przykładowe użycie:
    rejestr = RejestrZwierzat(160)

    rejestr.dodaj_zwierze("Lew", "Lew afrykański", "2008-05-15", 180, 100)
    rejestr.dodaj_zwierze("Słoń", "Słoń indyjski", "2010-10-20", 3000, 300)

    print(rejestr.view())
