''' Demonstrate class properties '''
class Grader():
	def __init__(self, score=0):
		self.score = score

math = Grader(90)
print('The math score was %s.' % math.score)
math.score = 101
print('The math score was changed to %s.' % math.score)

class Grades():
	def __init__(self, score=0):
		self.score = score
		
	@property 
	def score(self):
		return self.score
	
	@score.setter
	def score(self, value):
		if value > 100 or value < 0:
			raise ValueError('Invalid score')
		self._score = value
		
math = Grader(90)
print('The math score was %s.' % math.score)
try:
	math.score = 101
except ValueError:
	print("the score is not allowed")
	
class ReadOnly():
	@property
	def constant(self):
		return 24
		
only_read = ReadOnly()
print('the constant has the value:', only_read.constant)
try:
	only_read.constant = 25
except AttributeError:
	print('properties cannot be changed without a setter')
	
class HardWay():
	def __init__(self, value):
		self.hardset(value)
		
	harddoc = 'Properties can have getter, setter, deleter and doc string'
	def hardset(self, value):
		if value:
			self.way = True
		else:
			self.way = False
	def hardget(self):
		return self.way
	def harddel(self):
		self.way = None
	hard = property(fget=hardget, fset=hardset, fdel=harddel, doc=harddoc)
	

not_decorated = HardWay(1)
not_decorated.hard = 'test'
print('the value not decorated.hard is', not_decorated.hard)
del not_decorated.hard
print('the value not decorated.hard is', not_decorated.hard)
not_decorated.hard = 'testing again'
print('the value not decorated.hard is', not_decorated.hard)
print('HardWay.hard.__doc__')











		
		
	

	

