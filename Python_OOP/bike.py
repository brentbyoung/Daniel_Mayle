class Bike(object):
	def __init__(self, price, max_speed, miles):
		print "New Car!"
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
	def displayinfo(self):
		print self.price
		print self.max_speed
		print self.miles
	def ride(self):
		print "Riding"
		self.miles +=10
	def reverse(self):
		print "Reversing"
		self.miles -=5







harley = Bike('$10000', '75MPH', 0)
harley.ride()
harley.ride()
harley.ride()
harley.reverse()
harley.displayinfo()

honda = Bike('$20000', '100MPH', 0)
honda.ride()
honda.ride()
honda.reverse()
honda.reverse()
honda.displayinfo()

hellraiser = Bike('$50000', '200MPH', 0)
hellraiser.reverse
hellraiser.reverse
hellraiser.reverse
hellraiser.displayinfo()
