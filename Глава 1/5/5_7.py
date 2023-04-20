countries = {'Россия' : 'Москва', 'США' : 'Вашингтон', 'Германия' : 'Берлин', 'Франция' : 'Париж', 'Китай' : 'Пекин'}

country = input()
for i in countries:
    #for capital in countries.value():
    if country == i:
        for capital in countries.values():
            print(capital)
    else:
        print('Такой страны в словаре нет')