import random
from time import sleep
from typing import Sequence


class Door:
	"""
	A Door with default prize is Goat.
	"""
	def __init__(self, prized: bool = False) -> None:
		self.is_closed: bool = True
		self.prized: bool = prized
	
	def open(self) -> None:
		self.is_closed = False

	def __repr__(self) -> str:
		if self.is_closed:
			return "Closed Door"
		if self.prized:
			return "wow @@"
		return "GOAT"


class Game:
	"""
	A Classic Monty Hall's game with 3 doors and a grand prize.
	"""
	def __init__(self) -> None:
		# init 3 doors
		self.doors : Sequence = tuple([Door() for _ in range(3)])
		# select a door as a for a grand prize
		random.choice(self.doors).prized = True

		self.players_door = None

	def player_select(self, choice: int) -> None:
		"""
		Player selects a door, game reveals one Goat door.
		"""
		self.players_door: Door = self.doors[choice]
		self.open_other()
	
	def player_switch(self) -> None:
		"""
		Player switches door selection.
		"""
		for door in self.doors:
			if (door is not self.players_door) and door.is_closed:
				self.players_door = door
				break

	def open_other(self) -> None:
		"""
		Open the other goat door, randomly open one if both is not selected.
		"""
		while door:= random.choice(self.doors):
			if not door.prized and door is not self.players_door:
				door.open()
				break

	def open_all(self) -> None:
		"""
		Open all doors
		"""
		for door in self.doors:
			door.open()

	def __repr__(self) -> str:
		return '\n' + str(tuple(map(repr, self.doors))) + '\n'


if __name__ == "__main__":
	game = Game()
	print("There are 3 doors, behind one of them is a band new lambo\n and the others are goats.")
	print(game)
	while True:
		choice = input("Select your door! ( 1 | 2 | 3 | ).\n")
		try:
			assert choice
			choice = int(choice)
			if not 1 <= choice <= 3:
				raise ValueError()
		except AssertionError:
			print("Oops! You didn't answer anything. Try again!")
		except ValueError:
			print("Oops! That wasn't a valid answer. Try again!")
		else:
			game.player_select(choice-1)
			break
	print(f"You have selected door number {choice}.\nI'll make your life easier, here's door with a goat.")
	print(game)
	print("I'll let you switch door.")
	while True:
		switch = input("Do You want to switch door? ( yes | no )\n")
		try:
			assert switch
			if switch in ("yes", 'y'):
				game.player_switch()
				print("You've decided to switch door!")
				break
			elif switch in ("no", 'n'):
				print("You'be decided not to switch")
				break
			else:
				print("Oops! Invalid answer. Try again!")
		except AssertionError:
			print("Oops! You didn't answer anything. Try again!")
	print(f"Let's open your door and see what you get!")
	for x in range(3):
		print(x)
		sleep(1)
	game.open_all()
	print(game)
	if game.players_door.prized:
		input("Congrates, You just won a Lambo!")
	else:
		input("Unfortunately, You didn't win the Lambo.\nOn the bright side you have a new pet goat now! See ya next time ^^")