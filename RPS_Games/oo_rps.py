import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self):
        self.move = None

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = random.choice(Player.CHOICES)

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        answer = input("Do you choose rock, paper, or scissors?: \n")
        while answer.strip().lower()[0] not in 'rps':
            answer = input('Invalid input. Try again\n')
        self.move = answer

class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def play(self):
        self._display_welcome_message()
        while True:
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            if not self._play_again():
                break
        self._display_goodbye_message()

    def _play_again(self):
        answer = input("Would you like to play again? (Y or N)\n")
        if answer.lower().strip()[0] == 'y':
            return True
        return False

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _human_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((human_move == 'rock' and computer_move == 'scissors') or
            (human_move == 'paper' and computer_move == 'rock') or
            (human_move == 'scissors' and computer_move == 'paper'))

    def _computer_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((computer_move == 'rock' and human_move == 'scissors') or
          (computer_move == 'paper' and human_move == 'rock') or
          (computer_move == 'scissors' and human_move == 'paper'))

    def _display_winner(self):
        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        if self._human_wins():
            print('You win!')
        elif self._computer_wins():
            print('Computer wins!')
        else:
            print("It's a tie")


RPSGame().play()
