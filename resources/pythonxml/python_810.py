

#


#



#

#

#

#

#

#

#

#

#

#

#




#



numl = [97, 101, 103, 107, 109, 113]
numu = [67, 71, 73, 79, 83, 89]
num = [67, 89, 97, 113]

for _ in range(int(input())):
	length = input()
	string = input()
	result = ''

	for char in string:
		if char.islower() and char.isalpha():
			minimum = 200
			ascii_char = ord(char)
			temp = 0

			for j in numl:
				if minimum > abs(ascii_char - j):
					minimum = abs(ascii_char - j)
					temp = j

			result = result + chr(temp)

		elif char.isupper() and char.isalpha():
			minimum = 200
			ascii_char = ord(char)
			temp = 0

			for j in numu:
				if minimum > abs(ascii_char - j):
					minimum = abs(ascii_char - j)
					temp = j

			result = result + chr(temp)

		else:
			minimum = 200
			ascii_char = ord(char)
			temp = 0

			for j in num:
				if minimum > abs(ascii_char - j):
					minimum = abs(ascii_char - j)
					temp = j

			result = result + chr(temp)

	print(result)
