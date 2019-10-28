print("Praca domowa - Day03")
programs_list = list(range(1,11))
program_choice = ''
program_choice_decimal_or_not = False
while program_choice_decimal_or_not==False:
    print("Wybierz który program uruchomić podając liczbę od 1-10 gdzie: ")
    print("     -  1 - Przeliczanie stopni w skali Celcjusza i Fahrenheita")
    print("     -  2 - Podawanie pierwszej i ostatniej cyfry wprowadzonej liczby")
    print("     -  3 - Rysowanie prostokątu o zadanych rozmiarach")
    print("     -  4 - Przeliczanie liczby zapisanej w formacie binarnym na system dziesiętny")
    print("     -  5 - Czy podany rok jest rokiem przestępnym?")
    print("     -  6 - Program do rysowania list (z wykorzystaniem tabulate)")
    print("     -  7 - Podaj kwotę - rozmienię to na najmniejszą ilość monet.")
    print("     -  8 - Rysowanie piramidy o zadaniej wielkości")
    print("     -  9 - Kalkulator wieku psa")
    print("     - 10 - 24h temperatur")
    program_choice = input("Twój wybór: ")
    program_choice_decimal_or_not=program_choice.isdecimal()
    if program_choice_decimal_or_not==False or (program_choice_decimal_or_not==True and int(program_choice)>10):
        print("Wprowadzono błędą wartość: '"+program_choice+"'")
        print("By spróbować ponownie wciśnij: T/t")
        print("By zakończyć program wciśnij inny klawisz niż: T/t")
        if(input("Kontynuować? ").upper()=="T"):
            print("Wybrałeś by kontynuować. Zaczynamy ponownie...")
            program_choice_decimal_or_not=False
        else:
            print("Nie chciałeś próbować ponownie. Koniec programu.")
            exit()
    else:

        print("Poprawnie dokonano wyboru. Podałeś: " +program_choice)

        if int(program_choice)==1:
            program_title = "Program do przeliczania stopni ze skal Celcjusza i Fahrenheita."
            print("-" * len(program_title))
            print(program_title)
            print("-" * len(program_title))

            user_choice = ""
            scale_list = ("C","F")
            while user_choice.upper not in scale_list:
                print("Chcesz przeliczyć: ")
                print(" - stopnie Celcjusza na stopnie Fahrenheita wciśnij C")
                print(" - stopnie Fahrenheita na stopnie Celcjusza wciśnij F")
                user_choice = input("Twój wybór: \n")
                if user_choice.upper() in scale_list:
                    break
                else:
                    print("Został wprowadzony błędny znak: " + user_choice)
                    print("By spróbować ponownie wciśnij: T/t")
                    print("By zakończyć program wciśnij inny klawisz niż: T/t")
                    if(input("Kontynuować? ").upper()=="T"):
                        print("Wybrałeś by kontynuować. Zaczynamy ponownie...")
                        continue
                    else:
                        print("Nie chciałeś próbować ponownie. Koniec programu.")
                        exit()

            print("Poprawnie dokonano wyboru. Podałeś: " +user_choice)
            degrees_to_be_calculated = 0.00
            if user_choice.upper()=='C':
                print("Wybrałeś przeliczenie skali Celcjusza na Fahranhaita.")

                user_degrees_input_finished = False
                while user_degrees_input_finished == False:
                    user_degrees_input = input("Podaj temperaturę w Celcjuszach (wprowadź tylko cyfry): ")
                    try:
                        user_degrees = float(user_degrees_input)
                    except:
                        print("Podano błędną wartość: '"+user_degrees_input+"', spróbuj raz jeszcze.")
                        continue
                    user_degrees_input_finished = True

                print("Podano temperaturę: "+str(user_degrees_input)+" stopni w skali Celcjusza")
                print("Przeliczam na skalę Fahrenheita")
                user_degrees_calculated = round((user_degrees*9/5)+32,10)
                print("Przeliczono wg wzoru:")
                print("32+([Podana wartość stopni w Celcjuszach] *9/5) = " + str(user_degrees_calculated))
                print("Wynik końcowy:")
                print(str(user_degrees)+" stopni Celcjusza to: "+str(user_degrees_calculated)+" stopni Fahrenheita.")
            else:
                print("Wybrałeś przeliczenie skali Fahranhaita na Celcjusza.")

                user_degrees_input_finished = False
                while user_degrees_input_finished == False:
                    user_degrees_input = input("Podaj temperaturę w Fahranhaitach (wprowadź tylko cyfry): ")
                    try:
                        user_degrees = float(user_degrees_input)
                    except:
                        print("Podano błędną wartość: "+user_degrees_input+", spróbuj raz jeszcze.")
                        continue
                    user_degrees_input_finished = True

                print("Podano temperaturę: "+str(user_degrees_input)+" stopni w skali Fahranhaita")
                print("Przeliczam na skalę Celcjusza")
                user_degrees_calculated = round((user_degrees-32)*5/9,10)
                print("Przeliczono wg wzoru:")
                print("([Podana wartość stopni w Fahranhaitach]-32)*9/5) = " + str(user_degrees_calculated))
                print("Wynik końcowy:")
                print(str(user_degrees)+" stopni Fahranhaita to: "+str(user_degrees_calculated)+" stopni Celcjusza.")
        elif int(program_choice) == 2:
            program_title = "Program do podawania pierwszej i ostatniej cyfry podanej liczby"
            print("-" * len(program_title))
            print(program_title)
            print("-" * len(program_title))
            user_input_decimal_or_not=False

            while user_input_decimal_or_not==False:
                user_input_string = input("Podaj liczbę abym mógł zwrócić jej pierwszą i ostatnią cyfrę: ")
                user_input_decimal_or_not=user_input_string.lstrip('-+').isnumeric()
                if user_input_decimal_or_not==False:
                    print("Wprowadzono błędą wartość: '"+user_input_string+"'")
                    print("By spróbować ponownie wciśnij: T/t")
                    print("By zakończyć program wciśnij inny klawisz niż: T/t")
                    if(input("Kontynuować? ").upper()=="T"):
                        print("Wybrałeś by kontynuować. Zaczynamy ponownie...")
                        user_input_decimal_or_not=False
                    else:
                        print("Nie chciałeś próbować ponownie. Koniec programu.")
                        exit()
            print("Podano poprawnie liczbę: "+user_input_string)
            if int(user_input_string)>9 or int(user_input_string)<-9:
                print("Podano: "+user_input_string)
                print("Pierwsza cyfra to: " +user_input_string.lstrip('-')[0]+ ", druga cyfra to: "+user_input_string.lstrip('-')[-1])
            else:
                print("Podano tylko jedną cyfrę. Pierwsza i ostatnia cyfra to zatem: "+user_input_string.lstrip("-"))

            program_title = "Koniec programu do podawania pierwszej i ostatniej cyfry podanej liczby."
            print("-" * len(program_title))
            print(program_title)
            print("-" * len(program_title))

        elif int(program_choice) == 3:

            program_title = "Program do rysowania prostokątu"
            print("-" * len(program_title))
            print(program_title)
            print("-" * len(program_title))
            length_input_numeric_or_not=False
            width_input_numeric_or_not=False
            while width_input_numeric_or_not==False or length_input_numeric_or_not==False:
                length_input_string=input("Podaj długość prostokąta (musi być większa niż 1): ")
                length_input_numeric_or_not=length_input_string.isnumeric()
                if length_input_numeric_or_not==False or (length_input_numeric_or_not==True and int(length_input_string)<=1):
                    print("Wprowadzono błędą wartość: '"+length_input_string+"'")
                    print("By spróbować ponownie wciśnij: T/t")
                    print("By zakończyć program wciśnij inny klawisz niż: T/t")
                    if(input("Kontynuować? ").upper()=="T"):
                        print("Wybrałeś by kontynuować. Zaczynamy ponownie...")
                        length_input_numeric_or_not=False
                        continue
                    else:
                        print("Nie chciałeś próbować ponownie. Koniec programu.")
                        exit()

                width_input_string=input("Podaj szerokość prostokąta (musi być większa niż 1): ")
                width_input_numeric_or_not=width_input_string.isnumeric()
                if width_input_numeric_or_not==False or (width_input_numeric_or_not==True and int(width_input_string)<=1):
                    print("Wprowadzono błędą wartość: '"+width_input_string+"'")
                    print("By spróbować ponownie wciśnij: T/t")
                    print("By zakończyć program wciśnij inny klawisz niż: T/t")
                    if(input("Kontynuować? ").upper()=="T"):
                        print("Wybrałeś by kontynuować. Zaczynamy ponownie...")
                        width_input_numeric_or_not=False
                    else:
                        print("Nie chciałeś próbować ponownie. Koniec programu.")
                        exit()
            print("Podano poprawnie długość: "+length_input_string)
            print("Podano poprawnie szerokość: "+width_input_string)

            length = int(length_input_string)
            width = int(width_input_string)
            print("+" + "-" * (length - 2) + "+")
            inside_box = 1
            while inside_box < (width-1):
                print("|" + " " * (length - 2) + "|")
                inside_box=inside_box+1
            print("+" + "-" * (length - 2) + "+")


            program_title = "Koniec programu do rysowania prostokątu"
            print("-" * len(program_title))
            print(program_title)
            print("-" * len(program_title))

        elif int(program_choice) == 4:
            program_title = "Program do przeliczania liczby zapisanej w formacie binarnym na dziesiętny"
            print("-" * len(program_title))
            print(program_title)
            print("-" * len(program_title))

            binary_input_numeric_or_not = False
            while binary_input_numeric_or_not == False:
                binary_input_string = input("Podaj zapis binarny liczby: ")
                binary_input_numeric_or_not = binary_input_string.isnumeric()
                if binary_input_numeric_or_not == False:
                    print("Wprowadzono błędą wartość: '" + binary_input_string + "'")
                    print("By spróbować ponownie wciśnij: T/t")
                    print("By zakończyć program wciśnij inny klawisz niż: T/t")
                    if (input("Kontynuować? ").upper() == "T"):
                        print("Wybrałeś by kontynuować. Zaczynamy ponownie...")
                        binary_input_numeric_or_not = False
                    else:
                        print("Nie chciałeś próbować ponownie. Koniec programu.")
                        exit()
            print("Podano poprawnie liczbę binarnie: " + binary_input_string)
            print("Liczba ta zamieniona na dziesiętny to: "+str(int(binary_input_string,2)))

            program_title = "Koniec programu do przeliczania liczby zapisanej w formacie binarnym na dziesiętny"
            print("-" * len(program_title))
            print(program_title)
            print("-" * len(program_title))

        elif int(program_choice) == 5:
            program_title = "Program do sprawdzania roku przestępnego"
            print("-" * len(program_title))
            print(program_title)
            print("-" * len(program_title))

            year_input_numeric_or_not = False
            while year_input_numeric_or_not == False:
                year_input_string = input("Podaj rok: ")
                year_input_numeric_or_not = year_input_string.isnumeric()
                if year_input_numeric_or_not == False:
                    print("Wprowadzono błędą wartość: '" + year_input_string + "'")
                    print("By spróbować ponownie wciśnij: T/t")
                    print("By zakończyć program wciśnij inny klawisz niż: T/t")
                    if (input("Kontynuować? ").upper() == "T"):
                        print("Wybrałeś by kontynuować. Zaczynamy ponownie...")
                        year_input_numeric_or_not = False
                    else:
                        print("Nie chciałeś próbować ponownie. Koniec programu.")
                        exit()
            print("Podano poprawnie rok: " + year_input_string)

            year = int(year_input_string)
            if year in list(range(0,year+1,4)):
                print("Rok "+year_input_string+" to rok przestępny.")
            else:
                print("Rok " + year_input_string + " nie jest rokiem przestępnym.")

            program_title = "Koniec programu sprawdzania roku przestępnego."
            print("-" * len(program_title))
            print(program_title)
            print("-" * len(program_title))

        elif int(program_choice) == 6:

            program6_choice = False
            while program6_choice == False:

                def string_list_audit(string_input):
                    start_count = string_input.count("[")
                    end_count = string_input.count("]")
                    start_char = string_input[0]
                    end_char = string_input[-1]

                    count = False
                    char = False

                    if start_count == end_count:
                        count = True

                    if start_char == '[' and end_char == "]":
                        char = True

                    return count, char


                def create_list_from_input_string(input_string):
                    created_list = []
                    string_to_analyzed = (input_string[1:-1]).replace("'", "")
                    while len(string_to_analyzed) > 0:
                        if string_to_analyzed.find("[") >= 0:
                            inlist_count = string_to_analyzed.count("[")
                            counter = 0
                            while counter < inlist_count:
                                if string_to_analyzed.find("[") > 0:
                                    string_insert = (string_to_analyzed[:string_to_analyzed.find("[")]).replace(",", "")
                                    string_insert_len = len(string_insert.split())
                                    string_insert_counter = 0
                                    while string_insert_counter < string_insert_len:
                                        created_list.insert(len(created_list), string_insert.split()[string_insert_counter])
                                        string_insert_counter = string_insert_counter + 1
                                    string_to_analyzed = string_to_analyzed[string_to_analyzed.find("["):]
                                    counter = counter + 1
                                else:  # ("[")=0
                                    inlist_start = string_to_analyzed.find("[")
                                    inlist_start_check = inlist_start
                                    inlist_end = string_to_analyzed[inlist_start:].find("]")
                                    finish = False
                                    while finish == False:
                                        if string_to_analyzed[inlist_start_check:inlist_end + 1].find("[") > 0:
                                            inlist_start_check = inlist_end
                                            inlist_end = string_to_analyzed[inlist_start_check:].find("]")
                                            finish = False
                                        else:
                                            finish = True
                                    new_inlist_string = string_to_analyzed[inlist_start:inlist_end + 2]
                                    if new_inlist_string[-1]==",":
                                        new_inlist_string=new_inlist_string[0:-1]

                                    new_inlist = create_list_from_input_string(new_inlist_string)
                                    list_to_insert = []
                                    list_to_insert.insert(0, new_inlist)
                                    created_list.insert(len(created_list), tabulate(list_to_insert, tablefmt="psql"))

                                    string_to_analyzed = string_to_analyzed[inlist_end + 2:]
                                    if len(string_to_analyzed) == 0:
                                        # finish = True
                                        break
                                    counter = counter + 1
                        else:
                            new_list_split = (string_to_analyzed.replace(",", "")).split()
                            counter_split = 0
                            while counter_split < len(new_list_split):
                                created_list.insert(len(created_list), new_list_split[counter_split])
                                counter_split = counter_split + 1
                            string_to_analyzed = ""

                    return created_list

                from tabulate import tabulate
                tabulate.PRESERVE_WHITESPACE = True

                program_title = "Program do rysowania list."
                print("-" * len(program_title))
                print(program_title)
                print("-" * len(program_title))

                print("Witaj. Przygotowałem kilka przykładowych zestawów danych z których możesz wybrać wykonanie programu.")
                dane1 = "['col1', 'col2', 'col3']"
                dane2 = "['col1', 'col2', 'col3', ['col4', 'col5', 'col6']]"
                dane3 = "[['col1', 'col2'], 'col3', ['col4', 'col5']]"
                dane4 = "['col1', 'col2', 'col3', ['col4', 'col5', ['col6', 'col7']]]"

                choice_list = list(range(1, 6))
                user_choice = ''
                user_choice_digit_or_not = False
                while user_choice_digit_or_not == False:
                    print("Wybierz jedną z opcji wciskając 1, 2, 3, 4 lub 5: ")
                    print("-   1 - wykonanie programu z listą: " + dane1)
                    print("-   2 - wykonanie programu z listą: " + dane2)
                    print("-   3 - wykonanie programu z listą: " + dane3)
                    print("-   4 - wykonanie programu z listą: " + dane4)
                    print("-   5 - wprowadź listę samemu.")
                    user_choice = input("Twój wybór: ")
                    user_choice_digit_or_not = user_choice.isdigit()
                    if user_choice_digit_or_not == False or (
                            user_choice_digit_or_not == True and int(user_choice) not in choice_list):
                        print("Wprowadzono błędą wartość: '" + user_choice + "'")
                        print("By spróbować ponownie wciśnij: T/t")
                        print("By zakończyć program wciśnij inny klawisz niż: T/t")
                        if (input("Kontynuować? ").upper() == "T"):
                            print("Wybrałeś by kontynuować. Zaczynamy ponownie...")
                            user_choice_digit_or_not = False
                        else:
                            print("Nie chciałeś próbować ponownie. Koniec programu.")
                            exit()

                if int(user_choice) == 1:
                    dane = dane1
                elif int(user_choice) == 2:
                    dane = dane2
                elif int(user_choice) == 3:
                    dane = dane3
                elif int(user_choice) == 4:
                    dane = dane4
                else:
                    dane = input("Wpisz swoją listę: ")

                string_list = dane
                audit_count, audit_char = string_list_audit(string_list)
                if audit_count == False or audit_char == False:
                    print("Błędna lista")
                    break
                else:
                    string_list=string_list.replace(", ",",")
                    string_list=string_list.replace(",",", ")

                new_list = create_list_from_input_string(string_list)
                list_to_output = []
                list_to_output.insert(0, new_list)

                print("Podana do narysowania lista to: ")
                print(string_list)
                print("a tak wygląda po narysowaniu:")
                print(tabulate(list_to_output, tablefmt="psql"))

                program_title = "Koniec programu do rysowania list."
                print("-" * len(program_title))
                print(program_title)
                print("-" * len(program_title))

                print("Chcesz ponownie wybrać jedną z list lub podać swoją: T/t")
                print("By zakończyć program wciśnij inny klawisz niż: T/t")
                if (input("Kontynuować? ").upper() == "T"):
                    print("Wybrałeś by kontynuować. Zaczynamy ponownie...")
                    program6_choice = False
                else:
                    print("Nie chciałeś próbować ponownie. Koniec programu rysowania list.")
                    program6_choice = True

        elif int(program_choice) == 7:
            program_title = "Program do rozmieniania."
            program_title = "Rozmienię na monety: 5, 2, 1, 0.5, 0.2, 0.1 wydając ich jak najmniej."
            print("-" * len(program_title))
            print(program_title)
            print("-" * len(program_title))

            user_money_input_finished = False
            while user_money_input_finished == False:
                user_money_input = input("Podaj kwotę do rozmienienia: ")
                try:
                    user_money = float(user_money_input)
                except:
                    print("Podano błędną kwotę: '" + user_money_input + "', spróbuj raz jeszcze.")
                    continue
                user_money_input_finished = True

            value_5 = 0
            value_2 = 0
            value_1 = 0
            value_0_5 = 0
            value_0_2 = 0
            value_low = 0
            user_money_org = user_money
            no_round_problem = False
            user_money_rounder = 0.0
            while no_round_problem == False:
                user_money_rounder = round(user_money, 1)  # 14.9
                if user_money_rounder - user_money > 0:
                    user_money = user_money - (user_money_rounder - user_money)
                    no_round_problem = False
                else:
                    no_round_problem = True

            value_5 = round((user_money-round(user_money%5,2))/5)
            user_money = user_money-5*value_5
            print("Sprawdzam monety o wartości 5. Będzie ich: "+ str(value_5))
            value_2 = round((user_money-round(user_money%2,2))/2)
            user_money = user_money-2*value_2
            print("Sprawdzam monety o wartości 2. Będzie ich: "+ str(value_2))
            value_1 = round((user_money-round(user_money%1,2))/1)
            user_money = user_money-1*value_1
            print("Sprawdzam monety o wartości 1. Będzie ich: "+ str(value_1))
            value_0_5 = round((user_money-round(user_money%0.5,2))/0.5)
            user_money = user_money-0.5*value_0_5
            print("Sprawdzam monety o wartości 0.5. Będzie ich: "+ str(value_0_5))
            value_0_2 = round((user_money-round(user_money%0.2,2))/0.2)
            user_money = user_money-0.2*value_0_2
            print("Sprawdzam monety o wartości 0.2. Będzie ich: "+ str(value_0_2))
            value_low = round((user_money-round(user_money%0.1,2))/0.1)
            user_money = user_money-0.1*value_low
            print("Sprawdzam monety o wartości 0.1. Będzie ich: "+ str(value_low))

            user_money_left = round(user_money_org-(value_5*5)-(value_2*2)-(value_1*1)-(value_0_5*0.5)-(value_0_2*0.2)-(value_low*0.1),2)
            if user_money_left!=0:
                print("Pozostanie kwota niemożliwa do rozłożenia na monety: "+str(user_money_left))

            program_title = "Koniec programu do rozmieniania na monety"
            print("-" * len(program_title))
            print(program_title)
            print("-" * len(program_title))
        elif int(program_choice) == 8:
            program_title = "Program do rysowania piramidy"
            print("-" * len(program_title))
            print(program_title)
            print("-" * len(program_title))

            pyramid_input_numeric_or_not = False
            while pyramid_input_numeric_or_not == False:
                pyramid_input_string = input("Podaj wielkość piramidy (możliwe tylko liczby całkowite większe niż 1): ")
                pyramid_input_numeric_or_not = pyramid_input_string.isnumeric()
                if (pyramid_input_numeric_or_not == False) or (pyramid_input_numeric_or_not==True and int(pyramid_input_string)<=1):
                    print("Wprowadzono błędą wartość: '" + pyramid_input_string + "'")
                    print("By spróbować ponownie wciśnij: T/t")
                    print("By zakończyć program wciśnij inny klawisz niż: T/t")
                    if (input("Kontynuować? ").upper() == "T"):
                        print("Wybrałeś by kontynuować. Zaczynamy ponownie...")
                        pyramid_input_numeric_or_not = False
                    else:
                        print("Nie chciałeś próbować ponownie. Koniec programu.")
                        exit()
            pyramid = int(pyramid_input_string)
            pyramid_counter = 1
            pyramid_list=list(range(1,2*pyramid,2))
            pyramid_max=pyramid_list[-1]
            while pyramid_counter<=pyramid:
                print(" "*(pyramid-pyramid_counter) + "#"*pyramid_list[(pyramid_counter-1)])
                pyramid_counter = pyramid_counter+1

            program_title = "Koniec programu do rysowania piramidy"
            print("-" * len(program_title))
            print(program_title)
            print("-" * len(program_title))
        elif int(program_choice) == 9:
            program_title = "Programu do wyliczania wieku psa."
            print("-" * len(program_title))
            print(program_title)
            print("-" * len(program_title))

            dog_input_numeric_or_not = False
            while dog_input_numeric_or_not == False:
                print("Podaj ile lat ma pies")
                dog_input_string = input("przeliczę to względem lat ludzkich (możliwe liczby całkowite, większe niż 0) : ")
                dog_input_numeric_or_not = dog_input_string.isnumeric()
                if (dog_input_numeric_or_not == False) or (dog_input_numeric_or_not==True and int(dog_input_string)<=0):
                    print("Wprowadzono błędą wartość: '" + dog_input_string + "'")
                    print("By spróbować ponownie wciśnij: T/t")
                    print("By zakończyć program wciśnij inny klawisz niż: T/t")
                    if (input("Kontynuować? ").upper() == "T"):
                        print("Wybrałeś by kontynuować. Zaczynamy ponownie...")
                        dog_input_numeric_or_not = False
                    else:
                        print("Nie chciałeś próbować ponownie. Koniec programu.")
                        exit()

            dog = int(dog_input_string)
            dog_human = 0.0
            dog_counter = 1
            while dog_counter<=dog:
                if dog_counter in (1,2):
                    dog_human = dog_human + 10.5
                else:
                    dog_human = dog_human + 4
                dog_counter = dog_counter + 1

            print("Wiek psi: "+dog_input_string+" to tyle przeliczając na lata ludzkie: "+str(dog_human))

            program_title = "Koniec programu do wyliczania wieku psa."
            print("-" * len(program_title))
            print(program_title)
            print("-" * len(program_title))
        else: # int(program_choice) == 10:
            program_title = "Program 24h temperatur"
            print("-" * len(program_title))
            print(program_title)
            print("-" * len(program_title))

            dane = "215021482120211921002076207620502065202020152010200520002001199319901950183417501744186019462010"

            for time in list(range(0, 24)):
                result = ""
                if time < 10:
                    result = "0"
                else:
                    pass
                result = result + str(time) + ":00:\t"
                temp_string = dane[(time * 4):((time * 4) + 4)]
                temp_float = float(temp_string[:2] + "." + temp_string[2:])
                result = result + temp_string[:2] + "." + temp_string[2:] + "\u00b0" + "C"
                if temp_float <= 20.00:
                    result = result + "\t!"
                else:
                    pass

                if temp_float <= 18.5:
                    result = result + "!"
                print(result)


            program_title = "Koniec programu 24h temperatur"
            print("-" * len(program_title))
            print(program_title)
            print("-" * len(program_title))

        print("Chcesz ponownie wybrać jeden z 10 podprogramów wciśnij: T/t")
        print("By zakończyć program wciśnij inny klawisz niż: T/t")
        if (input("Kontynuować? ").upper() == "T"):
            print("Wybrałeś by kontynuować. Zaczynamy ponownie...")
            program_choice_decimal_or_not = False
        else:
            print("Nie chciałeś próbować ponownie. Koniec programu.")
            exit()