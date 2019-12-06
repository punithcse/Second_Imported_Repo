import random
faces = ('heads','tails')

'''
def subproc():
	print(' i do something')
	print('but return nothing')
	
subproc()
print(subproc())
'''

def greet():
	return random.choice(faces)
	
def test_greet():
	for loop in range(8):
		print(greet())
	print("test completed")
	

if __name__ == '__main__':
	greet()
	test_greet()
	

