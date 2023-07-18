# Задача 1.4.

# Есть словарь кодов товаров titles

titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}

# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.

store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}
for product in titles:
    code = titles[product]
    p_q = store[code]
    sum_q = 0
    sum_p = 0
    sum_p_q = 0
    for i in range(len(p_q)): 
        sum_q += p_q[i][list(p_q[i])[0]]   
        sum_p += p_q[i][list(p_q[i])[1]] 
        sum_p_q += sum_q * sum_p
    print(product, '-', sum_q, 'шт, стоимость', sum_p_q, 'руб')

print('-'*10)
for product, code in titles.items():
    sum_q1 = 0
    sum_p1 = 0
    sum_p_q1 = 0
    for p_q in store[code]: 
        sum_q1 += p_q['quantity']
        sum_p1 += p_q['price']
        sum_p_q1 += sum_q1 * sum_p1
    print(product, '-', sum_q1, 'шт, стоимость', sum_p_q1, 'руб')    
    
       
         
    
# Рассчитайте на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"

# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"
