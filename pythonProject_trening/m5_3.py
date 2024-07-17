class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return isinstance(other, Building) and self.buildingType == other.buildingType \
            and self.numberOfFloors == other.numberOfFloors


h1 = Building(15, 'Монолитный дом')
h2 = Building(10, 'Кирпичный дом')
print(h1 == h2)
