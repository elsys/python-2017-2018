

class Date:
	def __init__(self, day, month, year):
		print("constructor called")
		self.day = day
		self.month = month
		self.year = year
	
	def dump(self):
		print(self.day, self.month, self.year)	
	
	def next_day(self):
		self.day += 1
		if self.day > 30:
			self.month += 1
			self.day = 1
		if self.month > 12:
			self.year += 1
			self.month = 1
		
		
d = Date(3, 5, 2018)

# d.month = 5
# d.day = 3
# d.year = 2018

c = Date(30, 6, 2018)
# c.month = 6
# c.day = 30
# c.year = 2018


print(d.month, d.day, d.year)
print(d)
print(c)


d.dump()
c.dump()

c.next_day()
c.dump()


