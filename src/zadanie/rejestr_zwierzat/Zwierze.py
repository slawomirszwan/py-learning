
kot_symbol = "🐱"

class Zwierze:

    def __init__(self, zwierze_id, nazwa, gatunek, data_urodzenia, waga, wzrost):
        self.zwierze_id = zwierze_id
        self.nazwa = nazwa
        self.gatunek = gatunek
        self.data_urodzenia = data_urodzenia
        self.waga = waga
        self.wzrost = wzrost

    def view(self):
        zwierze_id, nazwa, gatunek, data_urodzenia, waga, wzrost = self.zwierze_id, self.nazwa, self.gatunek, self.data_urodzenia, self.waga, self.wzrost
        return f"{zwierze_id=} {kot_symbol} {gatunek=} {nazwa=} {data_urodzenia=} {waga=} {wzrost=}"


if __name__ == "__main__":

    # Przykładowe użycie:
    zwierze1 = Zwierze(1, "Lew", "Lew afrykański", "2008-05-15", 180, 100)
    zwierze2 = Zwierze(2, "Słoń", "Słoń indyjski", "2010-10-20", 3000, 300)

    """
    🐶 - Pies
    🐱 - Kot
    🐭 - Mysz
    🐰 - Królik
    🐻 - Niedźwiedź
    🦊 - Lis
    🐯 - Tygrys
    🐼 - Panda
    🦁 - Lew
    🐨 - Koala
    """