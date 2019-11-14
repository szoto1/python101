# wywołanie własnego wyjatku
# raise ValueError("Komunikat errora")

#from PIL import Image
# foto=image.open(plik)

def simpledebug():
    days = ['poniedzialek', 'wtorek', 'sroda', 'czwartek','piatek','sobota','niedziela']
    weekend = ('sobota', 'niedziela')

    for day in days:
        # print(day)
        if day in weekend:
            print("Weekend!")
        else:
            print("Do pracy!")


# simpledebug()

def photo():

    from PIL import Image

    # file = "C:\\Users\Szo\Desktop\moj.JPG"
    file = r"C:\Users\Szo\Desktop\moj.JPG"
    new_file = r"C:\Users\Szo\Desktop\moj_nowy.jpg"
    new_file2 = r"C:\Users\Szo\Desktop\moj_nowy2.jpg"
    image: Image.Image = Image.open(file)
    # image.show() #open i default browser
    image = image.resize((64,64)) #resizing open image
    image.save(new_file) #saving to new file
    image2: Image.Image = Image.open(new_file) #opening new resized file
    image2.show()

    image = image.rotate(90)
    image.save(new_file2)

    image3: Image.Image = Image.open(new_file2)  # opening new rotated file
    image3.show()

# photo()

def pogoda():

    import requests

    # wp_page = requests.get('https://wp.pl')
    # print(wp_page.text)

    api_key = "800101cc05e0bcd5b88c816246c988ff"
    api_host = "http://api.openweathermap.org/data/2.5/weather"
    city = "Gdansk"

    api_adress = f'{api_host}?appid={api_key}&q={city}'
    print("API builded adress is: ",api_adress) #building api adress for my city

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

    print(f"temperatura: {dict['main']['temp']} (Fahrenheitow)")
    print(f"wiatr: {dict['wind']['speed']} m/s")
    print(f"cisnienie: {dict['main']['pressure']}")



    # http://api.openweathermap.org/data/2.5/weather?appid=800101cc05e0bcd5b88c816246c988ff&q=Gdansk
    # print(wp_page.text)
    # print(result.json())

# pogoda()

def bjutisoap():
    #parser
    import requests
    from bs4 import BeautifulSoup

    www = 'https://wallpaperlist.com'
    page = requests.get(www) #fetching page

    # print(page.content)

    parser = BeautifulSoup(page.content, "html.parser") #pass what to parse and parser type
    # print(parser)
    images = parser.find_all('img') #looking for images

    for image in images:
        print(www+image['src']) #getting all the adressess of all the images

# bjutisoap()




