import locale
import sys

class Base_Model():
	trim ='normal'
	en_lit = 1.5
	mile_range=450
	tank_cap = 45
	color='white'
	trans='auto'
	
	@classmethod
	def miles_per_liter(cls):
		return cls.mile_range / cls.tank_cap
		
	@classmethod
	def miles_per_gallon(cls):
		return cls.miles_per_liter() * 3.78541
		
	def __init__(self, price, trans='auto', color='white'):
		self.price = price
		self.trans = trans
		self.color = color
	
	def info(self):
		if sys.platform.startswith('win'):
			locale.setlocale(locale.LC_ALL, 'us')
		else:
			locale.setlocale(locale.LC_ALL, 'en_US.utf8')
		print('the price of %s was %s ' % (self, locale.currency(self.price)))	
		
	def __str__(self):
		return 'a %s  base model with %s trans' % (self.color, self.trans)
		
coop = Base_Model(color='green',trans='auto', price=21313)
coop.info()
print('The %s gets %4.1f miles per gallon' % (coop, coop.miles_per_gallon()))
print('The %s gets %4.1f miles per liter' % (coop, coop.miles_per_liter()))
print('The %s gets %4.1f miles per gallon' % (Base_Model, Base_Model.miles_per_gallon()))




