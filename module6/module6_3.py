class Vechile:
    vehicle_type = "none"


class Car:
    price = 100000

    def horse_powers(self, horsePower):
        self.horsePower = 350


class Nissan(Car, Vechile):
    vehicle_type = 'sedan'
    price = 2400000

    def horse_powers(self, horsePower):
        super().horse_powers(horsePower)

        return f'количество лошидиных сил {horsePower}'


if __name__ == '__main__':

    print(Nissan.mro())
    nis = Nissan()
    print(nis.vehicle_type, nis.price, nis.horse_powers(450), sep='\n')
