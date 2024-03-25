from pprint import pprint

class Kosmita:
    def __init__(self, galaktyka = "Milky Way"):
        self.galaktyka = galaktyka


class Ziemianin(Kosmita):
    def __init__(self, gwiazda = "Słońce" ):


        super().__init__()
        self.gwiazda = gwiazda


x = Ziemianin()

print(x.gwiazda, x.galaktyka)
