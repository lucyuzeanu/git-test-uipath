import random
from numberguesser import NumberGuesser, Messages

class NumberGuesserGame:
    def __init__(self):
        self.max_guesses = 3
        self.number_guesser = NumberGuesser()
        self.messages = Messages()

    def play(self):
        play_game = self.number_guesser.welcome_player()
        if play_game != "yes":
            print("Maybe next time. Goodbye!")
            return

        player_name = self.number_guesser.get_player_name()

        number_to_guess = random.randint(1, 10)

        points = self.max_guesses

        self.messages.print_welcome_message(player_name)

        for guess_count in range(1, self.max_guesses + 1):
            guess = self.number_guesser.get_guess(guess_count)
            
            if guess == number_to_guess:
                self.messages.print_congratulations(player_name, points)
                return
            elif guess < number_to_guess:
                self.messages.print_feedback("low")
            else:
                self.messages.print_feedback("high")
            
            points -= 1

        self.messages.print_game_over(player_name, number_to_guess)
