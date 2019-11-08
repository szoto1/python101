#Here we practice csv

# import csv
#
# age = 0
#
# with open('test.csv', 'r+', newline='') as csv_file:
#     csv_data = csv.reader(csv_file)
#
#     for row in csv_data:
#         if row[4].isdigit():
#             age = age + int(row[4])
#
#     print("Age is: " + str(age))
#
#     # csv_write = csv.writer(csv_file)
#     # csv_write.writerow(['ZZZ', 'XXX', 'Gdansk', '123123', '18'])
#
# print('Bye')


#Here we practice pickle
def pickle_practice():

    import pickle
    from datetime import datetime

    def initial_list_creation():
        entries = [
            {"title" : "Pierwszy wpis", "body" : "Tresc pierwszego wpisu", "author" : "Gal Anonim", "date" : "2019-11-07"},
            {"title": "Drugi wpis", "body": "Tresc drugiego wpisu", "author": "Lukasz", "date": "2019-11-07"}
        ]
        return entries

    def list_creation():
        with open('book.pkl', 'rb+') as book_file:
            data = pickle.load(book_file)  # loading data to look what it has inside
            return data

    def ask_to_end():
        user_choice = input("Your choice: ")
        if user_choice.upper()=='YES':
            return False
        else:
            return True

    def add_new_entry():
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

    def save_to_pikle(entries):
        #here we save list entries to pickle file (binary data)
        with open('book.pkl', 'rb+') as book_file:
            pickle.dump(entries, book_file) #dumping data to file

    def choose_option():
        done = False
        while done == False:
            print("Choose what you want to do: ")
            print("Press 1 to: Add new entry")
            print("Press 2 to: Search entries with your input in body")
            print("Press 3 to: Print all entries from older to newer")
            print("Press 4 to: Print all entries from newer to older")
            user_input_option = input("Your choice: ")
            if user_input_option.isdigit():
                if int(user_input_option) in range(1,5):
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

    def new_entry():
        stop = False
        while stop == False:
            entries = list_creation()
            new_entry = add_new_entry()
            entries.append(new_entry)
            print("This is how many entries there is now: " + str(len(entries)))
            save_to_pikle(entries)
            # here we print those entries
            print("Here are all the entries: ")
            print(list_creation())
            print("If you want to add another entry please type: yes")
            print("If you type another key this task will end.")
            stop = ask_to_end()

    def new_search():
        #open file
        entries = list_creation()
        user_search_text = input("Please type what you want to search for: ")

        for row in entries:
            print(row.items())
            #dodanie wyszukiwania w body?





    def sort_print(option):
        """option can be with value:
        3 - Print all entries from older to newer
        4 - Print all entries from newer to older
        """
    #Main program loop

    end_program = False
    while end_program == False:
        option = choose_option()

        if option==1:
            new_entry()
        elif option==2:
            new_search()
        else:
            sort_print(option)

        print("If you want to make another action please type: yes")
        print("If you type another key program will end.")
        end_program = ask_to_end()

    print("This is the end.")
    exit()

#pickle_practice()

def try_exceptions():
    # here we try exceptions
    try:
        division = 10/0
        print(unresolved_variable)
    except ZeroDivisionError:
        print("Nie dziel przez zero.")
    except NameError:
        print("Brakuje zmiennej")
    except:
        print("Inny blad")

try_exceptions()