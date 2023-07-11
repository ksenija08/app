# Задача 2
# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
import random
import datetime

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
min = 0
random_song = []
random_songs = random.sample(my_favorite_songs, 3)
for i in range(3):
    min += random_songs[i][1] 
    random_song.append(random_songs[i][0])
second = round(min * 60)  
time_format = str(datetime.timedelta(seconds = second))
print('Три песни звучат', round(min, 2), 'минут')  
print('Три песни:', ', ' .join(random_song),'звучат',round(min, 2), 'минут')  
print(time_format)

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
min_dict = 0
random_songs_dict = random.sample(list(my_favorite_songs_dict), 3)
for song in random_songs_dict:
    random_song_dict_min = my_favorite_songs_dict[song]
    min_dict += random_song_dict_min     
second = round(min_dict * 60)  
time_format = str(datetime.timedelta(seconds = second))   
print(f"Три песни звучат {round(min_dict, 2)} минут.") 
print(f"Три песни: {', '.join(random_songs_dict)} - звучат {round(min_dict, 2)} минут.") 
print(f"{round(min_dict, 2)} минут -> {time_format}")

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 