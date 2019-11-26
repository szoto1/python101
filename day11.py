import datetime

class Pizza():
    """
    Cos o tej klasie.
    """
    stawka_vat = 23 #pole klasy (poza konstruktorem, poprostu na poziomie klasy)
    __marza = 1.05 #prywatne pole (dwa podkreslniki z przodu)
    """
    # metoda prywatna też zaczyna się jej nazwa od dwóch podkreślników
    """


    def __init__(self, skladnik_glowny):
        self.skladnik_glowny = skladnik_glowny
        self.rozmiar_cm = 30
        self.ciasto = "cienkie"
        self.cena = 23 * self.__marza

    #Metody klasy (tworzą instancję klasy i mogą odwoływać się do danych/metod obiektu)
    @classmethod
    def Hawajska(cls):
        return cls("ananas")

    @classmethod
    def podaj_stawke_vat(cls):
        return cls.stawka_vat

    #Metody statyczne (nie wymagaja tworzenia instancji klasy, nie są związane ani z obiektem ani z klasą)
    @staticmethod
    def podaj_date():
        return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    #getter / setter / deleter
    @property
    def marza(self):
        if self.__marza>=1.05:
            return "Duzo"
        else:
            return "Malo"
#
# hawajska = Pizza("ananas")
# print(hawajska.skladnik_glowny)
#
# hawajska2 = Pizza.Hawajska()
# print(hawajska2.skladnik_glowny)
#
# print(Pizza.podaj_stawke_vat())
# print(Pizza.stawka_vat)
#
# print(Pizza.podaj_date())
#
# print(hawajska.cena)
# print(Pizza.__dict__)
#
# import pprint
# pprint.pprint(Pizza.__dict__)
#
# print(Pizza._Pizza__marza)
#
# print(hawajska.marza)
# # print(Pizza.marza())



"""
getery, setery, deletery
"""

class Student():

    def __init__(self):
        self.__imie = None
        self.nazwisko = None
        self.data_dodania = None
        self.data_usuniecia = None
        self.skasowany = False

    @property #geter (ustawiamy na danych prywatnych)
    def imie(self):
        return self.__imie.capitalize()

    @imie.setter
    def imie(self, wartosc):
        self.__imie = wartosc

    @imie.deleter
    def imie(self):
        self.skasowany = True
        self.data_usuniecia = self.pobierz_date()

    @staticmethod
    def pobierz_date():
        return datetime.datetime.now().strftime('%Y-%m-%d')

# student = Student()
# student.imie = "lukasz"
# student.nazwisko = "anonim"
# student.data_dodania = student.pobierz_date()
#
# print(student.imie)
# print(student.nazwisko)
# print(student.data_dodania)
# print(student.data_usuniecia)
# print(student.skasowany)
# del(student.imie)
# print(student.data_usuniecia)
# print(student.skasowany)

