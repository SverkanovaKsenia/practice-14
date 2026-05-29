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
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print("-", flavor)


ice = IceCreamStand("Мороженое Радуга", "Кафе-мороженое")
ice.flavors = ["Ванильное", "Шоколадное", "Клубничное"]
ice.show_flavors()