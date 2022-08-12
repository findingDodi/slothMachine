from TheSlot import TheSlot


class TheMachine:

    GAME_RESULT_WIN = "win"
    GAME_RESULT_LOSE = "lose"
    GAME_RESULT_FREE_ROUND = "free"

    def __init__(self):
        self.dodo_coins = 100
        self.slot_amount = 4
        self.rounds = 0
        self.round_output = ""
        self.slots = [TheSlot(), TheSlot(), TheSlot(), TheSlot()]

    def play_round(self):
        if self.rounds == 0:
            return

        self.round_output = ""
        for slot in self.slots:
            slot.set_random_image()
            self.round_output += str(slot)

        self.check_round()

    def check_round(self):
        sloth_amount = self.round_output.count('🦥')
        if sloth_amount == 4:
            return TheMachine.GAME_RESULT_WIN
        elif sloth_amount == 3:
            return TheMachine.GAME_RESULT_FREE_ROUND
        else:
            return TheMachine.GAME_RESULT_LOSE

    def insert_dodo_coins(self, amount):
        self.dodo_coins += amount
        self.rounds = 4 * amount


if __name__ == "__main__":
    your_machine = TheMachine()
    for i in range(your_machine.rounds):
        your_machine.play_round()
