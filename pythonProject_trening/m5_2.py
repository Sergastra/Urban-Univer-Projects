class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f"numberOfFloors = {self.numberOfFloors}")


h = House()
h.setNewNumberOfFloors(14)

