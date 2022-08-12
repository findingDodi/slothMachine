from TheMachine import TheMachine


class ThePlayer:

    def __init__(self):
        self.dodo_coins = 10
        self.machine = TheMachine()

    def dekrement_dodo_coins(self, amount):
        self.dodo_coins -= amount

    def inkrement_dodo_coins(self, amount):
        self.dodo_coins += amount

    def play_round(self):
        pass

    def insert_dodo_coin(self):
        self.dekrement_dodo_coins(1)

    def show_stats(self):
        pass
