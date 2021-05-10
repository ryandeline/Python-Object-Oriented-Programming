# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
	def __init__(self, title, author, pages, price):
		self.title = title
		# TODO: add properties
		self.author = author
		self.pages = pages
		self.price = price
		self.__secret = 'This is a secret attribute'

	def getprice(self):
		if hasattr(self, '_discount'):
			return self.price - (self.price * self._discount)
		else:
			return self.price

	def setdiscount(self, amount):
		self._discount = amount

# TODO: create some Book instances
b1 = Book('War and Peace', 'Leo Tolstoy', 1225, 39.95)
b2 = Book('The Catcher in the Rye', 'JD Salinger', 234, 29.95)



# TODO: print the class and property
#print(b1)
#print(b1.title)

# TODO: print the price of  book1
# print(b1.getprice())

# # TODO: tye setting the discount
# print(b2.getprice())
# b2.setdiscount(0.25)
# print(b2.getprice())


#TODO: properties with double underscores are hidden by the interpreter
# print(b2._Book__secret) #Double underscore prevents other assignments to be overwritten

class Book:
	def __init__(self, title):
		self.title = title

class Newspaper:
	def __init__(self, name):
		self.name = name

	# def getprice(self):
	# 	if hasattr(self, '_discount'):
	# 		return self.price - (self.price * self._discount)
	# 	else:
	# 		return self.price

	# def setdiscount(self, amount):
	# 	self._discount = amount

# TODO: create some Book instances
b1 = Book('The Catcher in the Rye')
b2 = Book('The Grapes of Wrath')
n1 = Newspaper('The Washington Post')
n2 = Newspaper('The New York Times')

# # TODO: use type() to inspeect the object type
# print(type(b1))
# print(type(n1))

# # TODO: compare two types together
# print(type(b1) == type(b2))
# print(type(b1) == type(n2))

# TODO: use isinstance to compare a specific instance to a known type
print(isinstance(b1, Book))
print(isinstance(n1, Newspaper))
print(isinstance(n2, Book))
print(isinstance(n2, object))