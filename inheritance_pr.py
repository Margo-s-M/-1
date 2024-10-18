class Money:
    def __init__(self,whole_money, coin_money,currency="USD"):
        self.whole_money = whole_money
        self.coin_money = coin_money
        if 0 <= coin_money < 100:
            self.coin_money = coin_money
            self.currency = currency
    def display(self):
        print(f"{self.whole_money}{self.currency} {self.coin_money} peny")

    def add_money(self,money,coins):
        oll_coins = self.coin_money + coins
        oll_money = self.whole_money +money
        if  oll_coins >=100:
            oll_money += oll_coins //100
            oll_coins = oll_coins % 100

        self.whole_money = oll_money
        self.coin_money = oll_coins

    def get_money(self):
        return self.whole_money+self.coin_money/ 100

my_money = Money(10,25)
my_money.display()
my_money.add_money(3,75)
my_money.display()
print("extended amount :",my_money.get_money())


#PR1 Device
class Device():
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power
    @staticmethod
    def turn_on(self):
        return f"{self.brand} {self.model} увімкнено."
    @staticmethod
    def turn_off(self):
        return f"{self.brand} {self.model} вимкнено."

class CoffeMachine(Device):
    def __init__(self, brand, model, power, water_capacity,coffee_beans_capacity):
        super().__init__(brand, model, power)
        self.water_capacity = water_capacity
        self.coffee_beans_capacity = coffee_beans_capacity

    def make_coffee(self):
        return (f"{self.brand} {self.model} готує каву з водою "
                f"{self.water_capacity} л та зернами "
                f"{self.coffee_beans_capacity} г.")

class Blender(Device):
    def __init__(self, brand, model, power, speed_settings):
        super().__init__(brand, model, power)
        self.speed_settings = speed_settings

    def blend(self):
        return (f"{self.brand} {self.model} "
                f"працює на {self.speed_settings} налаштуваннях швидкості.")

class MeatGrinder(Device):
    def __init__(self, brand, model, power, capacity):
        super().__init__(brand, model, power)
        self.capacity = capacity

    def grind_meat(self):
        return (f"{self.brand} {self.model} "
                f"має місткість {self.capacity} кг для м'яса.")

coffee_machine = CoffeMachine("Philips","EP082","1500","1.8","275")
blender = Blender("Philips","HR3041","1200","5")
meat_grinder = MeatGrinder("Kenwood","MG516","1600","2.2")
print(coffee_machine.make_coffee())
print(coffee_machine.turn_on())
print(blender.blend())
print(blender.turn_on())
print(meat_grinder.grind_meat())
print(meat_grinder.turn_on())


#pr 2 Ship
class Ship:
    def __init__(self, length, width, color, engine):
        self.length = length
        self.width = width
        self.color = color
        self.engine = engine

    def get_info(self):
        return f"Length: {self.length}, Width: {self.width}, Color: {self.color}, Engine: {self.engine}"

    def start_engine(self):
        return f"{self.color} ship's engine is starting!"


class Frigate(Ship):
    def __init__(self, length, width, color, engine, ship_type):
        super().__init__(length, width, color, engine)
        self.ship_type = ship_type

    def get_info(self):
        return (super().get_info() +
                f", Type: {self.ship_type}")


class Destroyer(Ship):
    def __init__(self, length, width, color, engine, num_missiles):
        super().__init__(length, width, color, engine)
        self.num_missiles = num_missiles

    def get_info(self):
        return (super().get_info() +
                f", Number of missiles: {self.num_missiles}")


class Cruiser(Ship):
    def __init__(self, length, width, color, engine, num_crew):
        super().__init__(length, width, color, engine)
        self.num_crew = num_crew

    def get_info(self):
        return (super().get_info() +
                f", Number of crew: {self.num_crew}")



frigate = Frigate(100, 20, "Gray", "Turbojet", "Military")
destroyer = Destroyer(120, 25, "Black", "Diesel", 30)
cruiser = Cruiser(150, 30, "Blue", "Nuclear", 1500)


print(frigate.get_info())
print(frigate.start_engine())

print(destroyer.get_info())
print(destroyer.start_engine())

print(cruiser.get_info())
print(cruiser.start_engine())

