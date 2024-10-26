#Декоратор — це функція, яка приймає іншу функцію як аргумент,
# і часто всередині декоратора визначається функція wrapper.
# Ця внутрішня функція (wrapper) обгортає оригінальну функцію,
# виконуючи певні додаткові операції до та/або після її виклику.
# Потім wrapper повертається з декоратора і фактично замінює
# вихідну функцію


#pr


import datetime


def star_decorator(func):
    def wrapper():
        print("***************")
        func()
        print("***************")
    return wrapper

def text_decorator(func):
    def wrapper():
        print("**Current time**")
        func()
        print("**Spent time with benefit!**")
    return wrapper

@star_decorator
@text_decorator
def show_current_time():
    current_time = datetime.datetime.now().strftime("%H:%M ")
    print(f"Поточний час: {current_time}")


show_current_time()



#Pizza
def pizza_base():
    return "Основа для піци з томатним соусом та сиром"
def margherita_decorator(func):
    def wrapper():#внутрішня функція всередині декоратора, яка обертає основну функцію, щоб додати додаткову функціональність до неї без зміни вихідного коду.
        base = func()
        return f"{base}, базилік та моцарела"
    return wrapper
def four_cheeses_decorator(func):
    def wrapper():
        base = func()
        return f"{base}, пармезан, дорблю, чедер, моцарела"
    return wrapper
def capricciosa_decorator(func):
    def wrapper():
        base = func()
        return f"{base}, гриби, артишоки, шинка, оливки"
    return wrapper

def hawaiian_decorator(func):
    def wrapper():
        base = func()
        return f"{base}, ананас та шинка"
    return wrapper

@margherita_decorator
def margherita():
    return pizza_base()

@four_cheeses_decorator
def four_cheeses():
    return pizza_base()

@capricciosa_decorator
def capricciosa():
    return pizza_base()

@hawaiian_decorator
def hawaiian():
    return pizza_base()


print("Піца Маргарита:", margherita())
print("Піца Чотири сири:", four_cheeses())
print("Піца Капричоза:", capricciosa())
print("Піца Гавайська:", hawaiian())


#dz1
import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання: {end_time - start_time:.5f} секунд")
        return result
    return wrapper

@timer_decorator
def get_primes(limit=1000):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

primes = get_primes()
print(f"Прості числа від 0 до 1000: {primes}")
@timer_decorator
def get_primes_in_range(start=0, end=1000):
    primes = []
    for num in range(max(2, start), end + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

primes = get_primes_in_range(100, 500)
print(f"Прості числа від 100 до 500: {primes}")

#dz3фін звіти ???


