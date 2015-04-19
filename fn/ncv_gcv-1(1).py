#Theory filename: Calorific Value of Industrial fuels
#Theory file Authors: Ankur Patel

#Code Authors Name: Swathi Krishna, Krashnavatar, Kalit Singh
#Roll Numbers: 12750,12361,12337


	  		
import sys
import decimal

	#Input parameters:
		#N=Total number of hydrocarbons(1-5)(int)
		#C[i]=Index of the hydrocarbon according to the displayed list (1-5)(int)
		#per[i]=percentage of the hydrocarbon entered (float)



def heatl(a,b,c,d,e): 								#Calculates heat of combustion when H2O is in liquid state"""
	
	#a=	Heat of formation of the hydrocarbons
	#b=	Number of CO2 moles in the balanced chemical equation
	#c=	Number of H2O moles in the balanced chemical equation
	#d= Heat of formation of H2O(l)
	#e= Heat of formation of CO2
 	hcl=(c*d)+(b*e)-a
	return hcl





def heatv(a,b,c,d,e): #Calculates heat of combustion when H2O is in vapor state"""
	
	#a=	Heat of formation of the hydrocarbons
	#b=	Number of CO2 moles in the balanced chemical equation
	#c=	Number of H2O moles in the balanced chemical equation
	#d= Heat of formation of H2O(v)
	#e= Heat of formation of CO2   

	hcv=(c*d)+(b*e)-a
	return hcv
	

													#The first two lists store number of moles of CO2 and H2O in the balanced equations 

CO2 = [1,2,2,2,3]
H2O = [2,1,2,3,4]
Hof = [-29600,-97200,-68320,-57800,-70960,-94450]
HOHC = [-17890,54190,12500,-20240,-24820]

N = int(raw_input("\nEnter the total number of Hydrocarbons (Input Range : 1-5 ): "))

if(N>5 or N<1):

	print " The total number of Hydrocarbons should not exceed 5\nExiting\n"
	#os.system("pause")
	sys.exit()
else:
	i = 0
	C = [ 0 for i in range(0,N)]
	i = 0
	per = [0.0 for i in range(0,N)]
	i =0
	

	#PRINT Numeric Legends for hydrocarbons
	print "\nLegends:- CH4 - 1;  C2H2 - 2; C2H4 - 3; C2H6 - 4; C3H8 - 5\n"
	sum=0	
	while(i < N):
		
		C[i] = int(raw_input("Enter the Serial ID of " + str(i+1) + " hydrocarbon : "))
		if(C[i]>5 or C[i]<1):
			print "Legend not chosen properly\nExiting\n"
			sys.exit()
		else:
			per[i] = float(raw_input("Enter the percentage(by mass) of hydrocarbon entered: "))
			if(per[i]>100 or per[i]<0):
				print "Percentage value entered is either negative or exceeding 100\nExiting\n"
				sys.exit()
			else:
				sum+=per[i]
				if(sum>100):
					print"Total percentage has exceeded 100, which does not make sense\nExiting\n"
					sys.exit()
				else:
					i+=1
			



	i = 0
	net = 0.000
	gross = 0.000
	while(i < N):
		j = 0
		while(j < 5):
			if ((C[i]-1) == j):
				
				net +=  (abs(heatv(HOHC[j], CO2[j], H2O[j], Hof[3], Hof[1]))*per[i]/100)
				gross += (abs(heatl(HOHC[j], CO2[j], H2O[j], Hof[2], Hof[1]))*per[i]/100)
																		#Calculating net calorific value and gross calorific value
			j += 1
		i+=1

	
	#Output Parameters:
			#Net= The value of the net calorific value
			#Gross= The  value of the  gross calorific value
	#Example:
		#Total number of hydrocarbons=3
		#Hydrocarbon legend=1,percentage=94%
		#Hydrocarbon legend=4,percentage=3%
		#Hydrocarbon legend=5,percentage=0.5%
		#Answer net calorific value=196132.1 kcal/kg-mole of natural gas
		#Answer gross calorific value=217066.9 kcal/kg-mole of natural gas
	


	print "The Net Calorific Value (|NCV|): " , round(net,2) , "kcal/kg-mole of natural gas"
	print "The Gross Calorific Value (|GCV|): ", round(gross,2) , "kcal/kg-mole of natural gas"



																		#Printing the Calorific values
