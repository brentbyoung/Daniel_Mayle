class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print 'Price is: $' + str(self.price)
        print 'Max speed: ' + str(self.max_speed) + 'mph'
        print 'Total miles: ' + str(self.miles) + ' miles'
        return self

    def drive(self):
        print 'Driving'
        self.miles += 10
        return self

    def reverse(self):
        print 'Reversing'
        # prevent negative miles
        if self.miles >= 5:
            self.miles -= 5
        return self

# create instances and run methods
bike1 = Bike(99.99, 12, 0)
bike1.drive().drive().reverse().displayInfo()