import sys
import random

spieler = sys.argv[1]

computer_zahl = random.randint(0, 2)

if computer_zahl == 0:
    computer = "rock"
elif computer_zahl == 1:
    computer = "paper"
else:
    computer = "scissors"

print("Spieler:", spieler.capitalize())
print("Computer:", computer.capitalize())

if spieler == computer:
    print("Unentschieden!")
elif (spieler == "scissors" and computer == "paper") or \
     (spieler == "paper" and computer == "rock") or \
     (spieler == "rock" and computer == "scissors"):
    print("Der Spieler gewinnt!")
else:
    print("Der Computer gewinnt!")
