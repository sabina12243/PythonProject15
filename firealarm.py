class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        self.current_floor += 1
        print("Elevator is now on floor", self.current_floor)

    def floor_down(self):
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

    def run_elevator(self, num, floor):
        print("\nElevator", num, "going to floor", floor)
        self.elevators[num - 1].go_to_floor(floor)

    def fire_alarm(self):
        print("\nFIRE ALARM! All elevators go to bottom floor!")
        for i, e in enumerate(self.elevators, start=1):
            print("\nElevator", i, "going to bottom floor")
            e.go_to_floor(e.bottom)

building = Building(1, 10, 3)

building.run_elevator(1, 5)
building.run_elevator(2, 8)

building.fire_alarm()
