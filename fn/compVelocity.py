def comp_velocity(dp,pd,df,vis,g=9.8,Re):
    if Re<1:                 #condition for reynolds no <1
        v = float(g*dp**2*float((pd-df)/(18*vis)))
    elif Re>=1 and Re<=1000:     #condition for reynolds no >=1 but <=1000
        v = float(2*g*float(float(pd/df)-1)/27)**(0.7143)*(dp**(1.143))*(float(df/vis)**(0.4286))
    elif Re>1000 and Re<200000:           #condition for reynolds no >1000
        v = float((3*g*((pd/df)-1))**(0.5))*((dp)**(0.5))
    return v          # function returns the value of v calculatd for any one condition

print comp_velocity(dp,pd,df,vis,Re = R)


#Output is the velocity of the particle for the given input parameters")
