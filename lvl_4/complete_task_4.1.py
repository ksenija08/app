# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4


#import sqlite3

#connection = sqlite3.connect("teachers.db")
#cursor = connection.cursor()
#query_1 = """CREATE TABLE Students(Student_Id Integer, Student_Name Text, School_Id Integer Primary key);"""
#cursor.execute(query_1)
#query_2 = """INSERT INTO Students VALUES(201, 'Иван', 1),(202, 'Петр', 2),(203, 'Анастасия', 3),(204, 'Игорь', 4);"""
#cursor.execute(query_2)
#connection.commit()
#connection.close()

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3
Id_Student = int(input('Введите номер студента: '))
def get_connection():
  connection = sqlite3.connect("teachers.db")
  return connection

def close_connection(connection):
  if connection:
    connection.close()  

def get_school_student_info(Student_Id):
  
    try:
      connection = get_connection()
      cursor = connection.cursor()
      sql_query = "SELECT Students.Student_id, Students.student_name, School.School_id, School.School_name FROM Students JOIN School ON Students.School_id = School.School_id WHERE Students.Student_id = ?;"
      cursor.execute(sql_query,(Student_Id,))
      records = cursor.fetchall()
      close_connection(connection)
      id_s = []      
      for row in records:
        id_s.append(row[0])
      if Student_Id in id_s:
        print ("Данные по школе и студенте")
        for row in records:
          print ("ID студента:", row[0])
          print ("Имя студента:", row[1])
          print ("ID школы:", row[2])
          print ("Название школы:", row[3])
      else:
        print('Студента с таким ID не существует!')
    except (Exception, sqlite3.Error) as error:
      print ("Ошибка в получении данных: ", error)

get_school_student_info(Id_Student)
