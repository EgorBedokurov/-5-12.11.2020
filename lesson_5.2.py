#Вариант №1
some_text = 'make America great again'
print('Количество символов, включая пробелы - ', len(some_text)) # число символов
print('Количество символов, без пробелов - ', len(some_text) - len(some_text.split(' ')) + 1) #число символов без пробелов (отнимаем пробелы)
print('Количество слов - ', len(some_text.split())) #число слов


#Вариант №2
some_text2 = 'peace Labor may'
print('Количество символов, включая пробелы - ', len(some_text2))# число символов
print('Количество символов, без пробелов - ', len(some_text2) - some_text2.count(' '))# число символов без пробелов (отнимаем пробелы)
print('Количество слов - ', some_text2.count(' ') + 1)# число слов по количеству пробелов
