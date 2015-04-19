#theory file name : Solvent Extraction
#theory file author : 
#code author name : Alkesh Kumar Sinha
#roll no :12078

from __future__ import division

def solvent_extraction(L,V,x0,y1):
    
    #L=Volume flow rate in the aqueous phase in m^3/sec   
    #V=Volume flow rate in the organic phase in m^3/sec
    #x0=Initial Concentration(Cu) in g/L in the aqueous phase   
    #y1=Initial Concentration(Cu) in g/L in the organic phase
    #A=Amount of Copper extracted
    #x3=Final concentration(Cu) in g/L in the aqueous phase
    #y4=Final concentration(Cu) in g/L in the organic phase

    x1=(y1/2.25)**4      #equilibrium line equation for Y1  to get X1
    y2=x1+y1-x0          #mass balance equation for Mixture Settler 1 to get Y2
    x2=(y2/2.25)**4      #equilibrium line equation for Y2  to get X2
    y3=x2+y2-x1          #mass balance equation for Mixture Settler 2 to get Y3
    x3=(y3/2.25)**4      #equilibrium line equation for Y3  to get X3
    y4=x3+y3-x2          #mass balance equation for Mixture Settler 3 to get Y4

    A=((x0-x3)/x0)*100   

    return x3,y4

print solvent_extraction(100,100,0.002,0.004)                                         #answer (6.242950777494632e-13, 0.0020000000006242954) i.e (x3,y4)
print solvent_extraction(50,50,0.005,0.015)                                           #answer(3.901844840038389e-10, 0.010000000390184482) i.e (x3,y4)
print solvent_extraction(75,75,0.008,0.016)                                           #answer(1.5981955247547285e-10, 0.008000000159819554) i.e (x3,y4)



    
