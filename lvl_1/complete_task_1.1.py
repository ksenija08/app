# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# Первый способ
splited_my_favorite_songs = my_favorite_songs.split(', ')
print(splited_my_favorite_songs[0], splited_my_favorite_songs[-1], splited_my_favorite_songs[1], splited_my_favorite_songs[-2], sep = '\n')

# Второй способ
print(my_favorite_songs[0:13], my_favorite_songs[64:77], my_favorite_songs[16:30], my_favorite_songs[51:62], sep = '\n')

# Третий способ
i = []
a = 0
x = 1
b = len(my_favorite_songs)
for j in range(my_favorite_songs.count(',')):
    c =  my_favorite_songs.index(',',a,b)
    i.append(c)
    a = c + 1
print(my_favorite_songs[0:i[0]], my_favorite_songs[i[-1]+2:-1], my_favorite_songs[i[0]+2:i[1]],my_favorite_songs[i[-2]+2:i[-1]], sep = '\n')

# Четвертый способ
print(my_favorite_songs[:my_favorite_songs.find(',')], 
      my_favorite_songs[my_favorite_songs.rfind(',')+2:-1], 
      my_favorite_songs[my_favorite_songs.find(',')+2 :my_favorite_songs.find(',') + my_favorite_songs[my_favorite_songs.find(',')+1:-1].find(',')],
      my_favorite_songs[my_favorite_songs[:my_favorite_songs.rfind(',')].rfind(',')+2:my_favorite_songs.rfind(',')],  sep = '\n')