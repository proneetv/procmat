#Theory file name :kinetics for leaching of malasite ore

#Theory file author :Nirma Kumari

#Code author:Nirma Kumari

#Roll No:12452
           #input parameters
                   #input wtp is weight fraction of solids in slurry
                   #input C isNH4Cl concentration (Kmol m^-3)(C)
                   #input pd is paticle diameter(m) 
                   #input n is stirring speed(revolutions/sec)
import math



def Fraction_of_solid_diss(C,pd,n,T,s):   #function used for calculation raction of solid dissolved
    #s=solid_to_liquid_ratio(wtp)
    y=(10**(-5))*(C**(2.1))*(pd**(-1.96))*(s**(-0.64))*(n**(1.78))*(math.exp(-8500/T))
    x=1-((1-(y**0.5))**3)
    return x 

def time_taken_in_reaction(C,pd,n,T,s):    #function used for time taken for reaction
  
   Y=(10**(-5))*(C**(2.1))*(pd**(-1.96))*(s**(-0.64))*(n**(1.78))*(math.exp(-8500/T))
   fx=Fraction_of_solid_diss(C,pd,n,T,s)
   
   time=((1-(1-fx)**(1/3))**2)/Y
   return time


C=float(input("Enter  the NH4Cl concentration(Kmol m^-3): "))
s=float(input("solid_to_liquid_ratio(kg/kg): "))        
pd=float(input("Enter the particle Diameter(m): "))
n=float(input("Enter the stirring speed(rotaions/sec): "))
T=float(input("Enter the Reaction temperature(K): "))
x=Fraction_of_solid_diss(C,pd,n,T,s)
print("Reacted fraction of solid: ")
print(x)
print("Time taken in the reaction(sec)")
t=time_taken_in_reaction(C,pd,n,T,s)
print(str(t)[:4])
print("Kinetics of rection os reactin is given by :\n 1-(2*((1-x)**(1/3)))+((1-x)**(2/3))=(10**(-5))*(C**(2.1))*(pd**(-1.96))*(s**(-0.64))*(n**(1.78))*(math.exp(-8500/T))*t")
print("m :fraction of rected solid \n C:NH4Cl concentration(kmol/m^3) \n pd :particle diameter(m) \n s:% solid to % liquid ratio in slurry \n n :stirring speed(revolution/sec) \n t :reaction time")

      
left=1-(2*((1-x)**(1/3)))+((1-x)**(2/3))
l1=(int)(left*(10**5))
right=(10**(-5))*(C**(2.1))*(pd**(-1.96))*(s**(-0.64))*(n**(1.78))*(math.exp(-8500/T))*t
r1=(int)(right*(10**5))
if l1==r1:
    print("data given is follow above kinetics")
else:
    print("data given is not follow above kinetics")

#eg-    concentration of NH4cl(kmol/m^3)=1
#       solid to liquid ratio(kg/kg)    =0.01
#       particle diameter(meter)        =0.001
#       stirring spee(revolution/sec)   =1.67
#       Temperature of reaction(kelvin) =293
# Ans  
#     1.fraction of solid dissolve=2.85*exp(-5)
#     2.Time taken in reaction    = 1 sec          

        
        
	
