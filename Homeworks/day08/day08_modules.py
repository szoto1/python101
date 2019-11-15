def saveimg2disk(image_adress,image_name, where2save):
    import requests
    img = requests.get(image_adress)

    with open(where2save+image_name, 'wb') as file:
        file.write(img.content)

    return file_size(where2save+image_name), where2save+image_name

def getthoseimages(www, savedir):
    import requests
    from bs4 import  BeautifulSoup
    page = requests.get(www) #fetching page
    parser = BeautifulSoup(page.content, "html.parser") #pass what to parse and parser type
    images = parser.find_all('img') #looking for images
    img_len = len(images)
    images_size_all = 0
    all_images_paths = []
    for image in images:
        image_adress = www+image['src'] #getting all the adressess of all the images
        image_name = image_adress.split("/")[-1]
        image_size, image_path = saveimg2disk(image_adress,image_name,savedir)
        all_images_paths.append([image_path,image_name])
        images_size_all = images_size_all+image_size

    return img_len, images_size_all, all_images_paths

def file_size(file_path):
    import os
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return file_info.st_size

def checkos():
    import platform
    current_os = platform.system()

    if current_os == "Darwin":
        return "OSX"
    elif current_os == "Windows":
        return "WIN"
    elif current_os == "Linux":
        return "LIN"
    else:
        return None

def directory_div():
    operating_system = checkos()
    dir_div = ""
    if operating_system == 'OSX' :
        dir_div = "/"
    elif operating_system == "WIN" :
        dir_div = "\\"
    elif operating_system == "LIN" :
        dir_div = "/"
    else:
        print("Can't do much.")
        exit()
    return dir_div

def mini(list_with_paths,thumbs_dir,new_width=64):
    from PIL import Image
    size_after = 0
    width = 0
    height = 0
    new_height = 0
    for img in list_with_paths:

        org_img = img[0]
        org_img_name = img[1]
        new_img_name = "thumb_"+org_img_name
        new_img = thumbs_dir + new_img_name

        image: Image.Image = Image.open(org_img)
        width, height = image.size
        new_height = round(new_width*height / width)

        image = image.resize((new_width,new_height)) #resizing open image
        image.save(new_img) #saving to new file

        size_after = size_after + file_size(new_img)

    return size_after

    pass

def bytes_to_human(file_size_in_bytes):

    SIZE_UNITS = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']

    index = 0
    while file_size_in_bytes >= 1024:
        file_size_in_bytes /= 1024
        index = index + 1
    try:
        return f'{file_size_in_bytes} {SIZE_UNITS[index]}'
    except IndexError:
        return 'Something huuuuuuge!'


def send_simple_mail(subject, body, recipiant):

    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    login = "isapy@int.pl"
    password = "isapython;"
    server_adress = "poczta.int.pl"
    auth = "SSL"

    mail_body = MIMEText(body)
    mail = MIMEMultipart()
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

def checkweather(where):

    import requests
    api_key = "800101cc05e0bcd5b88c816246c988ff"
    api_host = "http://api.openweathermap.org/data/2.5/weather"
    city = where

    api_adress = f'{api_host}?appid={api_key}&q={city}'
    #print("API builded adress is: ", api_adress)  # building api adress for my city

    result = requests.get(api_adress)
    dict = result.json()
    # after debugginng and doing evaluate on this result I've got this for the content:
    # b'{"coord":{"lon":18.65,"lat":54.35},
    #    "weather":[{
    #       "id":800,
    #       "main":"Clear",
    #       "description":"clear sky",
    #       "icon":"01n"}],
    #    "base":"stations",
    #    "main":{"temp":275.42,"pressure":1016,"humidity":93,"temp_min":274.26,"temp_max":276.48},
    #    "visibility":7000,
    #    "wind":{"speed":1.5,"deg":170},
    #    "clouds":{"all":0},
    #    "dt":1573754398,
    #    "sys":{"type":1,"id":1696,"country":"PL","sunrise":1573711911,"sunset":1573742872},
    #    "timezone":3600,
    #    "id":3099434,
    #    "name":"Gdansk",
    #    "cod":200}'

    # http://api.openweathermap.org/data/2.5/weather?appid=800101cc05e0bcd5b88c816246c988ff&q=Gdansk
    # http://api.openweathermap.org/data/2.5/weather?appid=800101cc05e0bcd5b88c816246c988ff&q=Gdansk
    # print(dict)

    tempKelvin = dict['main']['temp']
    tempC = round(tempKelvin - 273.15)

    # print(f"temperatura: {dict['main']['temp']} (Kelvinow)")
    # print("temperatura: ",tempC," (Celcjusza)")
    # print(f"wiatr: {dict['wind']['speed']} m/s")
    # print(f"cisnienie: {dict['main']['pressure']} (hPa)")

    pressure = dict['main']['pressure']
    wind = dict['wind']['speed']

    weather = "Pogoda w: " + where + "\n" \
              "- temperatura (Celcjusze): " + str(tempC) + "\n" \
              "- cisnienie (hPa): " + str(pressure) + "\n" \
              "- wiatr (m/s): " + str(wind)

    return weather
    #

    # print(f"opis: {dict['weather'][0]['main']}")

    #
    # http://api.openweathermap.org/data/2.5/weather?appid=800101cc05e0bcd5b88c816246c988ff&q=Gdansk
    # print(wp_page.text)
    # print(result.json())

    # pogoda()

