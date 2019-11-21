
class Zwierze():

    def __init__(self):
        self.oczy = 2
        self.wlosy = True

    def __str__(self):
        return 'Oczy: {}, wlosy: {}'.format(self.oczy, self.wlosy)


class Czlowiek(Zwierze):

    def dajglos(self):
        print("Hello jestem człowiek")

class Lysy(Czlowiek):

    def __init__(self):
        super().__init__() #init for the upper class constructor to have access to variables/methods from upper class
        self.wlosy = False

    def dajglos(self):
        print("Masz jakis problem?")

class Student(Czlowiek):

    def dajglos(self):
        print("Siema jestem student")

class Kot(Zwierze):

     def dajglos(self):
         print("Miau")

class Pies(Zwierze):

    def dajglos(self):
        print("Hau Hau")

class Bokser(Pies):
    pass

class Jamnik(Pies):
    pass

zwierze = Zwierze()
czlowiek = Czlowiek()
pies = Pies()
kot = Kot()
jamnik = Jamnik()
bokser = Bokser()
student = Student()
lysy = Lysy()
# student.dajglos()
#print(bokser.oczy)

lysy.dajglos()

print(lysy)