import turtle


class Hilbert(object):
	
	def __init__(self, step):
		self.step = step
		self.pen = turtle.Pen()
		self.pen.up()
		self.pen.goto(300, 300)
		self.pen.down()
	
	def a(self, i):
		if i<=0:
			return
	
		self.d(i-1)
		
		self.pen.setheading(180)
		self.pen.forward(self.step)
		
		self.a(i-1)
		self.pen.setheading(270)
		self.pen.forward(self.step)
		
		self.a(i-1)
		self.pen.setheading(0)
		self.pen.forward(self.step)
		
		self.b(i-1)

	def b(self, i):
		if i<= 0:
			return
		
		self.c(i-1)
		self.pen.setheading(90)
		self.pen.forward(self.step)
		
		self.b(i-1)
		self.pen.setheading(0)
		self.pen.forward(self.step)
		
		self.b(i-1)
		self.pen.setheading(270)
		self.pen.forward(self.step)
		
		self.a(i-1)
		
	
	def c(self, i):
		if i<=0:
			return
		
		self.b(i-1)
		
		self.pen.setheading(0)
		self.pen.forward(self.step)
		
		self.c(i-1)
		self.pen.setheading(90)
		self.pen.forward(self.step)
		
		self.c(i-1)
		self.pen.setheading(180)
		self.pen.forward(self.step)
		
		self.d(i-1)
	
	def d(self, i):
		if i<=0:
			return
		self.a(i-1)
		
		self.pen.setheading(270)
		self.pen.forward(self.step)
		
		self.d(i-1)
		
		self.pen.setheading(180)
		self.pen.forward(self.step)
		
		self.d(i-1)
		
		self.pen.setheading(90)
		self.pen.forward(self.step)
		
		self.c(i-1)


if __name__ == "__main__":
	h = Hilbert(10)
	h.d(5)
	
	
	input("Press any key")

