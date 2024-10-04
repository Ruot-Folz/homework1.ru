class House:
    def __init__(self, name, number_of_floors):
        """
        Инициализация объекта класса House.

        Args:
            name (str): Имя дома.
            number_of_floors (int): Количество этажей в доме.
        """
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        """
        Переход на новый этаж.

        Args:
            new_floor (int): Номер этажа, на который нужно приехать.

        Returns:
            None
        """
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)
house = House('ЖК Эльбрус', 30)
house.go_to(10)
house.go_to(31)
