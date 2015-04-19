




#Theory filename: Primary and Secondary Crusher
#Theory file Authors: Aditya, Devendra



#Code Authors Name: Aman Singhal, Manoj Kumar, Mukul Janbandhu, Priyanshu Jain
#Roll Numbers: 12088,12401,12426,12518


#libraries imported to use fuctions in code

import math
import os
import sys

	
#Input parameters:
		
#F =  feed size (in mm)
#D =  Desired discharged size (in mm)
#T =  Plant throughput (tonnes/hours)
#d =  Bulk density of ore (tonnes/cubic metre)
#i =  seried ID
#j =  series number
#m =  Number of cone crusher required



def Primery_and_secondary_crusher (F,D,T,d):



	#y = dischage size of ore after passing through a particular crusher (in mm) 
	#C = capacity (cubic metre/hr)


	y = [0,1,2,3,4,5,6,7,8,9,10,11,12]    

	C = T/d

	if F > 1420 :
		print "Feed size is not in range [feed range(0 to 1420)] "
		sys.exit()





	print "\nYour options for primary crusher are :- "


	#Equation of each curve y= b*(C)^m
	#y = dischage size (in mm) 
	#C = capacity (cubic metre/hr)
	#b = constant of equation for each crusher 




	#Selection of Jaw crushers

	#possibilities of primery jaw crushers based on the feed opening and the discharge size which will be choosen by user 
	#check the feed size < feed opening and also whether the capacity is in the range of the given crusher

	if F <= 255 and C >= 6 and C <= 15: 
		print "Jaw_crusher_1 \n  Feed Opening = 255 * 405(mm*mm)\n dischage size = "
		y[0] = 3.76898*(C**1.009449) 	  
		print y[0]
		print " mm\n"

	if F <= 355 and C >= 13 and C <= 30:
		print "Jaw_crusher_2 \n Feed Opening = 355 * 610(mm*mm)\n dischage size = "
		y[1] = 1.805324*(C**1.095716)  
		print y[1]
		print " mm\n"

	if F <= 455 and C >= 27 and C <= 80:
		y[2] = 2.01705*(C**0.890806)   
		print "Jaw_crusher_3 \n Feed Opening = 455 * 915(mm*mm)\n dischage size = "
		print y[2]
		print " mm\n"

	if F <= 610 and C >= 40 and C <= 110:
		y[3] = 1.728558*(C**0.883568)   
		print "Jaw_crusher_4 \n Feed Opening = 610 * 915(mm*mm)\n dischage size = "
		print y[3]
		print " mm\n"

	if F <= 760 and C >= 75 and C <= 170: 
		y[4] = 0.385634*(C**1.161164)
		print "Jaw_crusher_5 \n Feed Opening = 760 * 1065(mm*mm)\n dischage size = "
		print y[4]
		print " mm\n"

	if F <= 915 and C >= 110 and C <= 210: 
		y[5] = 0.02041*(C**1.698989)
		print "Jaw_crusher_6 \n Feed Opening = 915 * 1220(mm*mm)\n dischage size = "
		print y[5]
		print " mm\n"

	if F <= 1065 and C >= 160 and C <= 280: 
		y[6] = 0.057715*(C**1.437366)
		print "Jaw_crusher_7 \n Feed Opening = 1065 * 1220(mm*mm)\n dischage size = "
		print y[6]
		print " mm\n"

	if F <= 1220 and C >= 200 and C <= 350: 
		y[7] =  0.229521*(C**1.146955)
		print "Jaw_crusher_8 \n Feed Opening = 1220 * 1525(mm*mm)\n dischage size = "
		print y[7]
		print " mm\n"

	if F <= 1420 and C >= 300 and C <= 450: 
		y[8] = 1.323601*(C**0.817227)
		print "Jaw_crusher_9 \n Feed Opening = 1420 * 1820(mm*mm)\n dischage size = "
		print y[8]
		print " mm\n"





	#Selection of Gyratory crusher



	#possibilities of primery Gyratory crushers based on the feed opening and the discharge size which will be choosen by user



	#Equation of each curve y= b*(C)^m
	#y = dischage size (in mm) 
	#C = capacity (cubic metre/hr)
	#b = constant of equation for each crusher 


	#check the feed size < feed opening and also whether the capacity is in the range of the given crusher

	if F <= 1070 and C >= 320 and C <= 600: 
		y[9] = 1.105156*(C**0.812629)
		print "Gyratory_crusher_1 \n Feed Opening = 1070 mm \n dischage size = "
		print y[9]
		print " mm\n"

	if F <= 1220 and C >= 500 and C <= 775: 
		y[10] = 0.085761*(C**1.16559)
		print "Gyratory_crusher_2 \n Feed Opening = 1220 mm\n dischage size = "
		print y[10]
		print " mm\n"

	if F <= 1370 and C >= 620 and C <= 1000: 
		y[11] = 0.085761*(C**1.16559)
		print "Gyratory_crusher_3 \n Feed Opening = 1370 mm\n dischage size = "
		print y[11]
		print " mm\n"

	if F <= 1520 and C >= 1000 and C <= 1080: 
		y[12] = 8.53E-11*(C**4.104063)
		print "Gyratory_crusher_4 \n Feed Opening = 1520 mm\n dischage size = "            
		print y[12]
		print " mm\n"


	#if the input from the user is not in given range and it will exit the code



	i = int(raw_input("\nEnter the series number : "))




	#Selection of Cone crusher

	# R = Reduction ratio
	# y = Discharge size (in mm)

	R = y[i-1]/D

	K = [0,1,2,3,4,5,6]


	#possibilities of secondary Cone crushers based on the feed opening and the discharge size which will be choosen by user
	#check Reduction ratio > 1 , means we did not got the desired size from primery crushers ,so have to use secondary crushers
	#check the feed size < feed opening and also whether the capacity is in the range of the given crusher

	if R > 1:                            
		F = R*D
		print "\nyour options for Secondary crusher are :-"
		if F <= 95 and D >= 10 and D <= 31 :
			print "Cone_crusher_1 \n Feed Opening = 95 mm"
			K[0] = (0.74186*D)**0.971018   

		if F <= 150 and D >= 13 and D <= 37 :
			print "Cone_crusher_2 \n Feed Opening = 150 mm"
			K[1] = (2.45561*D)**0.818061
			
		if F <= 210 and D >= 18 and D <= 46 :
			print "Cone_crusher_3 \n Feed Opening = 210 mm"
			K[2] = (3.03735*D)**0.921907
			
		if F <= 250 and D >= 18 and D <= 48 :
			print "Cone_crusher_4 \n Feed Opening = 250 mm"
			K[3] = (2.30775*D)**1.049744
			
		if F <= 280 and D >= 25 and D <= 59 :
			print "Cone_crusher_5 \n Feed Opening = 280 mm"
			K[4] = (7.6403*D)**1.049744
			
		if F <= 380 and D >= 30 and D <= 60 :  
			print "Cone_crusher_6 \n Feed Opening = 380 mm"
			K[5] = (17.5701*D)**1.049744

		if F <= 510 and D >= 38 and D <= 60 :
			print "Cone_crusher_7 \n Feed Opening = 510 mm"
			K[6] = (9.86329*D)**1.082183	



	if R <= 1 :
		print "you had your desired discharge size only using primery crusher "
		sys.exit()
	#no of cone crushers required to crush the ore to the desired discharge size




	j = int(raw_input("\nEnter the series number : "))
	m = C/K[j-1] #number of cone crusher required
	print "\nNumber of cone crusher required : " + str(int(math.ceil(m))) +'\n'

		

		#Output parameter:
		    #Number of cone crusher required
		    #example:-(to check the validity of the code)
		    #Feed size= 750 mm ; desired discharged size = 20 mm ; plant troughput = 600 t/h ; density of ore = 2 tonnes/ metre cube
		    #series no for primery = 9, series no for secondary crusher = 4
		    #Ans = 6


	os.system("pause")
