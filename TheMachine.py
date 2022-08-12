from TheSlot import TheSlot


class TheMachine:

    def __init__(self):
        self.slot_amount = 4
        self.rounds = 4
        self.slots = [TheSlot(), TheSlot(), TheSlot(), TheSlot()]

    def play_round(self):
        for slot in self.slots:
            slot.set_random_image()

    def print_round(self):
        machine_output = ""
        for slot in self.slots:
            machine_output += str(slot)

        print(machine_output)


if __name__ == "__main__":
    your_machine = TheMachine()
    for i in range(your_machine.rounds):
        your_machine.play_round()
        your_machine.print_round()
