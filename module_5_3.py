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

    def __len__(self):
        """
        Возвращает количество этажей в доме.

        Returns:
            int: Количество этажей в доме.
        """
        return self.number_of_floors

    def __str__(self):
        """
        Возвращает строку с информацией о доме.

        Returns:
            str: Строка с информацией о доме.
        """
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        """
        Сравнение количества этажей.

        Args:
            other (House): Другой объект класса House.

        Returns:
            bool: True, если количество этажей одинаковое, False иначе.
        """
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        """
        Сравнение количества этажей (меньше).

        Args:
            other (House): Другой объект класса House.

        Returns:
            bool: True, если количество этажей меньше, False иначе.
        """
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        """
        Сравнение количества этажей (меньше или равно).

        Args:
            other (House): Другой объект класса House.

        Returns:
            bool: True, если количество этажей меньше или равно, False иначе.
        """
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        """
        Сравнение количества этажей (больше).

        Args:
            other (House): Другой объект класса House.

        Returns:
            bool: True, если количество этажей больше, False иначе.
        """
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        """
        Сравнение количества этажей (больше или равно).

        Args:
            other (House): Другой объект класса House.

        Returns:
            bool: True, если количество этажей больше или равно, False иначе.
        """
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        """
        Сравнение количества этажей (не равно).

        Args:
            other (House): Другой объект класса House.

        Returns:
            bool: True, если количество этажей не равно, False иначе.
        """
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        """
        Увеличивает количество этажей на переданное значение.

        Args:
            value (int): Значение, на которое нужно увеличить количество этажей.

        Returns:
            House: Сам объект self.
        """
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        """
        Увеличивает количество этажей на переданное значение (правый операнд).

        Args:
            value (int): Значение, на которое нужно увеличить количество этажей.

        Returns:
            House: Сам объект self.
        """
        return self.__add__(value)

    def __iadd__(self, value):
        """
        Увеличивает количество этажей на переданное значение (инкремент).

        Args:
            value (int): Значение, на которое нужно увеличить количество этажей.

        Returns:
            House: Сам объект self.
        """
        return self.__add__(value)
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
