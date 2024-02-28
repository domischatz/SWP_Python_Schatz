class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"Color: {self.color}, Mileage: {self.mileage}"

car1 = Car(color="blue", mileage=20_000)
car2 = Car(color="red", mileage=30_000)

print(car1)
print(car2)

