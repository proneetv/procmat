def crusher(F,D,T,d,i,j):
	y = [0,1,2,3,4,5,6,7,8,9,10,11,12]    #y = []
	C = T/d
	if F <= 255 and C >= 6 and C <= 15: 
		y[0] = 3.76898*(C**1.009449) 	  #output size   ,    y = y + [  expr ]
	if F <= 355 and C >= 13 and C <= 30:
		y[1] = 1.805324*(C**1.095716)   #output size
	if F <= 455 and C >= 27 and C <= 80:
		y[2] = 2.01705*(C**0.890806)   #output size
	if F <= 610 and C >= 40 and C <= 110:
		y[3] = 1.728558*(C**0.883568)   #output size
	if F <= 760 and C >= 75 and C <= 170: 
		y[4] = 0.385634*(C**1.161164)
	if F <= 915 and C >= 110 and C <= 210: 
		y[5] = 0.02041*(C**1.698989)
	if F <= 1065 and C >= 160 and C <= 280: 
		y[6] = 0.057715*(C**1.437366)
	if F <= 1220 and C >= 200 and C <= 350: 
		y[7] =  0.229521*(C**1.146955)
	if F <= 1420 and C >= 300 and C <= 450: 
		y[8] = 1.323601*(C**0.817227)
	if F <= 1070 and C >= 320 and C <= 600: 
		y[9] = 1.105156*(C**0.812629)
	if F <= 1220 and C >= 500 and C <= 775: 
		y[10] = 0.085761*(C**1.16559)
	if F <= 1370 and C >= 620 and C <= 1000: 
		y[11] = 0.085761*(C**1.16559)
	if F <= 1520 and C >= 1000 and C <= 1080: 
		y[12] = 8.53E-11*(C**4.104063)

	R = y[i]/D
	K = [0,1,2,3,4,5,6]
	if R > 1:                                #  :  after every if conditional
		F = R*D
		if F <= 95 and D >= 10 and D <= 31 :
			K[0] = (0.74186*D)**0.971018   # remove all :  they dont come in normal statements
		if F <= 150 and D >= 13 and D <= 37 :
			K[1] = (2.45561*D)**0.818061
		if F <= 210 and D >= 18 and D <= 46 :
			K[2] = (3.03735*D)**0.921907
		if F <= 250 and D >= 18 and D <= 48 :
			K[3] = (2.30775*D)**1.049744
		if F <= 280 and D >= 25 and D <= 59 :
			K[4] = (7.6403*D)**1.049744
		if F <= 380 and D >= 30 and D <= 60 :  
			K[5] = (17.5701*D)**1.049744
		if F <= 510 and D >= 38 and D <= 60 :
			K[6] = (9.86329*D)**1.082183	

	m = C/K[j]
	return "\nNumber of cone crusher required : " + str(int(math.ceil(m)))
