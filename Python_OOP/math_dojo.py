# PART I
# Create a Python class called MathDojo that has the methods  add and subtract. 
# Have these 2 functions take at least 1 parameter. 
# Then create a new instance called md. It should be able to do the following task:

class MathDojo(object):
	def __init__(self):
		self.summed = 0
	def add(self, *numbers):
		for x in numbers:
			self.summed = self.summed + x
		return self
	def subtract(self, *numbers):
		for x in numbers:
			self.summed = self.summed - x
		return self
	def result(self):
		print(self.summed)

md = MathDojo()
md.add(2).add(2, 5).subtract(2, 3).result()


# PART II
# Modify MathDojo to take at least one integer(s) and/or list(s) 
# as a parameter with as many value passed in the list. 
# It should now be able to perform the following tasks:
class MathDojo2(object):
	def __init__(self):
		self.summed = 0
	def add(self, *args, **kwargs):
		for x in args:
			if type(x) is list:
				for i in x:
					self.summed = self.summed + i
		for x in args:
			if type(x) is int:
				self.summed = self.summed + x
		return self
	def subtract(self, *args, **kwargs):
		for x in args:
			if type(x) is list:
				for i in x:
					self.summed -= i
		for x in args:
			if type(x) is int:
				self.summed = self.summed - x
		return self
	def result(self):
		print(self.summed)

md2 = MathDojo2()
md2.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()

# PART III
# Make any needed changes in MathDojo in order to support tuples of 
# values in addition to lists and singletons.  
class MathDojo3(object):
	def __init__(self):
		self.summed = 0
	def add(self, *args, **kwargs): 
		for x in args:
			if type(x) is int:
				self.summed = self.summed + x
		for x in args:
			if type(x) is list:
				for i in x:
					self.summed = self.summed + i
		for x in args: 
			if type(x) is tuple:
				for i in x:
					self.summed += i
		return self
	def subtract(self, *args, **kwargs):
		for x in args:
			if type(x) is int:
				self.summed = self.summed - x
		for x in args:
			if type(x) is list:
				for i in x:
					self.summed -= i
		for x in args:
			if type(x) is tuple:
				for i in x:
					self.summed -= i
		return self 
	def result(self):
		print(self.summed)

md3 = MathDojo3()
tup = (1,3,4)
md3.add(tup, [1,2,3], 9, 8, 10).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()
