import random
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

cars = []
for i in range(1, 11):
    car = Car("ABC-" + str(i), random.randint(100, 200))
    cars.append(car)

race_over = False
while not race_over:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_over = True
            break

print("Race results:")
print("Reg.No | Max Speed | Current Speed | Distance")
for car in cars:
    print(car.registration_number, "|", car.max_speed, "|", car.current_speed, "|", round(car.travelled_distance, 1))
