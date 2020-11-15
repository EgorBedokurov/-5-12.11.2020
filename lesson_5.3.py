print('что будем вычеслять? \
если треугольник, введите "tr", \
если квадрат - "sq" ' )
figure = str(input(''))
if figure == 'tr':
        a = int(input('длина первого катета '))
        b = int(input('длина второго катета '))
if figure == 'sq':
        c = int(input('длина стороны фигуры '))
        
        
def area_form():
    if figure == 'tr':
        ar = a*b/2 # принимаем, что треугольник прямоуголный
    if figure == 'sq':
        ar = c*c
    return ar
    
print(area_form(), str('кв.см'))
