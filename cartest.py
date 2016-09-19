from unreliableCar import UnreliableCar
from unreliableCar import SilverServiceTaxi

badCar = UnreliableCar("UnreliableCar", 100, 90)

badCar.drive(50)
print(badCar)

niceTaxi = SilverServiceTaxi("Limo", 100, 1.2, 2)
niceTaxi.drive(10)
print(niceTaxi)
print("${:.2f}".format(niceTaxi.get_fare()))
