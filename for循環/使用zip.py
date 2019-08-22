days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

print('原方法：')
for i in range(len(days)):
    print(days[i], ": drink", drinks[i], "- eat", fruits[i], "- enjoy", desserts[i])

print('\nzip()用法：')
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)


english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'

print('轉換成list包tuple')
print(list( zip(english, french) ))
print('轉換成Dictionarie')
print(dict( zip(english, french) ))