#@@ -1,27 +1,28 @@
# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.
# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

class Matrix:

    #Заполнение матрицы
    def __init__(self, rows = 10, columns = 10, number = None):
       self.field = [[number for i in range(columns)] for j in range(rows)]
       self.rows = rows
       self.columns = columns

    #Замена существующих значений   
    def new_values(self, new_number=None):
        self.number = new_number 
        self.__init__(self.rows, self.columns, new_number)    

    #Замена выборочных существующих значений   
    def new_values_ij(self, i, j, new_value = None):
        self.field[i][j] = new_value

    #Вывод числа строк и колонок
    def len_rows_columns(self):
        print(f'Матрица состоит из {self.rows} строк и {self.columns} колонок')      

    def print_matrix(self):
        print('Матрица:')
        for row in m.field:            
            print(' '.join([str(elem) for elem in row])) 
    
m = Matrix(3, 4, 5)
m.print_matrix()

m.len_rows_columns()

m.new_values(6)
m.print_matrix()

m.new_values_ij(0,0,7)
m.print_matrix()

#Второй способ
print('-'*10)
class MatrixNew:

    #Заполнение матрицы
    def __init__(self, rows = 10, columns = 10):
       self.field = [[i * j for j in range(columns)] for i in range(rows)]
       self.rows = rows
       self.columns = columns
       
    #Замена существующих значений   
    def new_values(self, new_value = None):
        self.field = [[new_value for i in range(self.columns)] for j in range(self.rows)]
        
    #Замена выборочных существующих значений   
    def new_values_ij(self, i, j, new_value = None):
        self.field[i][j] = new_value     
        
    #Вывод числа строк и колонок
    def len_rows_columns(self):
        print(f'Матрица состоит из {self.rows} строк и {self.columns} колонок')      

    def print_matrix(self):
        print('Матрица:')
        for row in self.field:            
            print(' '.join([str(elem) for elem in row])) 
    
m = MatrixNew(4, 5)
m.print_matrix()

m.len_rows_columns()

m.new_values(7)
m.print_matrix()

m.new_values_ij(0,1,)
m.print_matrix()





