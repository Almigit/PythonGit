# Создать 3 класса:
# Salad, Main_dish, Drink

# в этих классах создать поля name(строка), price(инт), dish_of_the_day(булеан)

# так же в этих классах создать функцию show_price, которая будет 
# выводить на экран стоимость блюда в рублях. 
# При этом, если блюдо является блюдом дня, то из стоимости вычесть 50 рублей

# создать по 3 объекта каждого из классов с разным блюдом и добавить в лист menu

# написать функцию print_menu, с аргументом нашего листа меню - menu,
# используя for пройтись по всему листу и вывести на экран меню для клиента
# (название каждого блюда и стоимость (стоимость выводить функцией show_price))

# для вывода на экран использовать функцию print_menu, оформить по усмотрению, но так, чтобы пользователю было понятно

# создаю первый класс "Salad"
class Salad:
    def __init__(self, name, price, dish_of_the_day):
        self.name = name
        self.price = price
        self.dish_of_the_day = dish_of_the_day
    
    def show_price(self):
        if self.dish_of_the_day == True:
            self.price -= 50
            print(self.name + ": " + str(self.price))
        else:
            print(self.name + ": " + str(self.price))

# создаю объекты
salad1 = Salad("Olivier", 100, True)
salad2 = Salad("Vinegret",150, False)
salad3 = Salad("Shuba", 200, False)

# Создаю второй класс "Main_dish"
class Main_dish:
    def __init__(self, name, price, dish_of_the_day):
        self.name = name
        self.price = price
        self.dish_of_the_day = dish_of_the_day
    def show_price(self):
        if self.dish_of_the_day == True:
            self.price -= 50
            print(self.name + ": " + str(self.price))
        else:
            print(self.name + ": " + str(self.price))

# создаю объекты
main_dish1 = Main_dish("Solyanka", 200, True)
main_dish2 = Main_dish("Mashed potatoes with chicken", 250, False)
main_dish3 = Main_dish("Noodles with sausages", 230, False)

# Создаю третий класс "Drink"
class Drink:
    def __init__(self, name, price, dish_of_the_day):
        self.name = name
        self.price = price
        self.dish_of_the_day = dish_of_the_day
    def show_price(self):
        if self.dish_of_the_day == True:
            self.price -= 50
            print(self.name + ": " + str(self.price))
        else:
            print(self.name + ": " + str(self.price))

# создаю объекты
drink1 = Drink("Coffee", 120, True)
drink2 = Drink("Tea", 60, False)
drink3 = Drink("Orange juice", 80, False)

# создаю лист меню
menu = [salad1, salad2, salad3, main_dish1, main_dish2, main_dish3, drink1, drink2, drink3]

# создаю функцию print_menu
def print_menu():
    print("Menu")
    print("--------------------")
    for item in menu:
        item.show_price()
    print("--------------------")
    print("Note: all prices are specified in rubles")

print_menu()
