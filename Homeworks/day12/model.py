
import pickle
from Homeworks.day12 import tools

class Ksiega():

    def __init__(self):
        self.nazwa = "Ksiega Gosci"
        self.plik = "book.pkl"
        self.wpisy = []
        self.odczyt()

    def __len__(self):
        return len(self.wpisy)

    def dodajWpis(self, wpis):
        self.wpisy.append(wpis)
        self.zapisz()

    def zapisz(self):
        with open(self.plik, 'rb+') as plik_ksiegi:
            plik_ksiegi.seek(0)
            pickle.dump(self.wpisy, plik_ksiegi)

    def odczyt(self):

        try:
            plik_ksiegi = open(self.plik, 'rb+')
            self.wpisy = pickle.load(plik_ksiegi)
        except:
            plik_ksiegi = open(self.plik, 'wb+')

        plik_ksiegi.close()

class Wpis():

    def __init__(self, autor, tresc, tytul, data=tools.dzis()):
        self.autor = autor
        self.tresc = tresc
        self.tytul = tytul
        self.data = data

    def utworzWpis(self):
        pass



# wpis=Wpis(1,2,3,4)
# print(wpis.data)