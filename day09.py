class Stol():
    def __init__(self):
        self.ilosc_nog = 4

    def __add__(self, other):
        return self.ilosc_nog + other.ilosc_nog

class Krzeslo():
    def __init__(self, kolor_siedziska = "czerwony", cena = 100):
        self.kolor_siedziska = kolor_siedziska
        self.ilosc_kol = 5
        self.ilosc_nog = 5
        self.wysokosc = 90
        self.szerokosc = 40
        self.glebokosc = 40
        self.regulacja_wyskosci = True
        self.regulacja_podlokietnikow = False
        self.material = '100% cotton'
        self.cena = cena
        self.vat = 23

    def __str__(self):
        return f'Krzesło koloru: {self.kolor_siedziska}'

    def __len__(self):
        return self.wysokosc * self.szerokosc * self.glebokosc

    def pobierz_cene_netto(self):
        return self.cena

    def pobierz_cene_brutto(self):
        return self.cena * (1 + self.vat/100)

# obiekt = Krzeslo()
# print(obiekt)
# print(obiekt.kolor_siedziska)

# obiekt = Krzeslo('niebieski')
# print(obiekt)
# print(obiekt.kolor_siedziska)
# print(len(obiekt)) #new __len__ will be used from class

# obiekt = Krzeslo('niebieski', 120)
# print(obiekt.pobierz_cene_netto())
# print(obiekt.pobierz_cene_brutto())

krzeslo = Krzeslo() #creating, initializing object from class Krzeslo()
# print(krzeslo)
stol = Stol()
# print(stol)
print(stol+krzeslo) #this will trigger new method in class stol because + is __add__ method which we created in Stol class
print(isinstance(krzeslo,Krzeslo)) #checking if out object is an instance of a class isinstace(object, class)