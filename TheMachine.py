from TheSlot import TheSlot


class TheMachine:

    GAME_RESULT_WIN = "win"
    GAME_RESULT_LOSE = "lose"
    GAME_RESULT_FREE_ROUND = "free"

    def __init__(self):
        self.dodo_coins = 100
        self.output_tray = 0
        self.slot_amount = 4
        self.rounds = 0
        self.round_output = ""
        self.slots = [TheSlot(), TheSlot(), TheSlot(), TheSlot()]

    def play_round(self):
        if self.rounds == 0:
            return

        self.dekrement_rounds(1)
        self.round_output = ""
        for slot in self.slots:
            slot.set_random_image()
            self.round_output += str(slot)

        if self.check_round() == TheMachine.GAME_RESULT_FREE_ROUND:
            self.inkrement_rounds(1)

        if self.check_round() == TheMachine.GAME_RESULT_WIN:
            self.dodo_coins -= 4
            self.output_tray += 4

        return self.check_round()

    def check_round(self):
        sloth_amount = self.round_output.count('🦥')
        if sloth_amount == 4:
            return TheMachine.GAME_RESULT_WIN
        elif sloth_amount == 3:
            return TheMachine.GAME_RESULT_FREE_ROUND
        else:
            return TheMachine.GAME_RESULT_LOSE

    def insert_dodo_coins(self, amount):
        if amount > 0:
            self.dodo_coins += amount
            self.inkrement_rounds(4 * amount)

    def inkrement_rounds(self, amount):
        if amount > 0:
            self.rounds += amount

    def dekrement_rounds(self, amount):
        if amount > 0:
            self.rounds -= amount

    def get_dodo_coins(self):
        temp_output_tray = self.output_tray
        self.output_tray = 0
        return temp_output_tray


if __name__ == "__main__":
    your_machine = TheMachine()
    for i in range(your_machine.rounds):
        your_machine.play_round()
