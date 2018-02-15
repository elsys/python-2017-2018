import sys


if __name__ == "__main__":

	n = 10 # int(input())
	
	for i in range(1, n+1):
		print(i, end="")

	print("")

	print("a", "b", "c", "d", 
		sep="!!!!", end="(ala bala)\n", file=sys.stderr)

