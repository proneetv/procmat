def solid_to_liquid_ratio(wtp):               #function used for solid to liquid ratio 
    stl=wtp/(100-wtp)
    return stl


def Fraction_of_solid_diss(C,pd,n,T,t,wtp):   #function used for calculation raction of solid dissolved
    s=solid_to_liquid_ratio(wtp)
    y=(10**(-5))*(C**(2.1))*(pd**(-1.96))*(s**(-0.64))*(n**(1.78))*(math.exp(-8500/T))*t
    x=1-(1-(y**(0.5)))**3
    return x 

def time_taken_in_reaction(C,pd,n,T,fx,wtp):    #function used for time taken for reaction
   s=solid_to_liquid_ratio(wtp)
   Y=(10**(-5))*(C**(2.1))*(pd**(-1.96))*(s**(-0.64))*(n**(1.78))*(math.exp(-8500/T))
   if Y==0:
       print("It will take infinite time to complete the reaction\n")
       sys.exit()
   time=((1-(1-fx)**(1/3))**2)/Y
   return time


    s=solid_to_liquid_ratio(wtp)
    x=Fraction_of_solid_diss(C,pd,n,T,t,wtp)
    
    print("Reacted fraction of solid: ",x)
    

    s=solid_to_liquid_ratio(wtp)
    t=time_taken_in_reaction(C,pd,n,T,fx,wtp)
    print("Reaction Time: ",t,"minutes")
   

#eg-  for calculating fraction of solid dissolve
#       concentration of NH4cl(kmol/m^3)(C)  =1
#       weight % solid in slurry(wtp)        =20
#       particle diameter(mm)(pd)            =0.001
#       stirring speed(revolution/sec)        =1.67
#       Temperature of reaction(kelvin)      =293
#       Reaction of time(mins)(t)            =2
# Ans   1.4421740712422526e-05

#eg-   for calculating raction of time
#    concentration of NH4cl(kmol/m^3)(C)  =2
#    weight % solid in slurry(wtp)        =30
#    particle diameter(mm)(pd)            =0.003
#    stirring speed(revolution/sec)        =1.67
#    Temperature of reaction(kelvin)      =300
#    fraction of solid dissolve           =0.01
# Ans   1395496.1385075487 

        
        
	
