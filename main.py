with open(r'F:\fileopen homework\enter.txt', 'rt') as f:
    cook_book = {}
    for line in f:
        dish = line.strip()
        number = int(f.readline())
        ingridients = []
        for i in range(number):
            x = f.readline().strip()
            ingr, quantity, measure = x.split(' | ')
            ingridients.append({
                'ingr' : ingr,
                'quantity' : quantity,
                'measure' : measure
            })
        f.readline()
        cook_book[dish] = ingridients


def func(income_list, person):
    sort ={}
    for dish in dish_list:
        for x in cook_book[dish]:
            a = x.pop('ingr')
            b = x.pop('quantity')
            x['quantity'] = int(b) * person
            sort[a] = x
    return sort

x = 2
dish_list = ['Омлет', 'Фахитос']

print(func(dish_list,x))
print(cook_book)