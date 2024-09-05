import requests
import ctypes
import os
#from PIL import Image

api_url = "https://api.nasa.gov/planetary/apod?api_key=YRzChhPCV42v2InCxAbCEbDjOdg1qZDhNqV2NIlw"
apod = requests.get(api_url)
imgUrl = apod.json()['hdurl']
img = requests.get(imgUrl)

file = open('astro', 'wb')
file.write(img.content)
file.close()
PATH = os.path.abspath('astro')

#vImage = Image.open(PATH)
#if vImage.height > vImage.width:
#    rotated_image = vImage.rotate(90, expand=True)
#    rotated_image.save(PATH, format = 'JPEG')

ctypes.windll.user32.SystemParametersInfoW(20, 0, PATH, 3)

os.remove(PATH)