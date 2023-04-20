countries = {'Россия' : 'Москва', 'США' : 'Вашингтон', 'Германия' : 'Берлин', 'Франция' : 'Париж', 'Китай' : 'Пекин'}

for country in countries:
    print('Столицей', country, 'является', countries[country])
    
for country, capital in countries.items():
        print(country, capital)

for country in countries.keys():
    print('Страна:', country)

for capital in countries.values():
    print('Столица:', capital)