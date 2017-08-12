code_solution=["UTF-8","cp1254","latin-1","ASCII"]

character=input("Enter a character: ")

for x in code_solution:
	try:
		print("'{}'' represent with {}, be {} and {} number".format(character,x,character.encode(x),ord(character)))

	except UnicodeEncodeError:
		print("'{}' can't represent with {}!".format(character,x))