# Makes thingy run
running = 1

# Sets up variables up for use in calculator
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0
z = 0

print('type in math eqation or type exit to exit')
while running:
	print()
	inpt = input(':: ')
	
	if inpt == "exit":
		running = 0
	else:
		try:
			math = eval(inpt)
			print(math)
		except:
			print('Invalid input!')

