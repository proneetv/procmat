#Theory file name :velocity of particle

#Theory file author :Deepak Sachan

#Code author:Deepak Kumar Yadav

#Roll No:12229
           #input parameters
                   #input no 1 particle diameter as dp
                   #input no 2 particle density
                   #input no 3 density of fluid
                   #input no 4 viscosity
                   
                   
def Velocityfunc(dp,pd,df,vis):
        dp=float(dp) #(raw_input("enter the particle diameter in mm "))     #taking the input for particle diameter
        #dp=(float(dp)/1000)
        pd= float(pd) #float(raw_input("enter the particle density"))    #taking the input for particle density

        df=float(df) #float(raw_input("enter the fluid density"))    #taking the input for fluid density

        vis= float(vis) #float(raw_input("enter the fluid viscosity"))
                                        #taking the input for viscosity
        g=10

        Re=500 #Reynolds no by default to do further calculations
        
        #if Re<1:
        #v=float(g*dp**2*float((pd-df)/(18*vis)))        #condition for reynolds no <1
	
        #elif Re>=1 and Re<=1000:
        v=float(2*g*float(float(pd/df)-1)/27)**(0.7143)*(dp**(1.143))*(float(df/vis)**(0.4286))   #calculation for the reynolds no 1000=>Re>=1
	
        #elif Re>1000 and Re<200000:
        #v=float((3*g*((pd/df)-1))**(0.5))*((dp)**(0.5))        #calculation for reynolds no>1000
           #print("the output is the velocity of the particle ")

        #print(v)
        R=float(float(dp*df*v)/vis)
        #return R
        #print(R)

        #R=float(raw_input("enter the reynolds number which is calculated above"))
        #def Velocityfunc(dp,pd,df,vis):
        g=10
        if R<1:
                 v=float(g*dp**2*float((pd-df)/(18*vis)))        #condition for reynolds no <1
	
        elif R>=1 and R<=1000:
                v=float(2*g*float(float(pd/df)-1)/27)**(0.7143)*(dp**(1.143))*(float(df/vis)**(0.4286))   #calculation for the reynolds no 1000=>Re>=1
	
        elif R>1000 and R<200000:
                v=float((3*g*((pd/df)-1))**(0.5))*((dp)**(0.5))        #calculation for reynolds no>1000
        return v 
        print("the output is the velocity of the particle ")
        print(v)



	
