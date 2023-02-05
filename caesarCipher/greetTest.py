def greet():
    print('Good Morning')
    print('Today is a good Day')
    print('lets learn some Python today.')

greet()

def greet_with_name(name, location): # here name is a parameter
    print(f'Good Morning {name}')
    print(f'How is weather in {location} ? ')
    print(f'lets learn some Python {name}!!')

greet_with_name('Aman','Bhopal') # example of positional argument
greet_with_name(location='Jaipur',name='Amit') # example of keyword arguments