from TheMachine import TheMachine


class ThePlayer:

    def __init__(self):
        self.dodo_coins = 2
        self.machine = TheMachine()

    def dekrement_dodo_coins(self, amount):
        self.dodo_coins -= amount

    def inkrement_dodo_coins(self, amount):
        self.dodo_coins += amount

    def play_round(self):
        return self.machine.play_round()

    def insert_dodo_coin(self):
        if self.dodo_coins > 0:
            self.dekrement_dodo_coins(1)
            self.machine.insert_dodo_coins(1)
            return True

        return False

    def get_dodo_coins(self):
        self.inkrement_dodo_coins(self.machine.get_dodo_coins())

    def can_play(self):
        if self.dodo_coins > 0:
            return True

        return False

    def show_stats(self):
        pass

    def start_shell(self):
        print('A game contains 4 rounds and costs 1🦤')
        keep_playing = True
        while keep_playing and self.can_play():
            start_game = input('Do you want to start a game (y/n)?: ')
            if start_game == 'y':
                if self.insert_dodo_coin():
                    print('You successfully insert 1🦤!')

                while self.machine.rounds != 0:
                    print('You now have', self.machine.rounds, 'rounds and', str(self.dodo_coins) + '🦤', 'left!')
                    start_round = input('Please enter 1 to start the round: ')
                    if start_round == '1':
                        game_result = self.play_round()
                        print(self.machine.round_output)
                        if game_result == self.machine.GAME_RESULT_WIN:
                            print('You won the game! You get 4🦤!')
                        elif game_result == self.machine.GAME_RESULT_FREE_ROUND:
                            print('You won a free round! Congrats!')

                print('This game is over!')

            elif start_game == 'n':
                print('You still have', str(self.dodo_coins) + '🦤', 'left!')
                keep_playing = False

        if not self.can_play():
            print('Scuuusi you are not able to play!')
