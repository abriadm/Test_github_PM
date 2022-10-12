class Dog():
	"""A simple attempt to model a dog."""
	def __init__(self, name, age):
		"""Initialized name and age attributes."""
		self.name = name
		self.age = age
		
	def sit(self):
		"""Simulate a dog sitting in response to command."""
		print(self.name.title() + " is now sitting.")
		
	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

# -- try it --

class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		print("\nThis restaurant have a " + self.cuisine_type.title() + ".")
		print("We called " + self.restaurant_name.title())
	
	def open_restaurant(self):
		print( self.restaurant_name.title() + " open every saturday - thursday")
		
restaurant = Restaurant('nasi padang', 'masakan minang')
restaurant.describe_restaurant()
restaurant.open_restaurant()

class User():
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		
	def greet_user(self):
		full_name = self.first_name.title() + " " + self.last_name.title()
		print("\nHello my name is " + full_name + ".")
		
	def describe_user(self):
		print("My name is " + self.first_name.title() + " " + self.last_name.title() + " and I'm lonely now")
		print("Don't have any friends.")
		
profile = User('aldo', 'giveon')
profile.greet_user()
profile.describe_user()

# -- Working with class --

class Car():
	"""A simple attempt to repersent a car."""
	
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = "\n" + str(self.year) + " " + self.make + " " + self.model
		return long_name.title()
		
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

