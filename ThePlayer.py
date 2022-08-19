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
        self.machine.play_round()

    def insert_dodo_coin(self):
        self.dekrement_dodo_coins(1)
        self.machine.insert_dodo_coins(1)

    def show_stats(self):
        pass

    def start_shell(self):
        print('A game contains 4 rounds and costs 1🦤')
        keep_playing = True
        while keep_playing:
            start_game = input('Do you want to start a game (y/n)?: ')
            if start_game == 'y':
                self.insert_dodo_coin()
                print('You successfully insert 1🦤!')

                for i in range(self.machine.rounds):
                    start_round = input('Please enter 1 to start the round: ')
                    if start_round == '1':
                        self.play_round()
                        print(self.machine.round_output)

                print('This game over!')

            elif start_game == 'n':
                print('You have', str(self.dodo_coins) + '🦤', 'left!')
                keep_playing = False
