def sciezki():
    import sys
    import os
    print("Sciezka wyszukiwania Python: ", sys.path)
    print("Aktualny folder roboczy: ", os.getcwd())

#sciezki()

#moduły python: pypi.org



def przyklady():

    print("import całego modułu")
    import mytestmodul
    mytestmodul.hello()

    print("alternatywnie import jednej metody z modułu")
    from mytestmodul import hello
    hello()

    print("import metody pod innym aliasem mając już swoją metodę o podanej nazwie")
    def hello():
        print("Inne siema")
    from mytestmodul import hello as myTestHello
    hello()
    myTestHello()

    print("import z innego katalogu (mającego __init__.py)")
    import moduls_ext.mySecondTestModul as my2
    my2.bye()
    print(my2.add(1,2,45,12))
    print(my2.add(1,2,3))

#przyklady()

def przyklady2():

    import os
    import send2trash

    filename = os.getcwd()+"\\file2bedeleted3.txt"
    print("Moj plik:",filename)
    open(filename, 'w').close()
    # with open(filename, 'w') as book_file:
    #      print("File was created")

    #wysłanie pliku do kosza
    send2trash.send2trash(filename)

    #uruchomienie notepada
    os.system("notepad.exe")


#przyklady2()

def mail_example():
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart



    login = "isapy@int.pl"
    password = "isapython;"
    server_adress = "poczta.int.pl"
    auth = "SSL"

    #subject = input("Podaj tytul wiadomosci: ")
    #body = input("Podaje tresc wiadomosci: ")
    #recipiant = input("Podaj adresata wiadomosci: ")
    subject = "Lukasz pozdrawia"
    body = "wszystkich czytajacych"
    recipiant = login

    mail_body = MIMEText(body)
    mail = MIMEMultipart()
    mail.attach(MIMEText(file("text.txt").read()))
    mail['Subject'] = subject
    mail['From'] = login
    mail['To'] = recipiant
    mail.attach(mail_body)

    server = smtplib.SMTP(server_adress)
    if auth=="SSL":
        server.starttls() #wlaczenie SSL (szyfrowane połączenie)
    server.login(login, password)
    server.send_message(mail)
    server.quit()

mail_example()

praca domowa wyslac zalacznik