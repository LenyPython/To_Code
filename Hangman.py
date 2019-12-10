import random
# list of words, guessed part by the user and used letters

play = 'y'


def create_game():
	with open('ar.txt', 'r') as ar:
		list_of_words = ar.readlines()
	random_word = random.choice(list_of_words)
	guessed_part = ['_' for x in range(len(random_word) - 1)]
	used_letters = []
	chances = 6
	return random_word, guessed_part, used_letters, chances


# player normal input function
def letter_check(list_of_used_letters, letter):
	if letter.upper() in list_of_used_letters:
		guessed_letter = input('You tried that letter. Use other: ')
		return letter_check(list_of_used_letters, guessed_letter)
	else:
		guessed_letter = letter.upper()
	return guessed_letter.upper()


def rewrite_guessed_part(word, guessed_letter, known_part):
	for index in range(len(word)):
		if word[index] == guessed_letter:
			known_part[index] = word[index]
	return known_part


def conclusion(word, guessed, tries):
	print('The word was: ' + word)
	print('You guessed ' + ''.join(guessed))
	print('You tried ' + ','.join(tries))


def count_chances(remaining_chances, used, word, letter):
	if letter in used:
		return remaining_chances
	elif letter not in word:
		return remaining_chances - 1
	else:
		return remaining_chances


def print_hangman(left):
	if left == 6:
		print('Good!')
	elif left == 5:
		print('/ \\')
	elif left == 4:
		print(' |')
		print('/ \\')
	elif left == 3:
		print('/|\\')
		print(' |')
		print('/ \\')
	elif left == 2:
		print(' O')
		print('/|\\')
		print(' |')
		print('/ \\')
	elif left == 1:
		print('  |')
		print(' O|')
		print('/|\\')
		print(' |')
		print('/ \\')
	elif left == 0:
		print('You died!')
	else:
		print("Congratz!! You won!!")


if __name__ == '__main__':

	print('>>> Welcome to hangman!!!')
	print('-------------------------')
	# continue loop while there are empty brackets '_'
	while play == 'Y' or play == 'y':
		data = create_game()
		random_word = data[0]
		guessed_part = data[1]
		used_letters = data[2]
		chances = data[3]
		while '_' in guessed_part and chances > 0:
			print('-------------------------')
			guess = input('>>> Type your guess: ')
			guess = letter_check(used_letters, guess)

			guessed_part = rewrite_guessed_part(random_word, guess, guessed_part)
			chances = count_chances(chances, used_letters, random_word, guess)

			print(''.join(guessed_part))
			print('You got ' + str(chances) + ' chances left')
			print_hangman(chances)
			if guess not in used_letters:
				used_letters.append(guess)

		conclusion(random_word, guessed_part, used_letters)
		play = input("Would you like to play again? Type Y/y")
