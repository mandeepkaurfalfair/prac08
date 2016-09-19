from taxi import Car
from random import randint
from taxi import Taxi

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        carDrives = randint(0,100)
        if carDrives < self.reliability:
            super().drive(distance)
        else:
            print("The car sputters and goes nowhere")

class SilverServiceTaxi(Taxi):
    flagfall = 4.5
    def __init__(self, name, fuel, price_per_km, fanciness):
         super().__init__(name, fuel, price_per_km)
         self.fanciness = fanciness

    def get_fare(self):
        baseFare = super().get_fare()
        fare = baseFare * self.fanciness + SilverServiceTaxi.flagfall
        return fare