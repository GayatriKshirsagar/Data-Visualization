from random import randint

class Die:
	"""A class representing a single die. """

	def __init__(self, num_sides = 6):
		"""Assume a six-sided die. """
		self.num_sides = num_sides

	def roll(self):
		"""Return a random value between 1 and number of sides. 
		This function can return the starting value (1), ending value(num_sides), 
		or any integer between the two."""
		return randint(1, self.num_sides)