import os
import pickle
from datetime import datetime
from operator import itemgetter

def check_if_book_file_exists(guest_book_file_name):
    """cheking if our guest book pickle file exists and if not it will create it"""

    message = "Checking guest book file. "
    if os.path.isfile('./'+guest_book_file_name) == False:
        with open(guest_book_file_name, 'w+') as book_file:
            print(message, 'No guest book file. Created one')
    else:
        print(message, "Guest book file exists.")

def ask_to_end():
    """checking what will user answer"""

    user_choice = input("Your choice: ")
    if user_choice.upper()=='YES':
        return False
    else:
        return True

def add_new_entry():
    """
    Takes input from user with guest book entry and adds it to dictionary
    that is returned.
    """

    print("Please add some values: ")
    new_title = input("Title: ")
    new_body = input("Body: " )
    new_author = input("Author: " )
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
        print("Choose what you want to do: ")
        message = "Press 1 to: Add new entry"\
                  "\nPress 2 to: Search entries with your input in body" \
                  "\nPress 3 to: Print all entries from older to newer" \
                  "\nPress 4 to: Print all entries from newer to older"
        print(message)
        user_input_option = input("Your choice: ")
        if user_input_option.isdigit():
            if int(user_input_option) in range(1,message.count('\n')+2):
                print("Chosen option: " + user_input_option)
                return int(user_input_option)
            else:
                print("Wrong value.")
                print("If you want to try again please type: yes")
                print("If you type another key this task will end.")
                done = ask_to_end()
        else:
            print("Wrong value.")
            print("If you want to try again please type: yes")
            print("If you type another key this task will end.")
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
            print("Guest Book file is empty.")
            data = []
        except Exception:
            print("Something wrong just happend.")
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
        print("This is how many entries there is before adding new one: " + str(len(entries)))
        new_entry = add_new_entry()
        entries.append(new_entry)
        print("This is how many entries there is now: " + str(len(entries)))
        save_to_pikle(entries,guest_book_file_name)
        # here we print those entries
        print("Here are all the entries: ")
        print(list_creation(guest_book_file_name))
        print("If you want to add another entry please type: yes")
        print("If you type another key this task will end.")
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

        user_search_text = input("Please type what you want to search for (search is not case sensitive): ")
        matches = search_guest_book(guest_book_file_name,user_search_text)
        matches_len = len(matches)
        print("Found "+str(matches_len)+" entries with searched text: "+user_search_text)
        if len(matches)!=0:
            print("Here are all the entries with text: "+user_search_text+" in body: ")
            for row in matches:
                print(row)
        print("If you want to do another search please type: yes")
        print("If you type another key this task will end.")
        stop = ask_to_end()


        #dodanie wyszukiwania w body?

def sort_print(option):
    """option can be with value:
    3 - Print all entries from older to newer
    4 - Print all entries from newer to older
    """

    entries = list_creation(guest_book_file_name)
    if option==3:
        print("Here are all entries in guest book from older to newer.")
        for row in sorted(entries, key=itemgetter('date'), reverse=True):
            print(row)
    else:
        print("Here are all entries in guest book from newer to older.")
        for row in sorted(entries, key=itemgetter('date')):
            print(row)


#Main program

print("==========================")
print("Hello! \nWelcome to Guest Book App.")
print("==========================")

guest_book_file_name = "guest_book.pkl"
#Will now check if guest book file exists and if not empty file will be created
check_if_book_file_exists(guest_book_file_name)

end_program = False
while end_program == False:
    option = choose_option()

    if option == 1:
        new_entry(guest_book_file_name)
    elif option == 2:
        new_search(guest_book_file_name)
    else:
        sort_print(option)

    print("If you want to make another action please type: yes")
    print("If you type another key program will end.")
    end_program = ask_to_end()

print("This is the end.")
exit()
