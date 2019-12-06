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

class Sport_model(Base_Model):
	en_li = 2.0
	
	def eng_sound(self):
		return 'vromm, vrrom'
	
	def horn_sound(self):
		return 'beep, beep'
		
	def __str__(self):
		return 'Sport Model' 
		
coop_sport = Sport_model()
print('%s has %s trim level' % (coop_sport, coop_sport.trim))
print('%s has %s liter engine' % (coop_sport, coop_sport.en_li))
print('%s engine sounds like %s' % (coop_sport, coop_sport.eng_sound()))
print('%s horn sounds like %s' % (coop_sport, coop_sport.horn_sound()))

class Lux_model(Base_Model):
	en_li = 2.0
	
	def eng_sound(self):
		return 'Vromm, Vrrom'
	
	def horn_sound(self):
		return 'hunk, hunk'
		
	def __str__(self):
		return 'Lux Model'

class Lux_Sport_Model(Lux_model, Sport_model):
	def __str__(self):
		return 'Lux Sport Model'

coop_lux_sport = Lux_Sport_Model()
print('%s has %s trim level' % (coop_lux_sport, coop_lux_sport.trim))
print('%s has %s liter engine' % (coop_lux_sport, coop_lux_sport.en_li))
print('%s engine sounds like %s' % (coop_lux_sport, coop_lux_sport.eng_sound()))
print('%s horn sounds like %s' % (coop_lux_sport, coop_lux_sport.horn_sound()))




