import random
import os

def clear_screen():
    os.system('clear')

class Square:
    INITIAL_MARKER = ' '
    PLAYER_MARKER = 'X'
    COMPUTER_MARKER = 'O'

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    def __str__(self):
        return self.marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, new_value):
        self._marker = new_value

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

class Board:
    def __init__(self):
        self.squares = {x: Square() for x in range(1, 10)}

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |"
              f"  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |"
              f"  {self.squares[5]}  |"
              f"  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |"
              f"  {self.squares[9]}")
        print("     |     |")
        print()

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def unused_sqaures(self):
        return [key
                for key, square in self.squares.items()
                if square.is_unused()]

    def is_full(self):
        unused_sqaures = self.unused_sqaures()
        return len(unused_sqaures) == 0

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)

    def display_with_clear(self):
        clear_screen()
        print('\n')
        self.display()

class Player:
    def __init__(self, marker):
        self.marker = marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

class Human(Player):
    def __init__(self):
        super().__init__(Square.PLAYER_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    )
    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
    
    @staticmethod
    def _join_or(lst, sep=', ', word='or'):
        if len(lst) < 2:
            return lst[0]
        if len(lst) == 2:
            return f'{word} '.join(lst)
        
        return f'{sep}'.join(lst[:-1]) + f'{sep}{word} {lst[-1]}'

    def play(self):
        self.display_welcome_message()
        self.board.display()

        while True:

            self.human_moves()
            if self.is_game_over():
                break

            self.computer_moves()
            if self.is_game_over():
                break
            self.board.display_with_clear()

        self.board.display_with_clear()
        self.display_results()
        self.display_goodbye_message()

    def display_welcome_message(self):
        clear_screen()
        print("Welcome to Tic Tac Toe!")
        print()

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe! Goodbye!")

    def display_results(self):
        if self.is_winner(self.human):
            print("You won! Congratulations!")
        elif self.is_winner(self.computer):
            print("Computer won! Better luck next time!")
        else:
            print("A Tie Game! How boring.")

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True

        return False

    def human_moves(self):
        choice = None

        while True:
            valid_choices = self.board.unused_sqaures()
            choices_list = [str(choice) for choice in valid_choices]
            choices_str = TTTGame._join_or(choices_list)
            choice = input(f'Choose a square {choices_str}: ')
            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass
            print("Sorry, that's not a valid choice.")
            print()
        self.board.mark_square_at(choice, self.human.marker)

    def computer_moves(self):
        choice = random.choice(self.board.unused_sqaures())
        self.board.mark_square_at(choice, self.computer.marker)

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def someone_won(self):
        return (self.is_winner(self.human) or self.is_winner(self.computer))

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

game = TTTGame()
game.play()
