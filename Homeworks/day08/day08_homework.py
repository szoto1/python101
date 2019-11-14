#zadanie
# pobieranie obrazkow na dysk do katalogu images (zapisywac w nazwie takiej jak sa na stronie czyli zaczynajac od ostatniego slasza)
# zrobi miniaturki do images/thumbs i rozmiaru 64px szerowkosci (wysokosc proporcjonalna)
# policz ile jest zdjec na stronie
# wyslij maila z informacja ile zdjec sciagnieto,
# jaki jest sumaryczny rozmiar zdjec w MB (i ile MB zaoszczedzilem robiac miniaturki)
# dopisz w mailu jaka jest pogoda w Gdansku

import requests
from bs4 import BeautifulSoup
import os

def saveimg2disk(image_adress,image_name, where2save):

    img = requests.get(image_adress)

    with open(where2save+image_name, 'wb') as file:
        file.write(img.content)

    return file_size(where2save+image_name), where2save+image_name

def getthoseimages(www, savedir):

    page = requests.get(www) #fetching page
    parser = BeautifulSoup(page.content, "html.parser") #pass what to parse and parser type
    images = parser.find_all('img') #looking for images

    images_size_all = 0
    all_images_paths = []
    for image in images:
        image_adress = www+image['src'] #getting all the adressess of all the images
        image_name = image_adress.split("/")[-1]
        image_size, image_path = saveimg2disk(image_adress,image_name,savedir)
        all_images_paths.append(image_path)
        images_size_all = images_size_all+image_size

    return images_size_all, all_images_paths

def file_size(file_path):

    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return file_info.st_size

def mini(list_with_paths):

    size_after = 0
    for img in list_img_paths:
        #resize those

    return size_after



#Main program

www = 'https://wallpaperlist.com'
images_dir = os.getcwd()+"\\images\\" #add checking if dir exists if not create
thumbs_dir = images_dir+"thumbs\\" #add checking if dir exists if not create
images_bytes, list_img_paths=getthoseimages(www, images_dir)
images_bytes_after = mini(list_img_paths)

print(images_bytes)
print(list_img_paths)



