# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"
line = str(input('Введите строку:'))

def remove_exclamation_marks(s):
    res_s_1 = s.replace('!','')
    return res_s_1

print('Строка "' + line + '" после удаления всех "!" -> "' + remove_exclamation_marks(line) + '"')
""
# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if s.endswith('!',-1) == True:
        res_s_2 = s[0:-1]
    else:
        res_s_2 = s
    return res_s_2
    
print('Строка "' + line + '" после удаления последнего "!" == "' + remove_last_em(line) + '"')

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):

    
    split_s = s.split(' ')
    a = ''
    for i in range(len(split_s)):
        if split_s[i].count('!') != 1:
            a += str(split_s[i])
    return a

print('Предложение "' + line + '" после удаления слов, содержащих один "!" == "' + remove_word_with_one_em(line) + '"')