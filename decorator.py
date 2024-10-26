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
