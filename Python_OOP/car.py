class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        print "New Car!"
        self.speed = speed 
        self.fuel = fuel
        self.mileage = mileage
        self.price = price
        if price > 10000:
           self.tax = .15
        else:
            self.tax = .12
        self.display_all()

    def display_all(self):
        print 'Price: ' + str(self.price)
        print 'Speed: ' + str(self.speed) + 'mph'
        print 'Fuel: ' + self.fuel
        print 'Mileage: ' + str(self.mileage) + 'mpg'
        print 'Tax: ' + str(self.tax)
        
car1 = Car(2000, 35, '30 Gallons', 15)
car2 = Car(2000, 5, '25 Gallons', 105)
car3 = Car(2000, 15, '35 Gallons', 95)
car4 = Car(2000, 25, '50 Gallons', 25)
car5 = Car(2000, 45, '60 Gallons', 25)
car6 = Car(20000000, 35, '20 Gallons', 15)