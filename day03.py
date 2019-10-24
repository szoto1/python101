# # # # # wiek = input("Ile masz lat?")
# # # # # koty = input("Ile masz kotów?")
# # # #
# # # # # wiek = 2
# # # # # koty = 5
# # # #
# # # # # zdanie = "Ala ma 2 lata i posiada 5 kotów."
# # # # # zdanie = "Ala ma " + str(wiek) + " lata i posiada " + str(koty) + " kotów."
# # # # # zdanie = f"Ala ma {wiek} lata i posiada {koty} kotów."
# # # # # zdanie = "Ala ma {} lata i posiada {} kotów.".format(wiek, koty)
# # # # # zdanie = "Ala ma {a} lata i posiada {b} kotów.".format(b=koty, a=wiek)
# # # # # print(zdanie)
# # # #
# # # # # liczba = 1.234
# # # # # print("liczba: %s" % liczba)        # 1.234 (string rep.)
# # # # # print("liczba: %f" % liczba)        # 1.234000 (float)
# # # # # print("liczba: %0.10f" % liczba)    # 1.2340000000 (float z precyzją)
# # # # # print("liczba: %0.1f" % liczba)     # 1.2 (float z precyzją/zaokrąlenie)
# # # # # print("liczba: %d" % liczba)        # 1 (całkowita)
# # # #
# # # # #                012345678901
# # # # # zdanie_master = "encyklopedia"
# # # # # zdanie = zdanie_master[4]       # k
# # # # # zdanie = zdanie_master[-3]      # d
# # # # # zdanie = zdanie_master[2:8]     # cyklop
# # # # # zdanie = zdanie_master[:7]      # encyklo
# # # # # zdanie = zdanie_master[8:]      # edia
# # # # # zdanie = zdanie_master[1:7:2]   # nyl
# # # # # zdanie = zdanie_master[::-1]    # aidepolkycne
# # # # # print(zdanie)
# # # #
# # # # # print("Start")
# # # # # zmienna_a = False
# # # # # if(zmienna_a):
# # # # #     print("Prawda")
# # # # # else:
# # # # #     print("Fałsz")
# # # # # print("Koniec")
# # # #
# # # # # print("Sprawdzenie parzystości liczb")
# # # # # liczba = int(input("Podaj liczbę: "))
# # # # # # liczba = 2
# # # # # if(liczba%2==0):
# # # # #     print("Liczba parzysta.")
# # # # # else:
# # # # #     print("Liczba nieparzysta.")
# # # # # print("Koniec.")
# # # #
# # # # # print("Sprawdzenie podzielnosci przez 3 i 5")
# # # # # liczba = int(input("Podaj liczbę: "))
# # # # # # liczba = 15
# # # # #
# # # # # if (liczba%3==0 and liczba%5==0):
# # # # #     print("Liczba podzielna przez 3 i przez 5")
# # # # # elif liczba%3==0:
# # # # #     print("Liczba podzielna przez 3")
# # # # # elif liczba%5==0:
# # # # #     print("Liczba podzielna przez 5")
# # # # # else:
# # # # #     print("Liczba niepodzielna przez 3 i 5")
# # # # # print("Koniec.")
# # # #
# # # # # # wyrazy = ("raz", "dwa", "trzy") # krotka == tuple - nie można edytować
# # # # # wyrazy = ["raz", "dwa", "trzy"] # list - lista, można edytować
# # # # # wyrazy[0] = "jeden"
# # # # # print(wyrazy)
# # # #
# # # # # liczby_parzyste = range(0,20,2)
# # # # # # if 10 in liczby_parzyste:
# # # # # #     print("Prawda")
# # # # # # else:
# # # # # #     print("Fałsz")
# # # # # lista_liczb_parzystych = list(liczby_parzyste)
# # # # # print((lista_liczb_parzystych))
# # # # # lista_liczb_parzystych = tuple(liczby_parzyste)
# # # # # print((lista_liczb_parzystych))
# # # #
# # # # napis = "dwa"
# # # # lista = list(napis) # ['d', 'w', 'a']
# # # # print(lista)
# # # # lista = (napis) # dwa
# # # # print(lista) # ['d', 'w', 'a']
# # #
# # # lista_zakupow = ["kiełbasa", "piwko", "chipsy", "węgiel", "kubeczki"]
# # # print(lista_zakupow)
# # # lista_zakupow.append("talerzyki")
# # # print(lista_zakupow)
# # # lista_zakupow.insert(0, "grill")
# # # print(lista_zakupow)
# # # lista_zakupow[0] = "elektryczny grill"
# # # print(lista_zakupow)
# # # lista_zakupow.remove("piwko")
# # # print(lista_zakupow)
# # # if "vodka" in lista_zakupow:
# # #     lista_zakupow.remove("vodka")
# # # else: print("Brak vodki")
# # #
# # # del(lista_zakupow[1])
# # # print(lista_zakupow)
# #
# # print("Start")
# # liczba = 1
# # while liczba < 5:
# #     print(liczba)
# #     liczba = liczba + 1
# # print("Koniec")
# #
#
# lista_liczb = [1,2,3,4]
# for liczba in lista_liczb:
#     print(liczba)
#     if liczba==2:
#         break
#
# for litera in "jakies zdanie":
#     print(litera)