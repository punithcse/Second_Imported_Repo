import locale
import sys

class Base_Model():
	trim = 'normal'
	en_li = 1.5
	
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
		
coop = Base_Model(25000)
coop.info()

coop_blue = Base_Model(price=25559, color='blue')
coop_blue.info()

coop_manual_red = Base_Model(32647,'manual','red')
coop_manual_red.info()

coop_manual_green = Base_Model(color='green',trans='manual', price=21313)
coop_manual_green.info()
