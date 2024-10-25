
import pandas as pd
from PIL import Image





file_name = 'Данные по турагенству.csv'
pd.read_csv(file_name, delimiter=',')
article_read = pd.read_csv(file_name, delimiter=';',
    names = ['my_datetime', 'event', 'country',
	    'user_id', 'source', 'topic'])



res1 = article_read.sample(3)       #вывод случайного количества строк
print(res1)

res2 = article_read.head()[['user_id', 'topic']]     # вывод определенных данных
print(res2)

res3 = article_read[article_read.topic == 'Asia']      # фильтрация данных
print(res3)




file_image = 'мячик.jpg'
def resize_image(image_path):             #  изменяем размер изображения
    image = Image.open(image_path)
    image = image.resize((1280, 500))
    image.save(image_path)

def change_color(image_path):       #  изменяем цветовую гамму изображения
    image = Image.open(image_path)
    image = image.convert('L')
    image.save(image_path)

def new_format(image_path):          #   изменяем формат
    image = Image.open(image_path)
    image.save(image_path, 'png')



resize_image(file_image)
change_color(file_image)
new_format(file_image)