import random
import os
import time

def wait(seconds):
    time.sleep(seconds)

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
        self.reset()

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

    def is_unused_sqaure(self, key):
        return self.squares[key].is_unused()

    def display_with_clear(self):
        clear_screen()
        print('\n')
        self.display()

    def reset(self):
        self.squares = {x: Square() for x in range(1, 10)}

class Player:
    def __init__(self, marker):
        self.marker = marker
        self.wins = 0

    def reset_score(self):
        self.wins = 0

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

    def increase_score(self):
        self.wins += 1

    @property
    def wins(self):
        return self._wins

    @wins.setter
    def wins(self, value):
        self._wins = value

class Human(Player):
    def __init__(self):
        super().__init__(Square.PLAYER_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    TOTAL_ROUNDS = 3
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
        self.first_player = self.human

    @property
    def first_player(self):
        return self._first_player

    @first_player.setter
    def first_player(self, new_player):
        if not isinstance(new_player, Player):
            raise TypeError("New player must be a player object")
        self._first_player = new_player

    def _reset_game(self):
        clear_screen()
        self.board.reset()

    @staticmethod
    def _join_or(lst, sep=', ', word='or'):
        if len(lst) < 2:
            return lst[0]
        if len(lst) == 2:
            return f' {word} '.join(lst)

        return f'{sep}'.join(lst[:-1]) + f'{sep}{word} {lst[-1]}'

    def play_again(self):
        while True:
            answer = input('Would you like to play again? (y/n): ')
            answer.strip().lower()
            if answer[0] == 'y':
                return True
            if answer[0] == 'n':
                return False
            print("Sorry that's not a valid input.")

    def play(self):
        self.display_welcome_message()

        while True:
            self.play_game_of()
            if not self.play_again():
                break
            clear_screen()
            print('\n')

        self.display_goodbye_message()

    def play_game_of(self):
        while not self.is_game_over():
            self.play_round()
            self.first_player = self.toggle_player(self.first_player)
        self.display_game_results()
        self.human.reset_score()
        self.computer.reset_score()

    def play_round(self):
        current_player = self.first_player
        self.board.reset()
        self.board.display()
        self.display_players_turn()

        while True:
            self.player_moves(current_player)
            if self.is_round_over():
                break

            self.board.display_with_clear()
            current_player = self.toggle_player(current_player)

        self.board.display_with_clear()
        self.display_round_results()
        self.update_score()
        self.display_score()
        wait(1.5)

    def display_players_turn(self):
        if self.first_player == self.human:
            print("Your turn to move first!")
        else:
            print("Computer's turn to move first!")
            wait(2)
    def toggle_player(self, player):
        if player is self.human:
            return self.computer
        return self.human

    def player_moves(self, player):
        if player is self.human:
            self.human_moves()
        else:
            self.computer_moves()

    def is_game_over(self):
        return max(self.computer.wins, self.human.wins) == TTTGame.TOTAL_ROUNDS

    def display_welcome_message(self):
        clear_screen()
        print(f"Welcome to Tic Tac Toe! First to {TTTGame.TOTAL_ROUNDS} wins!")
        print()

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe! Goodbye!")

    def update_score(self):
        if self.is_winner(self.human):
            self.human.increase_score()
        elif self.is_winner(self.computer):
            self.computer.increase_score()
        else:
            pass

    def display_score(self):
        print(F"SCOREBOARD: [Human- {self.human.wins}] "
              f" [Computer- {self.computer.wins}]")

    def display_round_results(self):
        clear_screen()
        if self.is_winner(self.human):
            print("You won!")
        elif self.is_winner(self.computer):
            print("Computer won!")
        else:
            print("A Tie Round! How boring.")

    def display_game_results(self):
        if self.human.wins >= 3:
            print("You won the game!!! Congratulations")
        else:
            print("Computer wins the Game! Better luck next time!")

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
        choice = self.offensive_computer_move()
        if not choice:
            choice = self.defensive_computer_move()
        if not choice:
            choice = self.pick_center_square()
        if not choice:
            choice = self.pick_random_square()
        self.board.mark_square_at(choice, self.computer.marker)

    def offensive_computer_move(self):
        return self.find_winning_square_for(self.computer)

    def defensive_computer_move(self):
        return self.find_winning_square_for(self.human)

    def pick_center_square(self):
        if 5 in self.board.unused_sqaures():
            return 5
        return None

    def pick_random_square(self):
        return random.choice(self.board.unused_sqaures())

    def find_winning_square_for(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            key = self.winning_square(player, row)
            if key:
                return key
        return None

    def winning_square(self, player, row):
        if self.two_in_a_row(player, row):
            for key in row:
                if self.board.is_unused_sqaure(key):
                    return key
        return None

    def is_round_over(self):
        return self.board.is_full() or self.someone_won()

    def someone_won(self):
        return (self.is_winner(self.human) or self.is_winner(self.computer))

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def two_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 2

game = TTTGame()
game.play()
