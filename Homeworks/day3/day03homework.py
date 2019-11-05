def create_programs_list():
    """Returns list of the modules that user can pick from and run."""

    #if we need to add a new module please add new append at the end of program_list creation
    programs_list = []
    programs_list.append([len(programs_list)+1, "Przeliczanie stopni w skali Celcjusza i Fahrenheita"])
    programs_list.append([len(programs_list)+1, "Podawanie pierwszej i ostatniej cyfry wprowadzonej liczby"])
    programs_list.append([len(programs_list)+1, "Rysowanie prostokątu o zadanych rozmiarach"])
    programs_list.append([len(programs_list)+1, "Przeliczanie liczby zapisanej w formacie binarnym na system dziesiętny"])
    programs_list.append([len(programs_list)+1, "Czy podany rok jest rokiem przestępnym?"])
    programs_list.append([len(programs_list)+1, "Program do rysowania list"])
    programs_list.append([len(programs_list)+1, "Podaj kwotę - rozmienię to na najmniejszą ilość monet."])
    programs_list.append([len(programs_list)+1, "Rysowanie piramidy o zadaniej wielkości"])
    programs_list.append([len(programs_list)+1, "Kalkulator wieku psa"])
    programs_list.append([len(programs_list)+1, "24h temperatur"])

    return programs_list

def print_separation_line(number_of_chars=31):
    """Creates line of text only with '=' multiple times (default is 31) """
    print("="*number_of_chars)

def program_title(program_title,start):
    """Creates a description about starting or ending of the module."""
    if start:
        text_add = "To jest początek modułu o nazwie: "
    else:
        text_add = "To jest koniec modułu o nazwie: "
    text_to_print = text_add+program_title[1]
    print("-" * len(text_to_print))
    print(text_to_print)
    print("-" * len(text_to_print))

def ask_to_repeat(mode=1):
    """Function is checking if user want to continue or stop. Is returning True or False value."""
    if mode==1:
        print("By spróbować ponownie wciśnij: T/t")
        print("By zakończyć moduł wciśnij inny klawisz niż: T/t")
    else:
        print("By kontynuować wciśniej: T/t")
        print("By zakończyć program wciśnij inny klawisz niż: T/t")

    if (input("Kontynuować? ").upper() == "T"):
        print("Wybrałeś by kontynuować. Zaczynamy ponownie...")
        return True
    else:
        print("Nie chciałeś próbować ponownie.")
        return False

def input_numeric_or_not(input_desc):
    """Function is checking if input value is numeric or not."""
    user_input_numeric_or_not = False
    while user_input_numeric_or_not == False:
        user_input_string = input(input_desc)
        user_input_numeric_or_not = user_input_string.lstrip('-+').isnumeric()
        if user_input_numeric_or_not == False:
            print("Wprowadzono błędą wartość: '" + user_input_string + "'")
            print("By spróbować ponownie wciśnij: T/t")
            print("By zakończyć program wciśnij inny klawisz niż: T/t")
            if (input("Kontynuować? ").upper() == "T"):
                print("Wybrałeś by kontynuować. Zaczynamy ponownie...")
                user_input_numeric_or_not = False
            else:
                print("Nie chciałeś próbować ponownie. Koniec programu.")
                return None
    return user_input_string

def modul_1():
    """Runs module 1 function."""

    program_title(list_of_moduls[int(program_choice) - 1], True)

    user_choice = ""
    scale_list = ("C", "F")
    while user_choice.upper not in scale_list:
        print("Chcesz przeliczyć: ")
        print(" - stopnie Celcjusza na stopnie Fahrenheita wciśnij C")
        print(" - stopnie Fahrenheita na stopnie Celcjusza wciśnij F")
        user_choice = input("Twój wybór: \n")
        if user_choice.upper() in scale_list:
            break
        else:
            print("Został wprowadzony błędny znak: " + user_choice)
            if ask_to_repeat():
                continue
            else:
                return False

    print("Poprawnie dokonano wyboru. Podałeś: " + user_choice)
    degrees_to_be_calculated = 0.00
    if user_choice.upper() == 'C':
        print("Wybrałeś przeliczenie skali Celcjusza na Fahranhaita.")

        user_degrees_input_finished = False
        while user_degrees_input_finished == False:
            user_degrees_input = input("Podaj temperaturę w Celcjuszach (wprowadź tylko cyfry): ")
            try:
                user_degrees = float(user_degrees_input)
            except:
                print("Podano błędną wartość: '" + user_degrees_input + "', spróbuj raz jeszcze.")
                continue
            user_degrees_input_finished = True

        print("Podano temperaturę: " + str(user_degrees_input) + " stopni w skali Celcjusza")
        print("Przeliczam na skalę Fahrenheita")
        user_degrees_calculated = round((user_degrees * 9 / 5) + 32, 10)
        print("Przeliczono wg wzoru:")
        print("32+([Podana wartość stopni w Celcjuszach] *9/5) = " + str(user_degrees_calculated))
        print("Wynik końcowy:")
        print(str(user_degrees) + " stopni Celcjusza to: " + str(user_degrees_calculated) + " stopni Fahrenheita.")
    else:
        print("Wybrałeś przeliczenie skali Fahranhaita na Celcjusza.")

        user_degrees_input_finished = False
        while user_degrees_input_finished == False:
            user_degrees_input = input("Podaj temperaturę w Fahranhaitach (wprowadź tylko cyfry): ")
            try:
                user_degrees = float(user_degrees_input)
            except:
                print("Podano błędną wartość: " + user_degrees_input + ", spróbuj raz jeszcze.")
                continue
            user_degrees_input_finished = True

        print("Podano temperaturę: " + str(user_degrees_input) + " stopni w skali Fahranhaita")
        print("Przeliczam na skalę Celcjusza")
        user_degrees_calculated = round((user_degrees - 32) * 5 / 9, 10)
        print("Przeliczono wg wzoru:")
        print("([Podana wartość stopni w Fahranhaitach]-32)*9/5) = " + str(user_degrees_calculated))
        print("Wynik końcowy:")
        print(str(user_degrees) + " stopni Fahranhaita to: " + str(user_degrees_calculated) + " stopni Celcjusza.")
    program_title(list_of_moduls[int(program_choice) - 1], False)

def modul_2():
    """Runs module 2 function."""

    program_title(list_of_moduls[int(program_choice) - 1], True)
    user_input_string = input_numeric_or_not("Podaj liczbę abym mógł zwrócić jej pierwszą i ostatnią cyfrę: ")
    if user_input_string == None:
        print("Zrezygnowałeś z wprowadzania wartości.")
    else:
        print("Podano poprawnie liczbę: " + user_input_string)
        if int(user_input_string) > 9 or int(user_input_string) < -9:
            print("Podano: " + user_input_string)
            print("Pierwsza cyfra to: " + user_input_string.lstrip('-')[0] + ", druga cyfra to: " +
                  user_input_string.lstrip('-')[-1])
        else:
            print("Podano tylko jedną cyfrę. Pierwsza i ostatnia cyfra to zatem: " + user_input_string.lstrip("-"))
    program_title(list_of_moduls[int(program_choice) - 1], False)

def modul_3():
    """Runs module 3 function."""

    program_title(list_of_moduls[int(program_choice) - 1], True)
    length_string = input_numeric_or_not("Podaj długość prostokąta (możliwe tylko liczby całkowite większe niż 1): ")
    if length_string == None:
        return False
    else:
        while int(length_string) <= 1:
            print("Podana wartość nie jest większa niż 1.")
            if ask_to_repeat():
                length_string = input_numeric_or_not("Podaj długość prostokąta (możliwe tylko liczby całkowite większe niż 1): ")
                if length_string == None:
                    return False
            else:
                return False

    width_string = input_numeric_or_not("Podaj szerokość prostokąta (możliwe tylko liczby całkowite większe niż 1): ")
    if width_string == None:
        return False
    else:
        while int(width_string) <= 1:
            print("Podana wartość nie jest większa niż 1.")
            if ask_to_repeat():
                width_string = input_numeric_or_not("Podaj szerokość prostokąta (możliwe tylko liczby całkowite większe niż 1): ")
                if width_string == None:
                    return False
            else:
                return False

    print("Podano poprawnie długość: " + length_string)
    print("Podano poprawnie szerokość: " + width_string)

    length = int(length_string)
    width = int(width_string)
    print("+" + "-" * (length - 2) + "+")
    inside_box = 1
    while inside_box < (width - 1):
        print("|" + " " * (length - 2) + "|")
        inside_box = inside_box + 1
    print("+" + "-" * (length - 2) + "+")
    program_title(list_of_moduls[int(program_choice) - 1], False)

def modul_4():
    """Runs module 4 function."""

    program_title(list_of_moduls[int(program_choice) - 1], True)
    user_input_string=input_numeric_or_not("Podaj zapis binarny liczby: ")
    if user_input_string == None:
        print("Zrezygnowałeś z wprowadzania wartości.")
        return False
    print("Podano poprawnie liczbę binarnie: " + user_input_string)
    print("Liczba ta zamieniona na dziesiętny to: " + str(int(user_input_string, 2)))
    program_title(list_of_moduls[int(program_choice) - 1], False)
    return True

def modul_5():
    """Runs module 5 function."""

    program_title(list_of_moduls[int(program_choice) - 1], True)

    user_input_string=input_numeric_or_not("Podaj rok: ")
    if user_input_string == None:
        print("Zrezygnowałeś z wprowadzania wartości.")
        return False

    print("Podano poprawnie rok: " + user_input_string)

    year = int(user_input_string)
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("Rok " + user_input_string + " to rok przestępny.")
    else:
        print("Rok " + user_input_string + " nie jest rokiem przestępnym.")

    program_title(list_of_moduls[int(program_choice) - 1], False)
    return True


def string_list_audit(string_input):
    """Function perform basic audit for string for module 6 list building"""
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
    """Creating list from string that can contain lists inside other lists"""
    from tabulate import tabulate
    tabulate.PRESERVE_WHITESPACE = True
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
                    if new_inlist_string[-1] == ",":
                        new_inlist_string = new_inlist_string[0:-1]

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

def modul_6():
    """Runs module 6 function."""

    program_title(list_of_moduls[int(program_choice) - 1], True)
    from tabulate import tabulate
    tabulate.PRESERVE_WHITESPACE = True

    module6_another_list_loop = True
    while module6_another_list_loop == True:
        print("Przygotowałem kilka przykładowych zestawów danych z których możesz wybrać wykonanie programu.")
        dane1 = "['col1', 'col2', 'col3']"
        dane2 = "['col1', 'col2', 'col3', ['col4', 'col5', 'col6']]"
        dane3 = "[['col1', 'col2'], 'col3', ['col4', 'col5']]"
        dane4 = "['col1', 'col2', 'col3', ['col4', 'col5', ['col6', 'col7']]]"

        print("Wybierz jedną z opcji wciskając 1, 2, 3, 4 lub 5: ")
        print("-   1 - wykonanie programu z listą: " + dane1)
        print("-   2 - wykonanie programu z listą: " + dane2)
        print("-   3 - wykonanie programu z listą: " + dane3)
        print("-   4 - wykonanie programu z listą: " + dane4)
        print("-   5 - wprowadź listę samemu.")

        choice_list = list(range(1, 6))
        user_choice = input_numeric_or_not("Twój wybór: ")
        if user_choice == None:
            module6_another_list_loop = False
        else:
            while int(user_choice) not in choice_list:
                print("Podana wartość jest błędna.")
                if ask_to_repeat():
                    user_choice = input_numeric_or_not("Twój wybór: ")
                    if user_choice == None:
                        module6_another_list_loop = False
                else:
                    module6_another_list_loop = False

        #Printing list
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
            string_list = string_list.replace(", ", ",")
            string_list = string_list.replace(",", ", ")

        new_list = create_list_from_input_string(string_list)
        list_to_output = []
        list_to_output.insert(0, new_list)

        print("Podana do narysowania lista to: ")
        print(string_list)
        print("a tak wygląda po narysowaniu:")
        print(tabulate(list_to_output, tablefmt="psql"))

        print("Może chcesz spróbować wydrukować inną listę?")
        module6_another_list_loop = ask_to_repeat()
    program_title(list_of_moduls[int(program_choice) - 1], False)
    return True


def modul_7():
    """Runs module 7 function."""

    program_title(list_of_moduls[int(program_choice) - 1], True)
    user_money_input_finished = False
    while user_money_input_finished == False:
        user_money_input = input("Podaj kwotę do rozmienienia: ")
        try:
            user_money = float(user_money_input)
        except:
            print("Podano błędną kwotę: " + user_money_input)
            if ask_to_repeat():
                continue
            else:
                return False
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

    value_5 = round((user_money - round(user_money % 5, 2)) / 5)
    user_money = user_money - 5 * value_5
    print("Sprawdzam monety o wartości 5. Będzie ich: " + str(value_5))
    value_2 = round((user_money - round(user_money % 2, 2)) / 2)
    user_money = user_money - 2 * value_2
    print("Sprawdzam monety o wartości 2. Będzie ich: " + str(value_2))
    value_1 = round((user_money - round(user_money % 1, 2)) / 1)
    user_money = user_money - 1 * value_1
    print("Sprawdzam monety o wartości 1. Będzie ich: " + str(value_1))
    value_0_5 = round((user_money - round(user_money % 0.5, 2)) / 0.5)
    user_money = user_money - 0.5 * value_0_5
    print("Sprawdzam monety o wartości 0.5. Będzie ich: " + str(value_0_5))
    value_0_2 = round((user_money - round(user_money % 0.2, 2)) / 0.2)
    user_money = user_money - 0.2 * value_0_2
    print("Sprawdzam monety o wartości 0.2. Będzie ich: " + str(value_0_2))
    value_low = round((user_money - round(user_money % 0.1, 2)) / 0.1)
    user_money = user_money - 0.1 * value_low
    print("Sprawdzam monety o wartości 0.1. Będzie ich: " + str(value_low))

    user_money_left = round(
        user_money_org - (value_5 * 5) - (value_2 * 2) - (value_1 * 1) - (value_0_5 * 0.5) - (value_0_2 * 0.2) - (
                    value_low * 0.1), 2)
    if user_money_left != 0:
        print("Pozostanie kwota niemożliwa do rozłożenia na monety: " + str(user_money_left))
    program_title(list_of_moduls[int(program_choice) - 1], False)
    return True


def modul_8():
    """Runs module 8 function."""

    program_title(list_of_moduls[int(program_choice) - 1], True)

    length_string = input_numeric_or_not("Podaj wielkość piramidy (możliwe tylko liczby całkowite większe niż 1): ")
    if length_string == None:
        return False
    else:
        while int(length_string) <= 1:
            print("Podana wartość nie jest większa niż 1.")
            if ask_to_repeat():
                length_string = input_numeric_or_not("Podaj wielkość piramidy (możliwe tylko liczby całkowite większe niż 1): ")
                if length_string == None:
                    return False
            else:
                return False

    pyramid = int(length_string)
    pyramid_counter = 1
    pyramid_list = list(range(1, 2 * pyramid, 2))
    pyramid_max = pyramid_list[-1]
    while pyramid_counter <= pyramid:
        print(" " * (pyramid - pyramid_counter) + "#" * pyramid_list[(pyramid_counter - 1)])
        pyramid_counter = pyramid_counter + 1

    program_title(list_of_moduls[int(program_choice) - 1], False)


def modul_9():
    """Runs module 9 function."""

    program_title(list_of_moduls[int(program_choice) - 1], True)

    dog_year_string = input_numeric_or_not("Podaj ile lat ma pies: ")
    if dog_year_string == None:
        return False
    else:
        while int(dog_year_string) <= 0:
            print("Podana wartość nie jest większa niż 0.")
            if ask_to_repeat():
                dog_year_string = input_numeric_or_not("Podaj ile lat ma pies: ")
                if dog_year_string == None:
                    return False
            else:
                return False

    dog = int(dog_year_string)
    dog_human = 0.0
    dog_counter = 1
    while dog_counter <= dog:
        if dog_counter in (1, 2):
            dog_human = dog_human + 10.5
        else:
            dog_human = dog_human + 4
        dog_counter = dog_counter + 1

    print("Wiek psi: " + dog_year_string + " to tyle przeliczając na lata ludzkie: " + str(dog_human))

    program_title(list_of_moduls[int(program_choice) - 1], False)

def modul_10():
    """Runs module 10 function."""

    program_title(list_of_moduls[int(program_choice) - 1], True)
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
    program_title(list_of_moduls[int(program_choice) - 1], False)

# Main program starts here
print("Praca domowa - Łukasz Szotowski")
print_separation_line()
print("Witaj w Multitool Python (beta)")
print_separation_line()

#Creating list of program to choose from
list_of_moduls = create_programs_list()
number_of_programs = len(list_of_moduls)

#starting main program loop to choose modul to run
program_choice = ''
program_run = True
while program_run == True:
    print("Wybierz, który program uruchomić podając liczbę od 1-" + str(number_of_programs) + " gdzie: ")

    # printing list of moduls to choose from
    for modul in list_of_moduls:
        print("   - " + str(modul[0]) + " - " + modul[1])

    program_choice = input_numeric_or_not("Twój wybór: ")

    if program_choice == None:
        program_run = False
    else:
        while int(program_choice) not in range(1,number_of_programs+1) and program_run==True:
            print("Podana wartość nie jest z zakresu 1-"+str(number_of_programs)+".")
            if ask_to_repeat():
                program_choice = input_numeric_or_not("Twój wybór: ")
                if program_choice == None:
                    program_run = False
            else:
                program_run = False

    if program_run == True:
        print("Poprawnie dokonano wyboru. Podałeś: " +program_choice)
        moduls = globals()["modul_%s" % int(program_choice)]
        #running of the chosen module
        moduls()
        print("Chcesz ponownie wybrać jeden z "+str(number_of_programs)+" podprogramów?")
        program_run=ask_to_repeat(0)

print("Miłego dnia!")
exit()