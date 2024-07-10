class NumberGuesser:
    def welcome_player(self):
        return input("Do you want to play the Number Guesser game? (yes/no): ").strip().lower()

    def get_player_name(self):
        return input("Great! What's your name? ").strip()

    def get_guess(self, guess_count):
        return int(input("Guess %d: " % guess_count))

class Messages:
    def print_welcome_message(self, player_name):
        print("Alright %s, I have picked a number between 1 and 10." % player_name)
        print("You have 3 guesses to find the number. Let's start!")

    def print_feedback(self, feedback_type):
        if feedback_type == "low":
            print("Too low!")
        elif feedback_type == "high":
            print("Too high!")

    def print_congratulations(self, player_name, points):
        print("Congratulations %s! You guessed the number correctly. You win %d points!" % (player_name, points))

    def print_game_over(self, player_name, number_to_guess):
        print("Sorry %s, you've used all your guesses. The number was %d. Better luck next time!" % (player_name, number_to_guess))
