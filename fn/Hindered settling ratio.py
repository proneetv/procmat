#Theory filename: Partical Seperation Methods
#Theory file Authors: Deepak Sachan

#Code Authors Name: Simran Meena, Nirma Kumari
#Roll Numbers: 12722, 12452

    #Input parameters:
                #Pa=Density of first type of particle
                #Pb=Density of second type of particle
                #Pl=Density of liquid without solid
                #Ps=Density of the solids
                #Cw=Concentration of solids by weight in the slurry(%)
                #Cv=Concentration of solids by volume in the slurry(%)
               

import decimal


def Hindered_settling_ratio(Pa,Pb,Pl,Ps,Cw,Cv,m):  #Function for Calculation of hindered settling ratio

    if (Cv==0):                                    #Calculation of Specific Gravity of slurry(P)
        P = 100/((Cw/Ps)+((100-Cw)/Pl))            #If Cv is not given then calculating specific gravity of slurry(P) using Cw
    elif (Cv>0):                                   #If value of Cv is given then
        P=((Cv*Ps)+((100-Cv)*Pl))/100              #Calculation of specific gravity of slurry(P) uisng given value of Cv
    
    if(m==1):                                      #Condition for Turbulent regime
        h=((Pb-P)/(Pa-P))                          #Calculation of Hindered settling ratio using specific gravity of slurry(P)
    elif(m==0.5):                                  #condition for Stokes regime
        h=((Pb-P)/(Pa-P))**0.5                     #Calculation of Hindered settling ratio using specific gravity of slurry(P)
    return h

Pa=float(input("enter the density of particle 1 Pa (kg/m3): "))
Pb=float(input("enter the density of particle 2 Pb (kg/m3): "))
Pl=float(input("enter the density of liquid without solid Pl (kg/m3): "))
Ps=float(input("enter the density of the solids Ps (kg/m3): "))
ch=int(input("If you want to calculate specific gravity using the concentration of solids by weight (Cw), enter 1, else if you want to calculate using the concentration of solids by volume (Cv) enter 2: "))   #taking ch as a input for selecting Cw and Cv
if ch==1:
    Cv=0
    Cw=float(input("enter the concentration of solids by weight in the slurry(%)(Cw): "))
elif ch==2:
    Cw=0
    Cv=float(input("enter the concentration of solids by volume in the slurry(%)(Cv): "))
else:
    print"Invalid Input\nExit"
    sys.exit()
k=int(input("If stokes regime,enter 1, if turbulent regime enter 2: "))     #taking k as a input for selecting regime
if k==1:
    m=0.5
elif k==2:
    m=1
else:
    print"Invalid Input\nExit"
    sys.exit()
  
hindered_settling_ratio=Hindered_settling_ratio(Pa,Pb,Pl,Ps,Cw,Cv,m)

print 'Hindered settling ratio =',round(hindered_settling_ratio,2),


     #Output parameter:
     #h= Hindered settling ratio
     #eg:- density of particle 1(Pa)=1.7; density of particle 2(Pb) =2.65; fluid density(Pl)=1; solids density(Ps)=2.65; Cw=30; Cv=0; m=0.5
     #Ans:- 1.74
