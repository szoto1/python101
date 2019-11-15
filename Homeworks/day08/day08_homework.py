import os
from Homeworks.day08.day08_modules import *

#Main program

#checking different OSes to find directories paths for images

dir_div = directory_div()
www = 'https://wallpaperlist.com'
thumb_new_width = 64
images_dir = os.getcwd()+dir_div+"images"+dir_div   #add checking if dir exists if not create
thumbs_dir = images_dir+"thumbs"+dir_div            #add checking if dir exists if not create
img_numb, images_bytes, list_img_paths = getthoseimages(www, images_dir)

images_bytes_after = mini(list_img_paths,thumbs_dir,thumb_new_width)

saved_space = images_bytes - images_bytes_after


print("Number of images on page: ", img_numb)
print(bytes_to_human(images_bytes))
print(bytes_to_human(images_bytes_after))

checked_weather = checkweather("Gdansk")

subject = "Lukasz - zdjecia i pogoda."
recipiant = "isapy@int.pl"
#recipiant = "shotofsky@gmail.com"
body="Hej,\n" \
     "na stronie: " + www + "\n" \
     "zdjec bylo: " + str(img_numb) + ".\n" \
     "Rozmiar pobranych zdjec: " + bytes_to_human(images_bytes) + "\n" \
     "Rozmiar zdjec po pomniejszeniu: " + bytes_to_human(images_bytes_after) + "\n" \
     "Zaoszczedzilismy po pomniejszeniu: " + bytes_to_human(images_bytes-images_bytes_after) + "\n\n" + checked_weather + "\n\n" + "Pozdrawiam, Lukasz Sz."

send_simple_mail(subject, body, recipiant)