
#Theory File Name : Multiple hearth roaster and fluidized bed roaster

#Code Author Name : Kapil Verma, Priyanshu Jain, Kalit Kumar Singh
#Roll No : 12341, 12518, 12337


#Input parameters:
		# a1 = %Cu2S per tonne
		# a2 = %Fe2S per tonne
		# a3 = %SiO2 per tonne
		# a4 = %H2O per tonne
		# b1 = %Hydrogen in fuel
		# b2 = %Carbon in fuel
		#fuel= %fuel for a tonne of ore
		# x  = %excess air required


import math
import os


a1   = float(input("Enter the percent of Cu2S per tonne ore:\n"))
a2   = float(input("Enter the percent of FeS2 per tonne ore:\n"))
a3   = float(input("Enter the percent of SiO2 per tonne ore:\n"))
a4   = float(input("Enter the percent of H2O per tonne ore:\n"))
b1   = float(input("Enter the percent of Hydrogen in fuel:\n"))
b2   = float(input("Enter the percent of carbon in fuel:\n"))
fuel = float(input("Enter the percent of fuel for a tonne of ore:\n"))
x    = float(input("Enter the percent of excess air required:\n"))




if (a1+a2+a3+a4) > 100 or (a1+a2+a3+a4) < 100 or (b1 + b2) > 100 or (b1+b2) < 100:

	print ("sum of components of ore/fuel is not 100\n")


elif (a1+a2+a3+a4) == 100 or (b1+b2) == 100:


	def Roaster(a1, a2, a3, a4, b1, b2, fuel, x):
		Na1 = float(a1*10/159)         # Na1 = moles of Cu2S
		Na2 = float(a2*10/119.8)       # Na2 = moles of FeS2
		Na3 = float(a3*10/60)          # Na3 = moles of SiO2

		output = []

		#Calculate amount of CuO, Fe2O3 and SiO2 which add up to get total roasted product
		
		CuO = 2*Na1*79.5

		Fe2O3 = 0.5*Na2*159.6882

		Total_roasted_product = CuO + Fe2O3 + a3*10

		Total_oxygen_consumed =  float(2*Na1) + float((11/4)*Na2) + float((fuel*10*b1*.01)/4) + float((fuel*10*b2*.01)/12)
		print ("\nTotal oxygen consumed(in moles):", Total_oxygen_consumed)
		print ("\n")
		output.append(Total_oxygen_consumed)

		Theoretical_air_required = Total_oxygen_consumed* 4.76 * 22.4

		Experimental_air_required = (1+float(x/100))* Theoretical_air_required

		print ("Total roasted product(in Kg):", Total_roasted_product)
		print ("\n")
		output.append(Total_roasted_product)

		print ("Theoretical air required(in m^3):", Theoretical_air_required)
		print ("\n")
		output.append(Theoretical_air_required)


		print ("Experimental air required(in m^3):", Experimental_air_required)
		print ("\n")
		output.append(Experimental_air_required)

		return(output)

	values = Roaster(a1, a2, a3, a4, b1, b2, fuel, x)

os.system ("pause")	
