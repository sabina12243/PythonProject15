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

my_car = Car("ABC-123", 142)

my_car.accelerate(60)

my_car.drive(1.5)

print("Current Speed:", my_car.current_speed, "km/h")
print("Travelled Distance:", my_car.travelled_distance, "km")