import math

a_squer = int(input('введите значение стороны квадрата - '))

def per_sq(a_squer): #функция для мериметра
    a = a_squer * 4
    return a

def diag_sq(a_squer): #функция диагонали
    b = math.pow(a_squer, 2) * 2 #возведение в степень из math
    return math.sqrt(b) #извлечение корня из math

def sq_sq(a_squer):
    c = math.pow(a_squer, 2)
    return math.ceil(c)

print('периметр квадрата - ', per_sq(a_squer))
print('диагональ квадрата - ', diag_sq(a_squer))
print('площадь квадрата - ', sq_sq(a_squer))