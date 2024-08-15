import random
import os

class Player:
    CHOICES = ['rock', 'paper', 'scissors']
    def __init__(self):
        self.move = None

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        while True:
            answer = input("Please choose one of the following: (Rock, Paper, or Scissors) \n").lower().strip()
            if answer in Player.CHOICES:
                self.move = answer
                break
            os.system('clear')
            print("invalid input, please try again.")

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = random.choice(Player.CHOICES)

class Score:
    def __init__(self):
        self.total = 0
    
    def _increase_score(self):
        self.total += 1


class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_message(self):
        print("Welcome to Rock Paper Scissors! First to 3 wins!")

    def _display_goodbye_message(self):
        print("Thanks for Playing!")

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
        human_move = self._human.move
        computer_move = self._computer.move

        print(f'You chose: {human_move}')
        print(f'The computer chose: {computer_move}')

        if self._human_wins():
            print("You win!")
        elif self._computer_wins():
            print('Computer wins!')
        else:
            print("It's a tie")

    def _play_again(self):
        answer = input("Would you like the play again? (y/n)\n")
        return answer.lower().startswith('y')

    def play(self):
        self._display_welcome_message()

        while True:
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            if not self._play_again():
                break
        self._display_goodbye_message()


game = RPSGame()
game.play()
