import os
from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import pickle
from datetime import datetime
import string

def pick_a_file():
    """picking a file from disk to analyze"""

    analyze_button.configure(state=DISABLED)
    stop = "yes"
    while stop == "yes":
        filename.set(askopenfilename())
        if filename.get()=='':
            stop = tk.messagebox.askquestion("Wskazywanie pliku do analizy.","Błędne wskazanie pliku.\nCzy chcesz ponownie spróbować wskazać plik do analizy?")
            add_live_log_entry("Błędne wskazanie pliku do analizy.")
        else:
            tk.messagebox.showinfo("Wskazywanie pliku do analizy.", "Do analizy poprawnie wskazono plik: \n"+filename.get())
            stop = "no"
            add_live_log_entry("Poprawne wskazanie pliku do analizy.")

    if filename.get()!='':
        analyze_button.configure(state=NORMAL)

def load_log(log_name):
    """
    This function creates list from pickle log file.
    If the file is empty it will return empty list.
    """

    with open(log_name, 'rb+') as book_file:
        try:
            data = pickle.load(book_file)  # loading data to look what it has inside
        except EOFError:
            add_live_log_entry("Plik logu jest pusty ("+log_name+")")
            data = []
        except Exception:
            add_live_log_entry("Uwaga! Coś poszło nie tak! ("+log_name+")")
            data = []
        return data

def save_log(list,name):
    """saves list of entries to pickle log file (binary data)"""

    with open(name, 'rb+') as log_file:
        pickle.dump(list, log_file)  # dumping data to file

def add_log_entry(list):
    """
    Logging data.
    """

    #checking if log files exist, if not create those
    check_if_log_file_exists(pickle_datalog)

    with open(pickle_datalog, 'rb+') as log_file:
        pickle.dump(list, log_file)  # dumping data to file

def check_if_log_file_exists(name):
    """
    checking if our log files exist and if not it will create them
    """

    message = "Sprawdzam plik logu ("+name+")"
    if os.path.isfile('./'+name) == False:
        with open(name, 'w+') as log_file:
            add_live_log_entry("Brak pliku - plik został stworzony ("+name+")")
    else:
        add_live_log_entry("Plik logu istnieje  ("+name+")")

def check_chars(text):
    """checking how many chars are there in the text"""

    lenght = len(text)
    return lenght

def check_words_and_ints(text):
    """checking how many words are there in the text"""

    words = 0
    ints  = 0
    for word in text.split():

        if word.strip(string.punctuation).isalpha(): #removing all punctuations and checking if word contains alphabhet signs
            words = words + 1

        if word.strip(string.punctuation).isnumeric():
            ints = ints + 1

    return words, ints

def check_lower_cases(text):
    """checking how many lower cases are there in the text"""

    lowers = 0
    for char in text:
        if char.islower():
            lowers = lowers + 1

    return lowers

def check_upper_cases(text):
    """checking how many upper cases are there in the text"""

    uppers = 0
    for char in text:
        if char.isupper():
            uppers = uppers + 1

    return uppers

def check_letters(text):
    """checking how many letters are there in the text"""

    letters = 0

    for char in text:
        if char.isalpha():
            letters = letters + 1

    return letters

def analyze():
    """
    Function to analyze text in input file and add some logs.
    """

    case_setting = case_sensible_setting.get()
    if case_setting==1:
        add_live_log_entry("Rozpoczyna się analiza wskazanego pliku z uwzględnieniem wielkości liter.")
        print("Analiza z uwzględnieniem wielkości liter.")
    else:
        add_live_log_entry("Rozpoczyna się analiza wskazanego pliku bez uwzględniania wielkości liter.")

    #loading user input file
    with open(filename.get(), 'r') as file_to_analyze:
        text_to_analyze = file_to_analyze.read()

        chars = check_chars(text_to_analyze)
        words, ints = check_words_and_ints(text_to_analyze)

        if case_setting==1:
            lower_cases = check_lower_cases(text_to_analyze)
            upper_cases = check_upper_cases(text_to_analyze)
        else:
            lower_cases = None
            upper_cases = None

        letters = check_letters(text_to_analyze)

    summary_list = load_log(pickle_datalog)
    empty_summary = dict()
    empty_summary['chars'] = chars
    empty_summary['words'] = words
    empty_summary['ints']  = ints
    empty_summary['lower_cases'] = lower_cases
    empty_summary['upper_cases'] = upper_cases
    empty_summary['letters'] = letters

    if len(summary_list)==0:
        empty_summary['run_number']=1
        add_live_log_entry("Program wykonany po raz: 1")
    else:
        empty_summary['run_number']=len(summary_list)+1
        add_live_log_entry("Program wykonany po raz: "+ str(len(summary_list)+1))

    analyzed_message = "Analizowany tekst ma:\n" \
                       "- znaków:         " + str(chars) + "\n" \
                       "- wyrazów:        " + str(words) + "\n" \
                       "- numerów:        " + str(ints)  + "\n"

    if case_setting==1:
        analyzed_message = analyzed_message + \
                       "- małych liter:   " + str(lower_cases) + "\n" \
                       "- wielkich liter: " + str(upper_cases) + "\n"
    else:
        analyzed_message = analyzed_message + \
                       "- małych liter:   (brak danych - analiza bez uwzględniania wialkości liter)"  + "\n" \
                       "- wielkich liter: (brak danych - analiza bez uwzględniania wialkości liter)"  + "\n"

    analyzed_message = analyzed_message + \
                       "- liter:          " + str(letters)

    add_live_log_entry(analyzed_message) #this will add analyze result for user to see in app
    summary_list.append(empty_summary) #this will append dict with analyze result to list
    add_log_entry(summary_list) #this will add new list to our pickle saved log

def add_live_log_entry(message, option=True, start=0):
    """
    Function is adding text for user to see in app (live log)
    """

    if start==1:
        check_if_log_file_exists(app_log_file)

    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message =  "\n" + data + " - " + message
    with open(app_log_file, 'r+') as log_file:
        log_file.read()
        log_file.write(message)

    if option == True:
        with open(app_log_file, 'r') as log_file:
            #log_label.configure(text=log_file.read())
            log_text.configure(state=NORMAL)
            log_text.insert(tk.INSERT, message)
            log_text.configure(state=DISABLED)
    else:
        pass

#Main code

app_height = 700
app_width = 800

root = tk.Tk()
root.title("Program: Statystyki tekstu.")

#initialize variables
filename = StringVar()
case_sensible_setting = IntVar()
pickle_datalog = "text_stat_app.pkl"
app_log_file = "text_stat_app_log.txt"

#initialize app
canvas = tk.Canvas(root, height=app_height, width=app_width)
canvas.pack()

frame = tk.Frame(root)
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

title_label = tk.Label(frame, text="Witaj. Poniżej masz opcję wybrania pliku, który poddany zostanie analizie.\n")
title_label.pack()

pick_a_file_button = ttk.Button(frame, text = "Wybierz plik do analizy.", command = pick_a_file)
pick_a_file_button.pack()

case_checkbox = ttk.Checkbutton(frame, text="Zaznacz jeśli chcesz by analiza tesktu w pliku przebiegała uwzględniając wielkość liter.",variable=case_sensible_setting)
case_checkbox.pack()

analyze_button = ttk.Button(frame, text = "Analizuj dane z podanego pliku.", state=DISABLED, command = lambda i=case_sensible_setting.get(): analyze())
analyze_button.pack()

log_title_label = tk.Label(frame, text="\nLog na żywo:\n")
log_title_label.pack()

log_frame = tk.Frame(root, bg='grey', bd=1)
log_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

log_text = tk.Text(log_frame)
log_text.place(relwidth=1, relheight=1)

add_live_log_entry("Witaj! Program Statystyki Tekstu zaczyna sie.", True, 1)

root.mainloop()

add_live_log_entry("Koniec programu Statystyki Tekst.", False)

exit()
