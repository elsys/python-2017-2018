


if __name__ == "__main__":
	
	
	msg = input()
	n = int(msg)
	
	if n % 2 == 1:
		print("Weird")
	else:
		# even
		if 2 <= n <= 5:
			print("Not Weird")
		elif 6 <= n <= 20:
			print("Weird")
		else:
			print("Not Weird")


