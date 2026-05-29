class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0

    def describe_restaurant(self):
        print("Название ресторана:", self.restaurant_name)
        print("Тип кухни:", self.cuisine_type)

    def open_restaurant(self):
        print("Ресторан открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, location, work_hours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
        self.location = location
        self.work_hours = work_hours
        self.stick_ice_cream = []
        self.soft_ice_cream = []

    def show_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print("-", flavor)

    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        print("Добавлен сорт:", flavor)

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print("Удалён сорт:", flavor)
        else:
            print("Такого сорта нет:", flavor)

    def has_flavor(self, flavor):
        if flavor in self.flavors:
            print(flavor, "есть в наличии!")
        else:
            print(flavor, "нет в наличии!")

    def describe_cafe(self):
        print("Кафе-мороженое:", self.restaurant_name)
        print("Локация:", self.location)
        print("Время работы:", self.work_hours)

    def add_stick_ice_cream(self, flavor):
        self.stick_ice_cream.append(flavor)
        print("Добавлено мороженое на палочке:", flavor)

    def add_soft_ice_cream(self, flavor):
        self.soft_ice_cream.append(flavor)
        print("Добавлено мягкое мороженое:", flavor)

    def show_stick_ice_cream(self):
        print("Мороженое на палочке:")
        for flavor in self.stick_ice_cream:
            print("-", flavor)

    def show_soft_ice_cream(self):
        print("Мягкое мороженое:")
        for flavor in self.soft_ice_cream:
            print("-", flavor)


cafe = IceCreamStand("Мороженое Радуга", "Кафе-мороженое", "ул. Садовая, 15", "10:00 - 22:00")

cafe.describe_cafe()
print()
cafe.flavors = ["Ванильное", "Шоколадное", "Клубничное"]
cafe.show_flavors()
print()
cafe.add_flavor("Фисташковое")
cafe.show_flavors()
print()
cafe.remove_flavor("Клубничное")
cafe.show_flavors()
print()
cafe.has_flavor("Шоколадное")
cafe.has_flavor("Карамельное")
print()
cafe.add_stick_ice_cream("Эскимо")
cafe.add_soft_ice_cream("Крем-брюле")
print()
cafe.show_stick_ice_cream()
cafe.show_soft_ice_cream()