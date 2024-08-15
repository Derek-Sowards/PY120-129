import random
import os

class Player:
    CHOICES = ['rock', 'paper', 'scissors']
    def __init__(self):
        self.move = None
        self.score = Score()


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
    
    def increase(self):
        self.total += 1
    
    def reset(self):
        self.total = 0
    
    def __str__(self):
        return str(self.total)

    def __gt__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        return self.total > other.total


class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_message(self):
        print("Welcome to Rock Paper Scissors! First to 3 wins!")

    def _display_goodbye_message(self):
        print("Thanks for Playing!")
    
    def _find_round_winner(self):
        if self._human.score.total >= 3:
            return 'You'
        elif self._computer.score.total >= 3:
            return 'Computer'
    
    def _reset_score(self):
        self._human.score.reset()
        self._computer.score.reset()
        
    def _display_champion(self):
        if self._find_round_winner() == 'You':
            print("You are the ultimate champion of RPS!!! Congrats!")
        else:
            print("Computer is the ultimate champion of RPS! Better luck next time!")

    def _display_scoreboard(self):
        print(f"SCOREBOARD- Human: {self._human.score} Computer: {self._computer.score}")
    
    def _check_scoreboard(self):
        if self._human.score.total >= 3 or self._computer.score.total >= 3:
            return False
        return True
    
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
            self._human.score.increase()
            print("You win!")
        elif self._computer_wins():
            self._computer.score.increase()
            print('Computer wins!')
        else:
            print("It's a tie")

    def _play_again(self):
        answer = input("Would you like the play again? (y/n)\n")
        return answer.lower().startswith('y')

    def play(self):
        self._display_welcome_message()

        while True:
            while self._check_scoreboard():
                self._display_scoreboard()
                self._human.choose()
                self._computer.choose()
                self._display_winner()
            self._display_champion()
            if not self._play_again():
                break
            self._reset_score()
        self._display_goodbye_message()


game = RPSGame()
game.play()
