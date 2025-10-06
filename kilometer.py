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


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print("Registration | Max Speed | Current Speed | Distance Travelled")
        print("-------------------------------------------------------------")
        for car in self.cars:
            print(f"{car.registration_number:12} {car.max_speed:10} {car.current_speed:14} {car.travelled_distance:18.1f}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


# --- Main Program ---
cars = []
for i in range(1, 11):
    car = Car("ABC-" + str(i), random.randint(100, 200))
    cars.append(car)

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while not race.race_finished():
    race.hour_passes()
    hours += 1

    if hours % 10 == 0:
        print(f"\n--- After {hours} hours ---")
        race.print_status()

print(f"\n🏁 Race finished after {hours} hours! 🏁")
race.print_status()
