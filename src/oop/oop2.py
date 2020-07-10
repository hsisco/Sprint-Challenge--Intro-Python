"""
Test:
python3 oop/oop2.py
"""
# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    def drive(self):
        return "Vroooom!"

# Subclass Motorcycle from GroundVehicle.
class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels=2):
        super().__init__(num_wheels)
        self.num_wheels = num_wheels

    def drive(self):
        return "BRAAAP!!"
        
# print(f"GV wheels: {GroundVehicle().num_wheels}")
# print(f"MC wheels: {Motorcycle().num_wheels}")

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

a = [i.drive() for i in vehicles]
print(f"\nGroundVehicles go {a}\n")