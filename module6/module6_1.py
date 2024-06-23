class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    fed = True

    def eat(self, food):
        self.food = food

        if food != 1:
            print(f'{self.name} съел {food.name}')

        else:
            print(f'{self.name} не стал есть {food.name}')



class Predator(Animal):
    alive = False

    def eat(self, food):
        self.food = food

        if food == 1:
            print(f'{self.name} съел {food.name}')
        else:
            print(f'{self.name} не стал есть {food.name}')


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Flower(Plant):

    def food(self, name):
        self.name = name


class Fruit(Plant):

    def food(self, name, edible=True):
        self.name = name
        self.edible = edible


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
