class Animal:
    alive = True  # (живой)
    fed = False  # (накормленный)
    # name - индивидуальное название каждого животного

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    # Метод eat должен работать следующим образом:
    def eat(self, food):  # food - это параметр, принимающий объекты классов растений
        if isinstance(food, Plant):
            if food.edible:
                print(f'{self.name} съел {food.name}')
                self.fed = True
            else:
                print(f'{self.name} не стал есть {food.name}')
                self.alive = False

class Plant:
    edible = False  # (съедобность)
    # name - индивидуальное название каждого растения

    def __init__(self, name):
        self.name = name
        self.edible = False

class Mammal(Animal, Plant):
    pass

class Predator(Animal, Plant):
    pass

class Flower(Plant, Animal):
    pass

class Fruit(Plant, Animal):
    edible = True # переопределить при наследовании

    def __init__(self, edible):
        super().__init__(edible)
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

#Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось





