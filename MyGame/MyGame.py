# Seung-Joon Rim
# Started on: 12/6/2016 - 9:35 PM
# Finished on:

# This is my game

from sys import exit
from random import randint

class Scene(object):	# parent class of all scenes

	def enter(self, scene):				# class Scene has-a method enter() that takes parameters self
										# and scene
		with open(scene, 'r+') as f:	# open scene (a text file) in read mode and set it to f
			print ''
			for line in f.readlines():
				print line.strip()
				if line == '\n':		# if theres a blank line, pause the game
					raw_input("> ")		# continue the game with enter
					print ''

		f.close()


class Wake_Up(Scene):

	def enter(self):
		super(Wake_Up, self).enter('Wake_Up.txt')		# call parent class .enter() method with
														# parameters self and 'Wake_Up.txt'
		code = 2001
		guess = raw_input("\n(enter your guess) > ")
		guesses = 0

		while int(guess) != code and guesses < 2:		# 3 guesses, 1st guess has already been made
			guess = raw_input("(enter your guess) > ")
			guesses += 1
		
		if int(guess) == code:
			return 'Intro'	# if you guess right, go the intro scene
		else:
			return 'Death'	# if you guess wrong, go to death scene


class Intro(Scene):

	def enter(self):
		with open('Intro.txt', 'r+') as f:	# override parent class enter() method

			print ''
			for line in f.readlines():

				if '(name)' in line:							# when you get to the '(name)' in the text file,
					name = raw_input('\n(name) > ')				# ask player for his name and set it to name
					print ''
					print line.strip().replace('(name)', name)	# replace '(name)' in the text file with the
																# player's name
				else:
					print line.strip()							# else: just print the line normally
					if line == '\n':
						raw_input("> ")
						print ''

		choice = raw_input("\n(Type 1, 2, or 3) > ")	# prompt the user for his choice

		if str(1) in choice:
			return 'Death'
		elif str(2) in choice:		# right choice is the second one
			return 'Choose_Hallway'	# go to the 'Choose_Hallway' scene
		elif str(3) in choice:
			return 'Death'
		else:
			return 'Death'

		f.close()


class Choose_Hallway(Scene):

	def enter(self):
		super(Choose_Hallway, self).enter('Choose_Hallway.txt')

		choice = raw_input("\n(Type 1, 2, or 3) > ")

		if str(1) in choice:
			return 'Final'
		elif str(2) in choice:
			return 'Death'
		elif str(3) in choice:
			return 'Death'
		else:
			return 'Death'


class Final(Scene):

	def enter(self):
		super(Final, self).enter('Final.txt')

		exit(1)


class Death(Scene):

	def enter(self):
		super(Death, self).enter('Death.txt')

		exit(1)


class Map(object):

	scenes = {	# dictionary of scenes and their classes
		'Wake_Up': Wake_Up(),
		'Intro': Intro(),
		'Choose_Hallway': Choose_Hallway(),
		'Final': Final(),
		'Death': Death()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene	# the class Map has-a __init__ that takes parameters
										# self and start_scene

	def next_scene(self, scene_name):				
		val = Map.scenes.get(scene_name)	# from the scenes dictionary from the class Map,
		return val							# .get() the value of the key 'scene_name' and set
											# it to val, and return it

	def opening_scene(self):						
		return self.next_scene(self.start_scene)	# use the next_scene method with the parameter self.start_scene


class Engine(object):

	def __init__(self, scene_map):	
		self.scene_map = scene_map	# class Engine has-a __init__ that takes the parameters self
									# and scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()		# self.scene_map has-a method called opening_scene()
															# that takes only self parameter, set it to current_scene
		last_scene = self.scene_map.next_scene('Final')		# self.scene_map has-a method called next_scene(), call it with
															# parameters self and 'Final' and set it to last_scene

		while current_scene != last_scene:					# while current_scene does not equal last_scene
			next_scene_name = current_scene.enter()			# current_scene has-a method called enter(), when run it will 
															# return the string key to the next room, set the string to 
															# next_scene_name
			current_scene = self.scene_map.next_scene(next_scene_name)	# from self.scene_map, call the next_scene() method
																		# with parameters self and next_scene_name and set it
																		# as the new current_scene

		current_scene.enter()	# if current_scene == last_scene, run the enter() method (this is the final scene)

a_map = Map('Wake_Up')
a_game = Engine(a_map)
a_game.play()
