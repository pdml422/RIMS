class Dish:
    def __init__(self, category, name, price, sold):
        self.__category = category
        self.__name = name
        self.__price = price
        self.__sold = sold

    def set_category(self, category):
        self.__category = category

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price

    def set_sold(self, sold):
        self.__sold = sold

    def _get_category(self):
        return self.__category

    def _get_name(self):
        return self.__name

    def _get_price(self):
        return self.__price

    def _get_sold(self):
        return self.__sold

dish_list = []
with open("data/menu.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        fields = line.split(",")
        dish = Dish(fields[0], fields[1], fields[2], fields[3])
        dish_list.append(dish)
