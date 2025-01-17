class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.houses_history.append(args[0])
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

h1 = House('ЖК Горский', 18)
h2 = House('ЖК Олимпийский', 20)
h3 = House('ЖК Центральный', 15)

print(House.houses_history)

del h2
print(House.houses_history)
