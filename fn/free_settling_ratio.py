#Theory filename: Partical Seperation Methods
#Theory file Authors: Deepak Sachan

#Code Authors Name: Simran Meena, Nirma Kumari
#Roll Numbers:12722, 12452

import sys
import decimal

    #Input parameters:
               #Pa=Density of first tye particle (float)
               #Pb=Density of second type particle (float)
               #Pf=Density of fluid (float)
    

def free_settling_ratio(Pa,Pb,Pf,m):   #Function for Calculation of free settling ratio

 
    if   m==1:                      #Condition for Free settling ratio to be in turbulent regime
        d =((Pb-Pf)/(Pa-Pf))        #d is the Free settling ratio for turbulent regime
    elif m==0.5:                    #Condition for Free settling ratio to be in stokes regime
        d =((Pb-Pf)/(Pa-Pf))**0.5   #d is the Free settling ratio for stokes region

    return d

Pa=float(input("Enter density of first particle Pa (kg/m3): "))
Pb=float(input("Enter density of second particle Pb (kg/m3): "))
Pf=float(input("Enter Density of Fluid Pf (kg/m3): "))
k=int(input("If stokes regime,enter 1, if turbulent regime enter 2: "))   #taking k as input for selecting regime
if k==1:              
    m=0.5
elif k==2:
    m=1
else:
    print"Invalid Input\nExit"
    sys.exit()

Free_settling_Ratio=free_settling_ratio(Pa,Pb,Pf,m)      #storing value of free settling ratio
print 'Free settling Ratio =',round(Free_settling_Ratio,3),

        

    #Output parameter:
    #d= Free settling ratio
    #eg:- Paticle_1 density(Pa)=7.5; particle_2 density(Pb)=2.65; fluid density(Pf)=1; exponent(m)=0.5
    #Ans=0.504
    


    
