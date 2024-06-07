#Задайте переменные разных типов данных:
#  - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
#  - Выполните операции вывода кортежа immutable_var на экран.
#3. Изменение значений переменных:
#  - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
#4. Создание изменяемых структур данных:
#  - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
#  - Измените элементы списка mutable_list.
#  - Выведите на экран измененный список mutable_list.

immutable_var = 'Down Bad', 4, True, 'TTPD'
print(immutable_var)
# immutable_var[0] = 'The Alchemy'
# кортежи не поддерживают изменение элемента
mutable_list = ['Lavander Haze', 6, False, 'Midnights']
mutable_list[0] = 'Midnight Rain'
mutable_list[2] = True
mutable_list.append('Ms. Swift')
print(mutable_list)
