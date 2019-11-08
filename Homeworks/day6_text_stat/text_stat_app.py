import os

def hello():
    """
    Just saying hello.
    """
    print("==========================")
    print("Cześć! \nWitaj w Statystykach Tekstu.")
    print("==========================")


def bye():
    """
    Just saying bye.
    """
    print("==========================")
    print("Miłego dnia.\nKoniec programu Statystyki Tekstu.")
    print("==========================")

def pick_a_file():
    pass
    #return file, file_exists

def choose_case_setting():
    pass
    #return 1 or 0


def load_and_process_file():

    #load a file with "with"

    # print some statistics of the text in this file
    statistics_print(file)

def statistics_print(file):
    pass


def add_log_entry(name):
    """
    Logging data:
    1. Every program run data to pickle file.
    2. Summary of all runs to a txt file.
    """
    check_if_log_file_exists(name)


def check_if_log_file_exists(name):
    """
    checking if our log files exist and if not it will create them
    """

    message = "Sprawdzam plik (pkl). "
    if os.path.isfile('./'+name+".pkl") == False:
        with open(name+".pkl", 'w+') as pickle_file:
            print(message, 'Brak pliku - plik został stworzony')
    else:
        print(message, "Plik istnieje.")

    message = "Sprawdzam plik (txt). "
    if os.path.isfile('./'+name+".txt") == False:
        with open(name+".txt", 'w+') as pickle_file:
            print(message, 'Brak pliku - plik został stworzony')
    else:
        print(message, "Plik istnieje.")

#Main code
hello()

#setting up the log files names
log_files = "text_stat_app"

#user now has to pick a file
file, file_exists = pick_a_file()

#check with user to use case sensitive or non sensitive statistics
case_setting = choose_case_setting()

#loading a file and printing some statistics
load_and_process_file()

#adding log entry (to pickle for all program runs and txt file for summary)
add_log_entry()

bye()
