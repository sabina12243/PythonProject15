class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print("Elevator is now on floor", self.current_floor)

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print("Elevator is now on floor", self.current_floor)

    def go_to_floor(self, target_floor):
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()


class Building:
    def __init__(self, bottom, top, num_elevators):
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, target_floor):
        print(f"\nRunning elevator {elevator_number} to floor {target_floor}")
        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(target_floor)

my_building = Building(1, 10, 3)

my_building.run_elevator(1, 5)
my_building.run_elevator(2, 7)
my_building.run_elevator(1, 1)
