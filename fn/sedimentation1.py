#Theory File Name : Sedimentaion Classifiers
#Theory File Authors : Jay Mehta and Balendu Shekhar

#Code Author Name : Prashant Anand
#Roll No : 11521


import math

#Input Parameters

# w : rate (in tph) (int)
# dp : separation size (in  micrometer) (int)
# R1 : inner radius (in cm) (int)
# Pf : density of fluid  (in kg/m3) (int)
# Pp : density of solid  (in kg/m3) (int)
# uf : viscosity of fluid (in Pa s) (float)

def sedimentationClassifiers(w,dp,R1,Pf,Pp,uf):

	Q = (((w * 1000)/(2.0*Pf)) + ((w*1000)/(2.0*Pp)))/3600
	# Q : bulk flow rate
	
	Voo = (9.8 * dp * dp * 0.000001*0.000001 *(Pp-Pf))/(18*uf)
	
	R_1 = (Q/(2*3.14*Voo)) + (R1*R1*0.01*0.01)
	R = math.sqrt(R_1)
	# R : outer radius
	D = 2*R
	
	T1 = ((2 * 3.14 *1)*((R*R) - (R1*R1*0.01*0.01)))/Q
	H = T1 * Voo
	
	
	outputList = []
	outputList.append( D )
	outputList.append( H )
	
	#output parameter:
	# D : outer diameter
	# H : height
	
	#example
	#Rate = 500tph, Separation Size = 75 micro meter, Inner radius= 20 cm, Density of water = 1000 kg/m3, Density of solid = 2650 kg/m3, Viscosity of water = 0.001 Pa s
	#Ans :  D = 3.5 m
	#		H = 1 m
	
	return outputList

w = int(raw_input("Enter rate (in tph) = "))
dp = int(raw_input("Enter separation size (in  micrometer) = "))
R1 = int(raw_input("Enter inner radius (in cm) = "))
Pf = int(raw_input("Enter density of fluid  (in kg/m3)= "))
Pp = int(raw_input("Enter density of solid  (in kg/m3)= "))
uf = float(raw_input("Enter viscosity of fluid (in Pa s) = "))
print sedimentationClassifiers(w,dp,R1,Pf,Pp,uf)
print raw_input("Press<Enter>")
