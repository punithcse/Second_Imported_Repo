#Startd Coding in Pyhton!!
class Base_Model():
	trim = 'normal'
	en_li = 1.5
	
	def eng_sound(self):
		return 'putt, putt'
		
	def horn_sound(self):
		return 'beep, beep'
		
	def __str__(self):
		return 'Base Model'
	

coop = Base_Model()
print('%s has %s trim level' % (coop, coop.trim))
print('%s has %s liter engine' % (coop, coop.en_li))
print('%s engine sounds like %s' % (coop, coop.eng_sound()))
print('%s horn sounds like %s' % (coop, coop.horn_sound()))
