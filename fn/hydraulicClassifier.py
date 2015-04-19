
def terminalVelocity(dia, density_Particle, density_Fluid, coeff_Viscosity):
	g = 9.8
	v = g*dia*dia*(density_Particle-density_Fluid)/(18*coeff_Viscosity)									
	return v

def flowRate(d, v):
	r = (22/7)*d*d*(v)/4									
	return r

def hydraulicClassifier():
	print("Enter the number of classifiers:")
	n=int(input())			

	#user input for dimension of each classifier
	classifier_dia = []
	for i in range(n):
		print('Enter the value for upper diameter of the conical classifier ' ,i+1,'(in m):')
		d = float(input())
		classifier_dia.append(d)																					

	print('\nNow enter the values of critical particle size in each classifier above which  the particles will end up in underflow else will be in overflow \n')

	#user input for particle sizes in each classifier
	particle_dia = []
	for i in range(n):
		print('Critical diameter of particles in classifier ' ,i+1, '(in m):')
		dia = float(input())
		particle_dia.append(dia)

	print("\nEnter Density of Particles (in kg/m^3): ")
	density_Particle = float(input())																		

	print("\nEnter Density of Fluid (in kg/m^3): ")
	density_Fluid = float(input())

	print("\nEnter the value of Viscosity (in kg/m-s): ")
	coeff_Viscosity = float(input())

	#calculating terminal velocity in each classifier
	terminal_Velocity = []
	for i in range(n):																						
		velocity = terminalVelocity(particle_dia[i], density_Particle, density_Fluid, coeff_Viscosity)
		terminal_Velocity.append(velocity)

	#calculating flow rate in each classifier
	flow_Rate = []
	for i in range(n):																						
		r = flowRate(classifier_dia[i], terminal_Velocity[i])
		flow_Rate.append(r)

	print('\nTerminal Velocity in each classifier:\n')

	#printing terminal velocity in each classifier
	for i in range(n):																						
		print ("Terminal velocity in classifier", i+1, "(in m/s):", str(terminal_Velocity[i])[:4] )	

	print('\nFlow Rate in each classifier:\n')

	#printing flow rate for each classifier
	for i in range(n):
		print ("Flow rate in classifier", i+1, "(in m^3/s):", str(flow_Rate[i])[:4])

hydraulicClassifier()		