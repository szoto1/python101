import Homeworks.day12.model as model
import Homeworks.day12.view as View

View.menu()

opcja = int(input("Moj wybor: "))

if opcja == 1:

    autor = input("Jak masz na imię: ")
    tresc = input("Podaj tresc: ")
    tytul = input("Podaj tytul: ")

    wpis = model.Wpis(autor,tresc,tytul)
    ksiega = model.Ksiega()

    ksiega.dodajWpis(wpis)
    View.pokazRozmiar(len(ksiega))
elif opcja == 2:

    ksiega = model.Ksiega()
    if len(ksiega)==0:
        View.pokazBrakWpisow()
    else:
        View.wyswietlWpisy(ksiega.wpisy)

else:
    View.blad()
