import math

class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def dump(self):
		print("x=", self.x, "; y=", self.y)
 
	def __repr__(self):
		return "Point({},{})".format(self.x, self.y)

	def __add__(self, other):
		print("Point.__add__ called...")
		res = Point(self.x, self.y)
		res.sum(other)
		return res
		
	def sum(self, other):
		self.x += other.x
		self.y += other.y

	def sub(self, other):
		self.x -=other.x
		self.y -=other.y


	def dist(self):
		return math.sqrt(self.x*self.x + self.y*self.y)


p1 = Point(2,3)
p2 = Point(-3, 1)
p3 = Point(-1.5, -2.5)

p1.dump()
p2.dump()
p3.dump()

print(p1, p2, p3)

p1.sum(p2)
print(p1)

p1.sub(p2)
print(p1)

print(p1.dist())

p = Point(3,4)
print(p, p.dist())

print(p1, p2, p)
p = p1 + p2
print(p1, p2, p)





