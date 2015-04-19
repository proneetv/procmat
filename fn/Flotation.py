#Theory filename: Floatation Algorithm by-mani-and-nm"
#Theory file Authors:G.Mani Ratnam, K.Narayanamurthy,Kuldeep Merottha

#Code Authors Name: Shantanu Sharma,Anil Kumar
#Roll Numbers: 12655,12114



import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import pylab
import sys
import decimal

#Input Parameters:
	#Time Range(T)(float)
	#time interval(t)(float)
	#Order of reaction(n)(int)
	#Residence time(T1)(float)
	#Number of cells(N)(int)



																				#print('input time range from 0 to')		
T = float(raw_input('Input total time range T(min) = '))
if (T<0):
	print"Error,Total time less than 0\nInvalid\nExiting"
	sys.exit()
																					#print('Input time interval')
t = float(raw_input('Input sampling time t(min) = '))
if(t>T):
	print"Error\nTime interval greater than Total time\nInvalid\nExiting"
	sys.exit()
if(t<0):
	print"Error,Total time less than 0\nInvalid\nExiting"
	sys.exit()
																					#print('input order of rxn')
n = int(raw_input('Input order of your reaction, n = '))
if ((n < 1) and (n	> 2)):
	print "Error\nWrong Input\nOrder of reaction has to be 1 or 2\nExiting"
	sys.exit()
																					#print('input residence time')
T1 = float(raw_input('Input residence time T1(min) = '))
if(T1<0):
	print"Error,Total time less than 0\nInvalid\nExiting"
	sys.exit()
																					#print('input no of cells')
N = int(raw_input('Input total number of cells, N = '))


num = T/t
num = int(num)																		#no of iteration for for loop
#print num



conc = []																			#Lists to store concn and time
time = []
for i in range(0,num+1):															#loop to input conc with time
    																				#print'input concn at time',i*t,'mins'
   
    conc.append(float(raw_input('Concentration(gm/ml) at time ' +str(i*t)+ ' mins = ' )))                    
    time.append(i*t	)																#adding time to list

#print conc
#print time
  

m=[[]]																				#List to show Concn vs time
m[0].extend([conc[0],time[0]])
for i in range(1, num+1):
    m.append([conc[i],time[i]])

def exponential_fit(x, a, b, c):													#Function of Conc vs time
 	return a*np.exp(-b*x) + c

if __name__ == "__main__":
    x = np.array(time)
    y = np.array(conc)	    
    fitting_parameters, covariance = curve_fit(exponential_fit, x, y)
    a, b, c = fitting_parameters
    next_x =  float("inf")
    next_y = exponential_fit(next_x, a, b, c)

    #plt.plot(y)
    #plt.plot(np.append(y, next_y), 'ro')
    #plt.show()    
#print m


c_infi = next_y
#print c_infi
c_zero = conc[0]

																					#to calculate ((c_zero - c_infi)/(c - c_infi))



ratio = []																			#Empty lists for storing ratio and its ln
ln_ratio = []
for i in range(0,num+1):															#loop to calculate Ratio for each time
     c = conc[i]
     Ratio = float(float(c_zero - c_infi)/float(c - c_infi))
     ln_Ratio = np.log(Ratio)
     ratio.append(Ratio)                									      	#adding ratio to list
     ln_ratio.append(ln_Ratio)                      								#adding ratio to list
K=0


if n == 1:
	plot1 = [[]]																	#List for displaying ln_ratio vs time
	plot1[0].extend([ln_ratio[0],time[0]])
	for i in range(1, num+1):
		plot1.append([time[i],ln_ratio[i]])
          
	slope, intercept = np.polyfit(time, ln_ratio, 1)
	K=slope
	print "Rate constant: k =",round(K,2),"/min"


if n == 2:
	plot2 = [[]]																	#List for displaying ln_ratio vs time
	plot2[0].extend([ratio[0],time[0]])
	for i in range(1, num+1):
		plot2.append([time[i],ratio[i]])

	slope, intercept = np.polyfit(time, ratio, 1)
	K=slope/(c_zero-c_infi)
	print "Rate constant: k =",round(K,2),"ml/g/min"


R=(K*T1/(1+K*T1))*100	
r=(1-(1+K*T1)**(-N))*100
print "For a series of",N," cells, Recovery Rate:R=",round(r,3), "%"


