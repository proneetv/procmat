#Theory File Name : Hydrocyclone
#Theory File Authors : Aditya, Anish and Archit

#Code Author Name : Jyoti Prakash
#Roll No : 11342


import math

def hydrocyclone(phi, S, p, v, Dc, Cost,mass_ratained, n ):

    #phi = volume fraction of solids in slurry (float)
    #S = specific gravity of solid (float)
    #p = specific gravity of fluid (float)
    #v = vinlet velocity (float)
    #Dc = cyclone diameter (float)
    #Cost = cost of per unit electricity (float)
    #mass_ratained =  array of mass retained in different sieve range
    #n =  no. of rows in size distribution table (int)
    total_weight=0
    for x in xrange(0,10):
        total_weight=total_weight+mass_ratained[x]
    
    wt=[]
    avgsize=[0.055,0.55,2,4.5,8,12.5,20,37.5,62.5,87.5]

    for i in xrange(0,10):
        temp=((100*mass_ratained[i])/total_weight)
        wt.append(temp)


    Di = 0.5 * Dc
    Do = 0.5 * Dc
    Du = 0.25 * Dc
    h = 2 * Dc
    Di1=Di*0.0254
    Q1 =  v  * ((3.14 * Di1 * Di1)/4)
    Q=(Q1*pow(3.28084,3))*60
    print("Flow rate(feet cube per minute)= %0.2f" % Q)
#calculating F50
    F50_1 = 0
    for x in range(0, n):
        F50_1  = F50_1 + (avgsize[x]*wt[x])


    F50 = F50_1/100  
        
#calculating X50
    Dc1 = Dc ** 0.46
    Di1 = Di ** 0.6
    Do1 = Do ** 1.21
    Du1 = Du ** 0.71
    h1 = h ** 0.38
    Q1 = Q ** 0.45
    F501 = F50 ** 0.052
    SP = abs(S-p)
    SP1 = SP ** 0.5
    expo = (0.08*phi)/F501
    expo1 = math.exp(expo)

    X50 = (35 * Dc1 * Do1 * expo1) / (Du1 * h1 * Q1 * SP1)

    print("X50(micrometer)= %.2f" % X50)
#PD=pressure Difference
    PD = 0.5 * p * v * v
#W=Total Power Consumption 
    W = Q * PD
    totalCost = W * Cost

    return totalCost




phi=float(raw_input('Input Volume Fraction of solid : '))
S=float(raw_input('Input Specific Gravity of solid : '))
p=float(raw_input('Input Specific Gravity of fluid : '))
v=float(raw_input('Input Inlet Velocity(m/s): '))
Dc=float(raw_input('Input cyclone diameter(inches): '))
Cost=float(raw_input('Input cost per unit electricity(Rupees):'))


mass_ratained=[]

mass_ratained.append(float(raw_input("Input Mass retained in size range 0.01-0.1 micrometers(grams): ")))
mass_ratained.append(float(raw_input("Input Mass retained in size range 0.1-1 micrometers(grams): ")))
mass_ratained.append(float(raw_input("Input Mass retained in size range 1-3 micrometers(grams): ")))
mass_ratained.append(float(raw_input("Input Mass retained in size range 3-6 micrometers(grams): ")))
mass_ratained.append(float(raw_input("Input Mass retained in size range 6-10 micrometers(grams): ")))
mass_ratained.append(float(raw_input("Input Mass retained in size range 10-15 micrometers(grams): ")))
mass_ratained.append(float(raw_input("Input Mass retained in size range 15-25 micrometers(grams): ")))
mass_ratained.append(float(raw_input("Input Mass retained in size range 25-50 micrometers(grams): ")))
mass_ratained.append(float(raw_input("Input Mass retained in size range 50-75 micrometers(grams): ")))
mass_ratained.append(float(raw_input("Input Mass retained in size range 75-100 micrometers(grams): ")))



result=hydrocyclone(phi, S, p, v, Dc, Cost,mass_ratained,10)

print("Total Cost(Rupees)= %0.2f" % result)
