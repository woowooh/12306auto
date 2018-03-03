import random
import requests
import time
import constants
from PIL import Image
from threading import Thread


def captcha_url():
    url = constants.CHA_PT_PAGE
    rand = random.random()
    return url[:-18] + str(rand)


def save_image(name, image_data):
    with open(name, 'wb') as f:
        f.write(image_data)
    image_name = f_change(name, "ppm")
    return image_name


def f_change(name, suffix):
    img = Image.open(name)
    new_name = name.split('.')[0] + '.' + str(suffix)
    img.save(new_name)
    return new_name


def mul_thread(func):
    def wrapper(*args, **kwargs):
        t = Thread(target=func, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
    return wrapper

