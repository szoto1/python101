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
    # mail.attach(MIMEText(file("text.txt").read()))
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

# mail_example()

def mail_example2():

    import smtplib
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    login = "isapy@int.pl"
    password = "isapython;"
    server_adress = "poczta.int.pl"
    auth = "SSL"

    subject = input("Tytul wiadomosci: ")
    sender_email = "Pan Kleks <"+login+">"
    receiver_email = login

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    body = input("Tresc wiadomosci: ")
    message.attach(MIMEText(body, "plain"))

    filename = "text.txt"
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream") # The content type "application/octet-stream" means that a MIME attachment is a binary file
        part.set_payload(attachment.read())
        encoders.encode_base64(part) # Encode to base64
        part.add_header("Content-Disposition", f"attachment; filename= {filename}")
        message.attach(part)

    text = message.as_string()
    # sending my mail
    server = smtplib.SMTP(server_adress)
    if auth=="SSL":
        server.starttls() #wlaczenie SSL (szyfrowane połączenie)
    server.login(login, password)
    server.sendmail(sender_email, receiver_email, text)
    server.quit()


mail_example2()