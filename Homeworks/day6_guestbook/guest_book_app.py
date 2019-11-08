import os
import pickle
from datetime import datetime
from operator import itemgetter
import random


def check_if_book_file_exists(guest_book_file_name):
    """cheking if our guest book pickle file exists and if not it will create it"""

    message = "Sprawdzam plik księgi gości. "
    if os.path.isfile('./'+guest_book_file_name) == False:
        with open(guest_book_file_name, 'w+') as book_file:
            print(message, 'Brak pliku księgi gości. Plik został stworzony')
    else:
        print(message, "Plik księgi gości istnieje.")

def ask_to_end():
    """checking what will user answer"""

    user_choice = input("Twój wybór: ")
    if user_choice.upper()=='T':
        return False
    else:
        return True

def add_new_entry():
    """
    Takes input from user with guest book entry and adds it to dictionary
    that is returned.
    """

    print("Podaj co zawierać ma dodawany wpis: ")
    new_title = input("Tytuł: ")
    new_body = input("Treść: " )
    new_author = input("Autor: " )
    new_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    new_entry=dict()
    new_entry['title'] = new_title
    new_entry['body'] = new_body
    new_entry['author'] = new_author
    new_entry['date'] = new_date

    return new_entry

def choose_option():
    """
    Function to let the user choose option to do. User can pick from couple of options:
    1. To add new entry to guest book.
    2. To search entries in the guest book by the content in the body of the guest book entry.
    3. Print all entries in order from older to newer.
    4. Print all antries in order from newer to older.
    """

    done = False
    while done == False:
        print("Wybierz, którą czynność wykonać: ")
        message = "Wciśnij 1 aby: Dodać nowy wpis"\
                  "\nWciśnij 2 aby: Wyszukać wpisy zawierające podaną przez Ciebie frazę w treści wpisu." \
                  "\nWciśnij 3 aby: Wyświetlić wszystkie wpisy od najstarszego do najnowszego" \
                  "\nWciśnij 4 aby: Wyświetlić wszystkie wpisy od najnowszego do najstarszego" \
                  "\nWciśnij 5 aby: Wyświetlić wpisy pojedyńczo (następny/poprzedni)" \
                  "\nWciśnij 6 aby: Wyświetlić losowy wpis" \
                  "\nWciśnij 7 aby: Zakończyć program"
        print(message)
        user_input_option = input("Twój wybór: ")
        if user_input_option.isdigit():
            if int(user_input_option) in range(1,message.count('\n')+2):
                print("Wybrana opcja: " + user_input_option)
                return int(user_input_option)
            else:
                print("Błędna wartość.")
                print("Jeśli chcesz spróbować ponownie wciśnij: T lub t")
                print("Inny klawisz zakończy obecną opcję.")
                done = ask_to_end()
        else:
            print("Błędna wartość.")
            print("Jeśli chcesz spróbować ponownie wciśnij: T lub t")
            print("Inny klawisz zakończy obecną opcję.")
            done = ask_to_end()

def list_creation(guest_book_file_name):
    """
    This function creates list from pickle guest book file.
    If the file is empty it will return empty list.
    """

    with open(guest_book_file_name, 'rb+') as book_file:
        try:
            data = pickle.load(book_file)  # loading data to look what it has inside
        except EOFError:
            print("Plik księgi gości jest pusty.")
            data = []
        except Exception:
            print("Coś nie obsłużonego poszło nie tak...")
            data = []
        return data

def save_to_pikle(entries,guest_book_file_name):
    """saves list of entries to guest book pickle file (binary data)"""

    with open(guest_book_file_name, 'rb+') as book_file:
        pickle.dump(entries, book_file)  # dumping data to file

def new_entry(guest_book_file_name):
    """Function to add new entry to guest book pickle file from user input data."""

    stop = False
    while stop == False:
        entries = list_creation(guest_book_file_name)
        print("Tyle wpisów jest przed dodaniem Twojego, nowego wpisu: " + str(len(entries)))
        new_entry = add_new_entry()
        entries.append(new_entry)
        print("Tyle wpisów jest po dodaniu Twojego, nowego wpisu: " + str(len(entries)))
        save_to_pikle(entries,guest_book_file_name)
        # here we print those entries
        # print("Oto wszystkie wpisy: ")
        # print(list_creation(guest_book_file_name))
        print("Jeśli chcesz dodać inny wpis wciśnij: T lub t")
        print("Inny klawisz zakończy obecną opcję.")
        stop = ask_to_end()

def search_guest_book(guest_book_file_name,user_search_text):
    """
    Function to search if user input string is in any of entries in the body
    and if there is a match print those entries.
    """

    entries = list_creation(guest_book_file_name)
    matches = []

    for row in entries:
        if user_search_text.lower() in row['body'].lower():
            matches.append(row)

    return matches

def new_search(guest_book_file_name):
    """Function to take input from user and then return if there was a search match."""

    stop = False
    while stop == False:

        user_search_text = input("Proszę podaj frazę, po której przeszukam treści wpisów księgi gości (wielkość liter nie ma znaczenia): ")
        matches = search_guest_book(guest_book_file_name,user_search_text)
        matches_len = len(matches)
        print("Znaleziono tyle wpisów: "+str(matches_len)+" z szukaną frazą: "+user_search_text)
        if len(matches)!=0:
            print("Oto wszystkie wpisy z frazą: "+user_search_text+" w treści: ")
            for row in matches:
                print_entry_dict(row)
        print("Jeśli chcesz wykonać kolejne wyszukiwanie wpis wciśnij: T lub t")
        print("Inny klawisz zakończy obecną opcję.")
        stop = ask_to_end()

def sort_print(option, guest_book_file_name):
    """option can be with value:
    3 - Print all entries from older to newer
    4 - Print all entries from newer to older
    """
    entries, entries_len = check_if_empty(guest_book_file_name)

    if entries_len == 0:
        print("Brak możliwości wyświetlenia posortowanych wpisów.")
        return False

    if option==3:
        print("Oto wszystkie wpisy w księdze gości od najstarszego do najmłodszego:")
        for row in sorted(entries, key=itemgetter('date'), reverse=True):
            print_entry_dict(row)
    else:
        print("Oto wszystkie wpisy w księdze gości od najnowszego do najstarszego:")
        for row in sorted(entries, key=itemgetter('date')):
            print_entry_dict(row)

def check_if_empty(guest_book_file_name):
    entries = list_creation(guest_book_file_name)
    entries_len = len(entries)
    return entries, entries_len

def random_print(guest_book_file_name):
    """This function will print random entry from the guest book."""
    entries, entries_len = check_if_empty(guest_book_file_name)
    if entries_len == 0:
        print("Brak wpisów w księdze gości. Losowy wpis nie mógł być wyświetlony.")
    elif entries_len == 1:
        print("W księdze gości jest tylko jeden wpis, który właśnie dla Ciebie wyświetlam:")
        print_entry_list(entries)
    else:
        print("W księdze gości jest tyle wpisów: "+str(entries_len) +". Wyświetlam losowy: ")
        random_stop = False
        while random_stop == False:
            index = random.randrange(len(entries))
            print_entry_list(entries,index)
            #print(random.choice(entries))
            print("Jeśli chcesz wywietlić kolejny losowy wpis wciśnij: T lub t"
                  "\nWciśnięcie innego klawisza zakończy wyświetlanie wpisów losowych.")

            random_stop = ask_to_end()
def hello():
    """Printing the hello message."""

    print("==========================")
    print("Cześć! \nWitaj w Księdze Gości.")
    print("==========================")

def bye():
    """Printing the bye message."""

    print("==========================")
    print("Miłego dnia.\nKoniec programu Księga Gości.")
    print("==========================")

def before_or_after(index, last_entry_index):
    """
    This function will ask user what to do next:
    - show the entry one before
    - show the entry one after
    Return value of:
    - 1 will mean show the one after
    - -1 will mean show the one before
    """
    choice_message = ""
    next_doable = False
    back_doable = False
    if index == 0:
        choice_message="Wyświetlony wpis był pierwszym w księdze gości. Aby wyświetlić kolejny wpis wybierz: N lub n"
        next_doable = True
    elif index == last_entry_index:
        choice_message="Wyświetlony wpis był ostatnim w księdze gości. Aby wyświetlić poprzedni wpis wybierz: P lub p"
        back_doable = True
    else:
        choice_message="Wybierz: N lub n aby wyświetlić następny wpis.\nWybierz: P lub p aby wyświetlić poprzedni wpis."
        next_doable = True
        back_doable = True

    done = False
    while done == False:
        choice = 0
        print(choice_message)
        print("Wybierz: Z lub z aby zakończyć.")
        user_choice = input("Twój wybór: ")
        if user_choice.upper() == 'N':
            if next_doable:
                print("Twój wybór to wyświetlenie następnego wpisu.")
                choice = 1
                done = True
            else:
                print("Błędna wartość.")
                print("Jeśli chcesz spróbować ponownie wciśnij: T lub t")
                print("Inny klawisz zakończy obecną opcję.")
                done = ask_to_end()
        elif user_choice.upper() == 'P':
            if back_doable:
                print("Twój wybór to wyświetlenie poprzedniego wpisu.")
                choice = -1
                done = True
            else:
                print("Błędna wartość.")
                print("Jeśli chcesz spróbować ponownie wciśnij: T lub t")
                print("Inny klawisz zakończy obecną opcję.")
                done = ask_to_end()
            done = True
        elif user_choice.upper() == 'Z':
            break
        else:
            print("Błędna wartość.")
            print("Jeśli chcesz spróbować ponownie wciśnij: T lub t")
            print("Inny klawisz zakończy obecną opcję.")
            done = ask_to_end()

    return choice

def before_after_print(guest_book_file_name):
    """
    Printing all entries one by one.
    User will choose if the next entry shown will be the one that is before or after current one.
    """
    entries, entries_len = check_if_empty(guest_book_file_name)

    if entries_len == 0:
        print("Brak możliwości wyświetlenia wpisów.")
        return False
    elif entries_len == 1:
        print("Jest tylko jeden wpis w księdze gości. Oto on: ")
        print_entry_list(entries)
    else:
        entry_index_to_show = 0
        show_another = False
        while show_another == False:
            print("Oto wpis numer "+str(entry_index_to_show+1)+":")
            print_entry_list(entries,entry_index_to_show)
            user_choice = before_or_after(entry_index_to_show, entries_len-1)
            if user_choice == 1:
                entry_index_to_show=entry_index_to_show+1
            elif user_choice == -1:
                entry_index_to_show=entry_index_to_show-1
            else:
                show_another = True

def print_entry_dict(row):
    """
    Print more elegant way our entry.
    """
    elegant_print = "--------------------------------------------------\n"
    elegant_print = elegant_print + "Autor wpisu: " + row['author'] + "\n" \
                    "Tytuł wpisu: " + row['title'] + "\n" \
                    "Treść wpisu: " + row['body'] + "\n" \
                    "Data dodania wpisu: " + row['date']
    elegant_print = elegant_print +"\n--------------------------------------------------"
    print(elegant_print)

def print_entry_list(list,index=-1):
    """
    Print all or one entry from list.
    """

    if index == -1:
        list_to_show = list
    else:
        list_to_show = list[index:index+1]

    for row in list_to_show:
        print_entry_dict(row)


#Main program
hello()

guest_book_file_name = "ksiega_gosci.pkl"

#Will now check if guest book file exists and if not empty file will be created
check_if_book_file_exists(guest_book_file_name)

end_program = False
while end_program == False:
    option = choose_option()

    if option == 1:
        new_entry(guest_book_file_name)
    elif option == 2:
        new_search(guest_book_file_name)
    elif option == 3:
        sort_print(option,guest_book_file_name)
    elif option == 4:
        sort_print(option,guest_book_file_name)
    elif option == 5:
        before_after_print(guest_book_file_name)
    elif option == 6:
        random_print(guest_book_file_name)
    else:
        end_program = True
        continue

    print("Jeśli chcesz ponownie wybrać opcję do wykonania wciśnij: T lub t")
    print("Inny klawisz zakończy program.")
    end_program = ask_to_end()

bye()
exit()
