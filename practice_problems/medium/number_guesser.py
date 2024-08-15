import random

class GuessingGame:
    RANGE = range(1, 101)
    MAX_GUESSES = 7
    GUESSES_REMAINING = range(MAX_GUESSES, 0, -1)
    GUESS_RESULT_MESSAGE = {
        'high': 'Your guess was too high!',
        'low': 'Your guess was too low!',
        'match': "That's the number!",
    }
    WIN_OR_LOSE = {
        'high': 'lose',
        'low': 'lose',
        'match': 'win'
    }
    END_OF_GAME = {
        'lose': 'You have no more guesses. You lose!',
        'win': 'You won!!'
    }

    def __init__(self):
        self.secret_number = None
    
    def reset(self):
        self.secret_number = random.choice(self.RANGE)

    def play(self):
        self.reset()
        result = self.play_game()
        self.display_end_of_game(result)

    def play_game(self):
        for guess in self.GUESSES_REMAINING:
            self.guesses_remaining_message(guess)
            answer = self.guess_result(self.get_guess())
            self.guess_result_message(answer)
            if answer == 'match':
                return self.WIN_OR_LOSE[answer]
            
        return self.WIN_OR_LOSE[answer]

    def guesses_remaining_message(self, remaining):
        print()
        print(f'You have {remaining} guesses remaining.')

    def get_guess(self):
        while True:
            answer = input(f'Enter a number between {self.RANGE}:\n')
            if not answer.isdigit() or int(answer) not in self.RANGE:
                print('Invalid answer. Try again')
            else:
                return int(answer)

    def guess_result(self, guess_number):
        if guess_number > self.secret_number:
            return 'high'
        elif guess_number < self.secret_number:
            return 'low'
        return 'match'

    def guess_result_message(self, answer):
        print(self.GUESS_RESULT_MESSAGE[answer])
    
    def display_end_of_game(self, answer):
        print()
        print(self.END_OF_GAME[answer])

hello = GuessingGame()
hello.play()