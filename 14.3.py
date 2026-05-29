from tkinter import *

class IceCreamStand:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.flavors = ["Ванильное", "Шоколадное", "Клубничное"]
        self.types = ["На палочке", "Мягкое"]

    def add_flavor(self, flavor):
        if flavor and flavor not in self.flavors:
            self.flavors.append(flavor)
            return True
        return False

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            return True
        return False

    def check_flavor(self, flavor):
        return flavor in self.flavors

    def add_type(self, type_name):
        if type_name and type_name not in self.types:
            self.types.append(type_name)
            return True
        return False

    def remove_type(self, type_name):
        if type_name in self.types:
            self.types.remove(type_name)
            return True
        return False

    def get_flavors(self):
        return self.flavors

    def get_types(self):
        return self.types

    def get_name(self):
        return self.name

    def get_cuisine(self):
        return self.cuisine

    def set_name(self, new_name):
        if new_name:
            self.name = new_name
            return True
        return False

    def set_cuisine(self, new_cuisine):
        if new_cuisine:
            self.cuisine = new_cuisine
            return True
        return False


cafe = IceCreamStand("Мороженое Радуга", "Кафе-мороженое")


def update_flavors_text():
    text = "Сорта мороженого (вкусы)\n"
    for flavor in cafe.get_flavors():
        text = text + "- " + flavor + "\n"
    flavors_label.config(text=text)


def update_types_text():
    text = "Типы мороженого\n"
    for type_name in cafe.get_types():
        text = text + "- " + type_name + "\n"
    types_label.config(text=text)


def update_info_display():
    info_label.config(text="Название: " + cafe.get_name() + "\nКухня: " + cafe.get_cuisine())



def add_flavor():
    flavor = flavor_entry.get()
    if cafe.add_flavor(flavor):
        flavor_entry.delete(0, END)
        update_flavors_text()
        status_label.config(text="Готово")
    else:
        status_label.config(text="Сорт уже есть")


def remove_flavor():
    flavor = flavor_entry.get()
    if cafe.remove_flavor(flavor):
        flavor_entry.delete(0, END)
        update_flavors_text()
        status_label.config(text="Удалён: " + flavor)
    else:
        status_label.config(text="Сорт не найден")


def check_flavor():
    flavor = flavor_entry.get()
    if flavor:
        if cafe.check_flavor(flavor):
            status_label.config(text=flavor + " есть в наличии!")
        else:
            status_label.config(text=flavor + " нет в наличии!")
    else:
        status_label.config(text="Введите сорт")


def add_type():
    type_name = type_entry.get()
    if cafe.add_type(type_name):
        type_entry.delete(0, END)
        update_types_text()
        status_label.config(text="Готово")
    else:
        status_label.config(text="Тип уже есть")


def remove_type():
    type_name = type_entry.get()
    if cafe.remove_type(type_name):
        type_entry.delete(0, END)
        update_types_text()
        status_label.config(text="Удалён тип: " + type_name)
    else:
        status_label.config(text="Тип не найден")


def check_type():
    type_name = type_entry.get()
    if type_name:
        if type_name in cafe.get_types():
            status_label.config(text=type_name + " есть в наличии!")
        else:
            status_label.config(text=type_name + " нет в наличии!")
    else:
        status_label.config(text="Введите тип")


def show_types():
    text = "Типы мороженого\n"
    for type_name in cafe.get_types():
        text = text + "- " + type_name + "\n"
    status_label.config(text=text)


def update_info():
    text = info_entry.get()
    if text:
        parts = text.split(",")
        if len(parts) >= 1:
            cafe.set_name(parts[0].strip())
        if len(parts) >= 2:
            cafe.set_cuisine(parts[1].strip())
        info_entry.delete(0, END)
        update_info_display()
        status_label.config(text="Готово")
    else:
        status_label.config(text="Введите: название, кухня")


root = Tk()
root.title('Управление кафе-мороженым')
root.geometry('550x600')
root.resizable(width=False, height=False)

left_frame = Frame(root)
left_frame.place(x=10, y=10, width=250, height=300)

flavors_label = Label(left_frame, text="", justify=LEFT)
flavors_label.pack()

flavor_entry = Entry(left_frame)
flavor_entry.pack()

Button(left_frame, text="Добавить", command=add_flavor).pack()
Button(left_frame, text="Удалить", command=remove_flavor).pack()
Button(left_frame, text="Проверить", command=check_flavor).pack()


right_frame = Frame(root)
right_frame.place(x=280, y=10, width=250, height=300)

types_label = Label(right_frame, text="", justify=LEFT)
types_label.pack()

type_entry = Entry(right_frame)
type_entry.pack()

Button(right_frame, text="Добавить тип", command=add_type).pack()
Button(right_frame, text="Удалить тип", command=remove_type).pack()
Button(right_frame, text="Список типов", command=show_types).pack()

center_frame = Frame(root)
center_frame.place(x=10, y=330, width=520, height=200)

info_label = Label(center_frame, text="Название: Мороженое Радуга\nКухня: Кафе-мороженое", justify=LEFT)
info_label.pack(anchor=W, pady=5)

info_entry = Entry(center_frame)
info_entry.pack(fill=X, pady=5)

Button(center_frame, text="Обновить", command=update_info).pack(pady=10)

status_label = Label(root, text="Готово", fg="green")
status_label.place(x=10, y=550, width=520)

update_flavors_text()
update_types_text()
update_info_display()

root.mainloop()