def identity(nums):
	"""Identity:

    Given a list of numbers, write a list comprehension that produces a copy of 
	the list.
	"""

	identity_ = [i for i in nums]
	return identity_

def doubled(nums):
	"""Given a list of numbers, returns a list comprehension that produces a list
	of each number doubled.
	"""

	doubled_ = [num*2 for num in nums]
	return doubled_

def squared(nums):
	"""Given a list of numbers, returns a list comprehension that produces a list
	of each number squared.
	"""

	squared_ = [num**2 for num in nums]
	return squared_

def even(nums):
	"""Given a list of numbers, create a list comprehension that returns only 
	even numbers in that list.
	"""

	even_ = [num for num in nums if num % 2 == 0]
	return even_

def odds(nums):
	"""Given a list of numbers, create a list comprehension that returns only 
	odds numbers in that list
	"""

	odds_ = [num for num in nums if num % 2 != 0]
	return odds_

def positives(nums):
	"""Given a list of numbers, create a list comprehension that returns only 
	positives numbers in that list.
	"""
	positives_ = [num for num in nums if num > 0]
	return positives_

def selective_stringify_nums(nums):
	"""Selectively stringify nums:

    Given a list of numbers, write a list comprehension that produces a list of
	strings of each number that is divisible by 5.
	"""

	stringified = [str(num) for num in nums if not(num % 5)]
	return stringified

def words_not_the(sentence):
	"""Words not 'the'

    Given a sentence, produce a list of the lengths of each word in the sentence,
	but only if the word is not 'the.
	"""

	not_the_lenghts = [len(word) for word in list(sentence.split()) if word != 'the']
	return not_the_lenghts

def vowels(word):
	"""Vowels:

    Given a string representing a word, write a list comprehension that produces
	a list of all the vowels in that word.
	"""
	vowels_ = [letter for letter in word if letter in 'aeiou']
	return vowels_

def vowels_set(word):
	"""Vowels set:

    Given a string representing a word, write a set comprehension that produces 
	a set of all the vowels in that word.
	"""

	vowels_set_ = set([letter for letter in word if letter in 'aeiou'])
	return vowels_set_

def disemvowel(sentence):
	"""Disemvowel:

    Given a sentence, return the sentence with all vowels removed.
	"""

	sentence = sentence
	#la logica seria:
		# agregar elemento a la comprehension list, si el elemento
		# no esta en la string 'aeiou'
	disemvowel_ = ''.join([char for char in sentence if char not in 'aeiou'])
	return disemvowel_

def wiggle_numbers(nums):
	"""Wiggle numbers:

    Given a list of numbers, return the list with all even numbers doubled, and 
	all odd numbers turned negative.
	"""

	wiggle_numbers_ = [num*2 if num % 2 == 0 else num*(-1) for num in nums]
	return wiggle_numbers_

def encrypt_lol(sentence):
	"""Encrypt lol:

    Given a sentence, return the setence with all it's letter transposed by 1 
	in the alphabet, but only if the letter is a-y.
	"""
	
	encrypt_lol_ = ''.join([chr(ord(letter) + 1) if (ord('a') <= ord(letter) <= 
	ord('y')) else letter for letter in sentence])
	return encrypt_lol_





numeros = list(range(0,11)) + list(reversed(range(-10, 0)))
sentence = 'What the fuck if the fucking world is fucked'
word = 'pija'
print(encrypt_lol(sentence))



