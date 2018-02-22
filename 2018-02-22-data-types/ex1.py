

if __name__ == "__main__":
	
	l1 = ["a", "b", "c"]
	c = 0
	for i, l in enumerate(l1):
		print(c, i, l)
		c += 1
		
	print(" %--% ".join(l1))
	
	print(",".join([str(i) for i in range(10)]))
	
	l2 = [("a", "b"), ("c", "d"), ("e", "f")]
	for i, l in enumerate(l2):
		print(i, l)


	for i, (a, b) in enumerate(l2):
		print(i, a, b)


	for t in enumerate(l1):
		print(t)
		i, v = t
		print(i,v)

	for t in enumerate(l2):
		print(t)
		i, v = t
		print(i, v)
		i, (v1,v2) = t
		print(i,v1,v2)


	l3 = [("a", "b", "3"), ("c", "d", "4"), ("e", "f", "5")]
	for t in l3:
		print(t)
		v1, v2, v3  = t
		print(v1, v2, v3)
	for v1,v2,v3 in l3:
		print(v1, v2, v3)
	for t in enumerate(l3):
		print(t)
		i, (v1,v2,v3)=t


		

