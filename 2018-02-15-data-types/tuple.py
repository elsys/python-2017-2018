


l2 = [1,2]
t2 = (1, 2)

print(type(l2))

print(type(t2))

l2.append(3)

print(l2)

# t2.append(3)


t3 = tuple(l2)
print(t3)


print(hash(t3))
print(hash(t2))

# print(hash(l2))

line = input()
print("line:" , line)
str_list = line.split()
print("str_list:", str_list)

integer_list = list(map(int, str_list))
print(integer_list)





