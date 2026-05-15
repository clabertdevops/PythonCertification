# funzioni interne che sfruttano le variabili passate dalla funzione principale
def create_greeting(message):
    # 'messaggio' è una variabile libera:
    # non è locale a saluta() né globale
    def greet(name):
        return f'{message} {name}!'
    return greet

hello = create_greeting("Hello")
goodbye = create_greeting("Goodbye")

print(hello("Bob"))
print(goodbye("Mary"))

def cont_init(start): 
    def increment(step):
        return start + step
    return increment

f = cont_init(10)
print(f.__closure__) # (<cell at 0x...: int object at 0x...>,)
print(f.__closure__[0].cell_contents) # 10
print(f.__code__.co_freevars) # ('start',)




def outer_func():
    message = 'Func'

    def inner_func():
        print(message)
    
    # return inner_func() se ritorni con le parentesi viene passata l'esecuzione della funzione 
    return inner_func # senza parentesi l'esecuzione della funzione avviene quando viene chiamata la variabile che la contiene

my_func = outer_func()
my_func()
my_func()

def outer_func_parameter(message):
    

    def inner_func():
        print(message)
    
    return inner_func

hi_function = outer_func_parameter("HI")
hello_function = outer_func_parameter("Hello")

hi_function()
hello_function()

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times_3 = make_multiplier_of(3)
times_5 = make_multiplier_of(5)
print(times_3(9))
print(times_5(9))

print(times_5(times_3(2)))

'''
All function objects have a __closure__ attribute 
that returns a tuple of cell objects if it is a closure function.
'''

print(times_3.__closure__)
print(times_3.__closure__[0].cell_contents) # 3