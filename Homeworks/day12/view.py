
def menu():
    print("Witaj w programie. Wybierz opcję: ")
    print("1 - Dodaj wpis")
    print("2 - Wyświetl wpisy")

def blad():
    print("Wystapil blad. Papa")

def pokazRozmiar(rozmiar):
    print("Rozmiar: ", str(rozmiar))

def pokazBrakWpisow():
    print("Brak wpisów w księdze gości.")

def wyswietlWpisy(wpisy):
    for numer_wpisu, wpis in enumerate(wpisy,1):
        print("#" * 50)
        print("Wpis nr: " + str(numer_wpisu) + "\nAutor: " + wpis.autor + "\nTresc: " + wpis.tresc + "\nTytul: " + wpis.tytul + "\nData: " + wpis.data)
        print("Tresc: " + wpis.tresci())
        print("Tresc skrocona (2 znaki): " + wpis.tresci(2))
        print("#" * 50)

