 # Theory file name: Drying program without prosity
 # Theory Author name: Chandrakanta, Pritul 
 # Code author name: Krashnavtar (12361), Mukul Janbandhu (12426)


 # a is constant to decide the solution by graph or without graph
 # tc =time for constant drying 
 # tf =time during first falling condition 
 # tt =total time of constant and first falling
 # Rc =rate of constant falling 
 # Rf =slope of first falling condition 
 # y1, y2 and y3 are initial moisture content, critial moisture content, and final moisture content respectably
 # R and P are reynolds number and parental number respectly 
 # h is heat transfer coefficient 








import math
import os
import sys


def drying():

	a = int(raw_input("if you want to solve with graph(R(rate of drying) vs X(moisture containt)) then press 1 and without graph press 2 : \n"))


	if a  == 1 :

		#input parameters

		m = float(raw_input("enter m {mass of dry solid (kg/m2)} :"))
		Xi = float(raw_input("initial moisture content in dry solid (%):"))
		Xc = float(raw_input("moisture content in dry solid after constant drying region(kg/kg dry solid ):"))
		Rc = float(raw_input("drying rate at the critical point X2 *10^(-3)(kg/m2.s):"))
		Xf = float(raw_input("final moisture content in dry solid (%):"))
		Rf = float(raw_input("drying rate corresponding final moisture content  *10^(-3)(kg/m2.s):"))

		
		Rc = Rc * (10**(-3))
		
		Rf = Rf * (10**(-3))

		y1 = Xi / (100 - Xi)
		
		y3 = Xf / (100 - Xf)


		print y1,y3

		tc = (m * ( y1 - Xc ) ) / (Rc)

		print ((math.log(Rc/Rf)))


		tf = (m * (( Xc- y3)/ (Rc - Rf))) * ((math.log(Rc/Rf)))

		print "constant falling rate time:",tc,"s","\nfirst falling rate time:",tf,"s\n"


		tt = tc + tf

		print "Total time :",tt,"s"


		return tt








	if a == 2 :
		

		#input parameters

		m = float(raw_input("enter m {mass of dry solid (kg/m2)} :"))
		X1 = float(raw_input("initial moisture content in dry solid (%):"))
		X3 = float(raw_input("final moisture content in dry solid (%):"))
		D = float(raw_input("diameter(m):"))
		r = float(raw_input("density of the fluid (kg/m3):"))
		n = float(raw_input("dynamic viscosity of the fluid (kg/m.s):"))
		C = float(raw_input("specific heat (J/kg.K):"))
		v = float(raw_input("mean velocity of object relative to fluid (m/s):"))
		T = float(raw_input("temperature of air(K):"))
		Tw = float(raw_input("wet bulb temperature(K):"))
		L = float(raw_input("latent heat of vaporization (J/kg):"))
		K = float(raw_input("thermal conductivity (W/m.K):"))
		
		y1 = X1 / ( 100-X1 )

		
		y3 = X3 / (100 - X3)

		
		R = r*v*D/n

		
		P = C*n/K

		
		h = 1.17 * (K/D) * (R**(0.585)) * (P**(0.33333))
		
		Rc = h * (T-Tw) / L
		

		tc = (m * ( y1 - y3 ) ) / (Rc)


		

		print "Total constant rate time :",tc,"s"

		return tc

	os.system("pause")	

	