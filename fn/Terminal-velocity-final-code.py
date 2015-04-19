def Velocityfunc(dp,pd,df,vis):
        dp=float(dp) #(raw_input("enter the particle diameter in mm "))     #taking the input for particle diameter
        #dp=(float(dp)/1000)
        pd= float(pd) #float(raw_input("enter the particle density"))    #taking the input for particle density

        df=float(df) #float(raw_input("enter the fluid density"))    #taking the input for fluid density

        vis= float(vis) #float(raw_input("enter the fluid viscosity"))
                                        #taking the input for viscosity
        g=10

        Re=500 #Reynolds no by default to do further calculations
        v=float(2*g*float(float(pd/df)-1)/27)**(0.7143)*(dp**(1.143))*(float(df/vis)**(0.4286))   #calculation for the reynolds no 1000=>Re>=1
        R=float(float(dp*df*v)/vis)
        g=10
        if R<1:
                 v=float(g*dp**2*float((pd-df)/(18*vis)))
        elif R>=1 and R<=1000:
                v=float(2*g*float(float(pd/df)-1)/27)**(0.7143)*(dp**(1.143))*(float(df/vis)**(0.4286))  
        elif R>1000 and R<200000:
                v=float((3*g*((pd/df)-1))**(0.5))*((dp)**(0.5))        #calculation for reynolds no>1000
        return v

