class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.park = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.park[carType] == 0:
            return False
        self.park[carType] -= 1
        return True