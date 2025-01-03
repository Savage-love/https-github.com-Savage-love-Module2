class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        cls.houses_history.append(args[0])
        return obj
    def __init__(self, name , numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors
        isinstance(numbers_of_floors, int)


    def go_to(self, new_floor):
        if new_floor > self.numbers_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.numbers_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.numbers_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors == other.numbers_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors < other.numbers_of_floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors <= other.numbers_of_floors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors > other.numbers_of_floors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors >= other.numbers_of_floors
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors != other.numbers_of_floors
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors += value
            return self
        return NotImplemented

    def __radd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)
        return NotImplemented
    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

