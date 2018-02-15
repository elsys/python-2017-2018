


if __name__ == "__main__":

	n = int(input())
	res = []
	for i in range(n):
		line = input()
		words = line.split()
		command = words[0]
		if command == "insert":
			i = int(words[1])
			e = int(words[2])
			res.insert(i, e)
		elif command == "print":
			print(res)


# lchorbadjiev@elsys-bg.org















		
