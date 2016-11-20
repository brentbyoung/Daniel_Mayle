class Animal(object):
	def __init__(self, name):
		print "New animal: "
		self.name = name
		self.health = 100
	
	def walk(self):
		self.health -= 1
		return self
	
	def run(self):
		self.health -= 5
		return self
	
	def displayHealth(self):
		print 'Animal name: ' + str(self.name)
		print 'Health: '	+ str(self.health)
		return self


class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150

	def pet(self):
		self.health +=5
		return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print "This is a dragon"
        super(Dragon, self).displayHealth()

animal = Animal('Roger')
animal.walk().walk().walk().run().run().displayHealth()


dog = Dog('Odie')
dog.walk().walk().walk().run().run().pet().displayHealth()

dragon = Dragon('Bahamut')
dragon.fly().displayHealth()


