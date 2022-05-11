#!/usr/bin/env python3
import random
import time
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def time_pause(message, num):
    print(message)
    time.sleep(num)


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

    def point(self):
        self.score += 1


# class ReflectPlayer(Player):
#     def __init__(self):
#         self.score = 0
#         self.my_move = random.choice(moves)
#
#     def move(self):
#         return self.my_move
#
#     def learn(self, player, enemy):
#         self.my_move = enemy

# This class returns rock if the enemy move is None.
class ReflectPlayer(Player):
    def __init__(self):
        self.my_move = None
        self.their_move = None
        self.score = 0

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        while True:
            if self.their_move is None:
                self.their_move = "rock"
                return "rock"
            else:
                return self.their_move

class CyclePlayer(Player):
    def __init__(self):
        self.score = 0
        self.my_move = random.choice(moves)

    def move(self):
        if self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'scissors':
            return 'rock'

    def learn(self, player, enemy):
        self.my_move = player


class RandomPlayer(Player):
    def __init__(self):
        self.score = 0

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def __init__(self):
        self.score = 0

    def move(self):
        self.choose = input("Rock, Paper, Scissors?\n").lower()
        return self.choose


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.round = 0

    def beats(self, one, two):
        while True:
            if one == 'rock' and two == 'scissors':
                time_pause("Rock beats scissors! Player 1 won.", 2)
                self.p1.point()
                break
            elif one == 'rock' and two == 'paper':
                time_pause("Paper beats Rock! Player 2 won.", 2)
                self.p2.point()
                break
            elif one == 'scissors' and two == 'paper':
                time_pause("Scissor beats Paper! Player 1 won.", 2)
                self.p1.point()
                break
            elif one == 'scissors' and two == 'rock':
                time_pause("Rock beats Scissor! Player 2 won.", 2)
                self.p2.point()
                break
            elif one == 'paper' and two == 'rock':
                time_pause("Paper beats Rock! Player 1 won.", 2)
                self.p1.point()
                break
            elif one == 'paper' and two == 'scissors':
                time_pause("Scissor beats Paper! Player 2 won.", 2)
                self.p2.point()
                break
            elif one == two:
                time_pause(f"Both players chose {one}. Its a tie.", 2)
                break
            else:
                print("Try again.")
                break

    def scores(self):
        time_pause(f"Player1 score: {self.p1.score} "
                   f"\t Player2 score: {self.p2.score}", 2)

    def play_round(self):
        while True:
            move1 = self.p1.move()
            move2 = self.p2.move()
            self.p1.learn(move1, move2)
            self.p2.learn(move2, move1)
            if move1 in moves and move2 in moves:
                time_pause(f"You played {move1}.", 1)
                time_pause(f"Your opponent played {move2}.", 1)
                self.beats(move1, move2)
                break
            else:
                print("Try again.")

    def play_game(self):
        while True:
            round_game = input("Play rock, paper, scissors? "
                               "(Yes/No)\n").lower()
            if round_game == 'yes':
                self.round += 1
                time_pause("Game start!", 2)
                time_pause(f"Round {self.round}:", 2)
                self.scores()
                self.play_round()
            elif round_game == 'no':
                print("Thank you for playing.")
                break
            else:
                time_pause("Invalid. Try again.", 2)
        print("Game over!")
        time_pause(f"Final score is Player1: {self.p1.score}"
                   f"\t Player2: {self.p2.score}", 2)
        if self.p1.score > self.p2.score:
            time_pause("Player 1 wins!", 2)
        elif self.p2.score > self.p1.score:
            time_pause("Player 2 wins!", 2)
        elif self.p2.score == self.p1.score:
            time_pause("Its a tie.", 2)


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
