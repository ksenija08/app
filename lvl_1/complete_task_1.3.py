# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!
# Первый вариант
number = int(input('Введите номер месяца:'))
months = ['январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь' ]
months_1 = [1, 3, 5, 7, 8, 10, 12]
months_2 = [4, 6, 9, 11]
months_3 = [2]
if number in months_1:
    print('Вы ввели', months[number-1] + '. 31 дней') 
elif number in months_2:
    print('Вы ввели', months[number-1] + '. 30 дней') 
elif number in months_3:
    print('Вы ввели', months[number-1] + '. 28 дней')    
else:
    print('Такого месяца нет!')   
# Второй вариант
number = int(input('Введите номер месяца:'))
months = {
    'январь':31,'февраль':28,'март':31,'апрель':30,'май':31,'июнь':30,'июль':31,'август':31,'сентябрь':30,'октябрь':31,'ноябрь':30,'декабрь':31}
if 1 <= number <= len(list(months)):
    month = list(months)[number-1]
    print('Вы ввели', month + '.', months[month], 'дней' ) 
else:
    print('Такого месяца нет!')          
