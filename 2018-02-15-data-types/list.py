
l1 = list(range(10))
print(l1)

l2 = [v*v for v in l1]
print(l2)

l3 = [v*v*v for v in l1 if v % 3 !=0]
print(l3)

l4 = [[v,w] for v in l1 for w in l2 if v%3== 0 and w%3 ==0]
print(l4)


l5 = [v*v for v in range(10)]
print(l5)


res = [[i,j,k] 
	for i in range(2) 
	for j in range(3) 
	for k in range(2) if i+j+k ==2]
print(res)






