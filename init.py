from datetime import timedelta
from flask import make_response, request, current_app, Flask, jsonify, json, request
from functools import update_wrapper
import math
import time

def hydrocyclone(phi, S, p, v, Dc, Cost,mass_ratained, n ):
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
    s = "Flow rate(feet cube per minute): " + str(round(Q,2))
    F50_1 = 0
    for x in range(0, n):
        F50_1  = F50_1 + (avgsize[x]*wt[x])
    F50 = F50_1/100        
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

    s = s + "<BR>X50(micrometer): " + str(X50)
    PD = 0.5 * p * v * v
    W = Q * PD
    totalCost = W * Cost

    s = s + "<BR>TotalCost: Rs." + totalCost
    return s


def triboelectric(E,qa,Ma,x):
    g = 9.8
    y=3.2     
    tsquare = (2*y)/g
    t = tsquare**(0.5)
    x = (qa*E*tsquare)/(2*Ma) 
    return "X = " + str(round(x,2)) + "m, Time = " + str(round(t,2)) + "sec"



def elldiag(x1,y1,x2,y2):
    x1 = round(x1, 2)
    y1 = round(y1, 2)
    x2 = round(x2, 2)
    y2 = round(y2, 2)
    list1 = [x1, y1]
    list2 = [x2, y2]
    if list1[1] == list2[1]:
        return 'There exist no temp. where gibbs free energy of both the reactions in same'
    else:
        temp = float(list1[0]-list2[0])/float(list1[1]-list2[1])
        temp = round(temp, 2)
        return "Equilibrium Temperature: =" + str(round(temp,2)) + "K"



def flash_smelt(iCu,iSiO2,iFe,iS,iAl2O3,iCaO,fCu,fSiO2,fFe,fS,fAl2O3,fCaO,fO2):
    TW = (iSiO2*1000)/fSiO2

    CaO = (fCaO * (TW / 100))
    Al2O3 = (fAl2O3 * (TW / 100))
    SiO2 = (fSiO2 * (TW / 100))

    Cu2S = (fCu*TW*159)/12700

    s = (fS*TW)/100
    s2 = (Cu2S*32)/159
    O2 = ((fO2*TW)/100)
    FeS = ((s-s2)*88)/32

    Fe1 = (FeS*56)/88
    FeR = (fFe*TW/100) - Fe1
    Fe3O4 = ((FeR/0.7)-(O2/0.3))/0.0957
    Fe2O3 = (O2-(0.28*Fe3O4))/0.3
    
    s = "Total wieght of roasted product :" + str(TW) + "Kg<BR>"
    s = s + "weight of CaO in roasted product :" + str(CaO) + "Kg"
    s = s + "<BR>weight of Al2O3 in roasted product :" + str(Al2O3) + "Kg"
    s = s + "<BR>weight of SiO2 in roasted product :" + str(SiO2) + "Kg"
    s = s + "<BR>weight of Cu2S in roasted product :" + str(Cu2S),"Kg"
    s = s + "<BR>weight of FeS in roasted product :" + str(FeS) + "Kg"
    s = s + "<BR>weight of Fe3O4 in roasted product :" + str(Fe3O4) + "Kg"
    s = s + "<BR>weight of Fe2O3 in roasted product :" + str(Fe2O3) + "Kg"
    return s

def imperialsmelting(ZNOp, PBOp, FEOp, SIOp, sc, ZNp, CO2CO):

    ZNOw = (sc * ZNOp)/100
    PBOw = (sc * PBOp)/100
    FEOw = (sc * FEOp)/100
    SIOw = (sc * SIOp)/100

    ZNOm = ZNOw/81
    PBOm = PBOw/223
    FEOm = FEOw/72
    SIOm = SIOw/60
    
    Y = (ZNOm * 100) / ZNp

    ZNf = ZNOm
    COf = 2*(ZNOm + PBOm)
    CO2f = CO2CO * COf
    N2f = 1.5 * (ZNOm + PBOm) * 3.76
    
    O2f = (Y - (ZNf + COf + CO2f + N2f)) * 0.21
    
    N2f1 = N2f + (Y - (ZNf + COf + CO2f + N2f) - O2f)
    
    air_amount = N2f1/0.79
    liq_lead = PBOm
    slagFEO = FEOm
    slagSIO2 = SIOm
    coke_amount = COf + CO2f
    coke_amountf = coke_amount * 12
    
    HZNOo = 83500 #standard enthalpy of ZnO
    HPBOo = 52500 #standard enthalpy of PbO
    HZNO = 9500 #enthalpy of ZnO(1100-298)
    HPBO = 10800 #enthalpy of PbO (1100-298)
    HFEO = 10280 #enthalpy of FeO (1100-298)
    HSIO = 19940 #enthalpy of SiO2 (1100-298)
    HZN = 36160 #enthalpy of Zn (v) (1300-298)
    HCO2 = 12010 #enthalpy of CO2 (1300-298)
    HCO = 7460 #enthalpy of CO (1300-298)
    HN2 = 7500 #enthalpy of N2 (1300-298)
    HO2 = 7873 #enthalpy of O2 (1300-298)
    HPB = 10110 #enthalpy of Pb (1600-298)
    HFEOr = 11990 #enthalpy of FeO (1600-298)
    HSIO2r = 21100 #enthalpy of SiO2 (1600-298)
    slag_formation = 30602 #enthalpy of slag formation
    
    heat_reaction = (HZNOo * ZNOm)+ (HPBOo * PBOm)
    heat_reactants = (HZNO * ZNOm) + (HPBO * PBOm) + (HFEO * FEOm) + (HSIO * SIOm)
    heat_gases = (HZN * ZNf) + (HCO2 * CO2f) + (HCO * COf) + (HN2 * N2f1) + (HO2 * O2f)
    heat_slag = (HPB * liq_lead) + (HFEOr * slagFEO) + (HSIO2r * slagSIO2)
    heat_input = heat_reaction + heat_reactants + slag_formation
    heat_output = heat_gases + heat_slag
    heat_deficit = heat_output - heat_input
    Cp = 7.5
    Preheated_T = heat_deficit / (Y * Cp)
    
    
    s = s + "moles of zinc in vapour: " + str(ZNf)
    s = s + "<BR>moles of CO2 " + str(COf)
    s = s + "<BR>moles of CO " + str(CO2f)
    s = s + "<BR>moles of O2 " + str(O2f)
    s = s + "<BR>moles of N2 " + str(N2f1)
    s = s + "<BR>amount of air " + str(air_amount)
    s = s + "<BR>moles of lead " + str(liq_lead)
    s = s + "<BR>moles of FeO " + str(slagFEO)
    s = s + "<BR>moles of FeO " + str(slagSIO2)
    s = s + "<BR>amount of coke " + str(coke_amountf)
    s = s + "<BR>Preaheated temperature " + str(Preheated_T) +"K"
    return s


def Decomposition_Temp(x1,y1,x2,y2):
    m=(y2-y1)/(x2-x1)
    c=y1-(m*x1)
    DT=c/m
    return DT

def dryk(m,Xi,Xc,Rc,Xf,Rf):
    Rc = Rc * (10**(-3))
    Rf = Rf * (10**(-3))
    y1 = Xi / (100 - Xi)
    y3 = Xf / (100 - Xf)
    tc = (m * ( y1 - Xc ) ) / (Rc)
    tf = (m * (( Xc- y3)/ (Rc - Rf))) * ((math.log(Rc/Rf)))
    tt = tc + tf

    s = "Constant falling rate time: " + tc + "sec" + "<BR>First falling rate time:" + tf + "sec<BR>"
    s = s + "Total time: " + tt + "sec"

def drying_time(pd,dp,Ms,e,Tw,Tgi,Xi,Xf,Vsc):
    da=1.1
    k=0.03
    cp=1000.0
    u=0.002
    L=2440000.0
    v1=Xi*0.01
    v2=Xf*0.01
    Xi=v1
    Xf=v2
    E=e*0.01
    e=E
    z=dp/1000.0
    dp=z
    Ss=(6.0)/(pd*dp)
    H=(Ms/(pd*(1-e)))
    time.sleep(2)
    am= (da*1.0*Vsc)
    time.sleep(2)
    mm=(Ms*(Xi-Xf))
    time.sleep(2)
    s=(1.17*(pow(k,0.67))*(pow(da,0.58))*(pow(Vsc,0.58))*(pow(cp,0.33)))
    m=(pow(dp,0.42))*(pow(u,0.25))
    h=(s)/m
    time.sleep(2)
    exp_powfact=-6.0*h*H*(1-e)/(am*cp*dp)
    evr=exp(exp_powfact)
    tgf= ((Tgi-Tw)*evr )+Tw
    time1 =(mm*L)/(am*cp*(Tgi-tgf))
    time1=time1/60.0
    time.sleep(2)
    hc = raw_input()
    s = 'specific surface area '  + str(round(Ss,2)) + 'm2/kg' 
    s = s +'height ' +  str(round(H,2)) + ' m'
    s = s + 'Mass flow rate of ' + str(round(am,2)) + 'kg/m2-s'
    s = s + 'Moisture to be removed ' + str(round(mm,2)) + 'kg/m2'
    s = s + 'heat transfer coefficent ' + str(round(h,2)) + 'W/m2-k'
    s = s + 'Final air outlet Temp ' + str(round(tgf,2)) + 'kelvin'
    s = s + 'Total time for drying '  + str(round(time1,2)) + 'Min.'
    return s

def rec1(I,T):
    Q = I*T*60*60             #Calculating the total charge being passed in the cell
    dM = 63.5*Q/(2*96500)     #Calculating mass of copper deposited on the cathode
    return dM

def rec2(n,Ec,Ea):
    Ecell = Ec+Ea                                                                             #Calculating the Cell Potential
    s = "The cell potential of the reaction is Ecell =" + str(round(Ecell,2)) + 'Volts'
    dG = -n*96484.56*Ecell                                                                           #Calculating the Free energy of the reaction 
    s = s + "<BR>The free energy of the reaction is dG = " + str(round(dG,2)) + "J"                            #Printing the free energy in joules
    if dG<0:
        s = s + '<BR>The zinc ions will plate out onto the copper at standard conditions ince the reaction is spontaneous(dG<0) ' #Printing the statement for the reaction to be spontaneous. 
    elif dG>0:
        s = s + '<BR>The zinc ions will not plate out onto the copper at standard conditions since the reaction is not spontaneous(dG>0)' #Printing the statement for the reaction to not to be spontaneous.
    return s

def rec3(W,V,T):
    n = (W*1000)/70                                                             #Calculating the moles of chlorine produced, by converting mass from kg to grams and using density of chlorine 70 g mol-1
    F = n*2                                                                     #Calculating Faradays of charge
    s = 'The Faradays of charge is ' + str(round(F,2)) + 'F'  
    Q = 96500*F                                                                 #Calculating charge in coulombs
    s = s+ '<BR>The Total charge in the cell is ' + str(round(Q,2)) + 'C'
    T = 3600*24                                                                 #Converting time (Duration of electrolysis) from hours to seconds
    s = s + '<BR>The Time for which the charge travels is ' + str(round(T,2)) + 'seconds'
    I = Q/T                                                                     #Calculating current in amperes
    s = s + '<BR>The Total current in the cell is ' + str(round(I,2)) + 'Amperes'
    P = V*I                                                                     #Calculating the total power generated by the cell in joules
    s = s + '<BR>The Total power generated by the cell is ' +str(round(P,2)) + 'Watt'
    return s

def rec4(N,Na,Nc,A,L,i,R,n,k):
    if Na==Nc:             
        Ncell = 2*Nc-1     
    elif Na==Nc+1:
        Ncell = 2*Nc       

    I = i*A                
    Rth = I*0.0292         
    ni = R/Rth             

    Re = L/(k*A)           
    V = 2+n+I*Re           
    nv = 2/V               
    np = ni*nv             
    P = V*I*Ncell*N        

    s = '<BR>The Current Efficiency is ' + str(round(ni,2))
    s = s + '<BR>The Voltage across each cell is ' + str(round(V,2)) + 'V'
    s = s + '<BR>The Voltage efficiency is ' + str(round(nv,2))
    s = s + '<BR>The Power efficiency is ' + str(round(np,2))
    s = s + '<BR>The Power consumed across all cells is ' + str(round(P,2)) + 'Watt'
    return s


def free_settling_ratio(Pa,Pb,Pf,m):
    if   m==1:
        d =((Pb-Pf)/(Pa-Pf))
    elif m==0.5:
        d =((Pb-Pf)/(Pa-Pf))**0.5
    return d

def solvent_extraction(L,V,x0,y1):
    x1=(y1/2.25)**4      
    y2=x1+y1-x0          
    x2=(y2/2.25)**4      
    y3=x2+y2-x1          
    x3=(y3/2.25)**4      
    y4=x3+y3-x2          

    A=((x0-x3)/x0)*100   

    return x3,y4

def solid_to_liquid_ratio(wtp):
    stl=wtp/(100-wtp)
    return stl


def Fraction_of_solid_diss(C,pd,n,T,t,wtp):
    s=solid_to_liquid_ratio(wtp)
    y=(10**(-5))*(C**(2.1))*(pd**(-1.96))*(s**(-0.64))*(n**(1.78))*(math.exp(-8500/T))*t
    x=1-(1-(y**(0.5)))**3
    return x 

def time_taken_in_reaction(C,pd,n,T,fx,wtp):
   s=solid_to_liquid_ratio(wtp)
   Y=(10**(-5))*(C**(2.1))*(pd**(-1.96))*(s**(-0.64))*(n**(1.78))*(math.exp(-8500/T))
   time=((1-(1-fx)**(1/3))**2)/Y
   return time

def cementation(Eanode, Ecathode, n, T, Fe):
    EOCell = Ecathode - Eanode
    
    lnK = (EOCell * n * 96500)/ (8.314 * T)
    K = 2.718281828 ** lnK
    
    FeConc = Fe/55.845;
    eqconc =  FeConc/K
    
    outputList = []
    outputList.append(EOCell)
    outputList.append(eqconc)
    
    return outputList
    


def crusher(F,D,T,d,i,j):
    y = [0,1,2,3,4,5,6,7,8,9,10,11,12]    #y = []
    C = T/d
    if F <= 255 and C >= 6 and C <= 15: 
        y[0] = 3.76898*(C**1.009449)      #output size   ,    y = y + [  expr ]
    if F <= 355 and C >= 13 and C <= 30:
        y[1] = 1.805324*(C**1.095716)   #output size
    if F <= 455 and C >= 27 and C <= 80:
        y[2] = 2.01705*(C**0.890806)   #output size
    if F <= 610 and C >= 40 and C <= 110:
        y[3] = 1.728558*(C**0.883568)   #output size
    if F <= 760 and C >= 75 and C <= 170: 
        y[4] = 0.385634*(C**1.161164)
    if F <= 915 and C >= 110 and C <= 210: 
        y[5] = 0.02041*(C**1.698989)
    if F <= 1065 and C >= 160 and C <= 280: 
        y[6] = 0.057715*(C**1.437366)
    if F <= 1220 and C >= 200 and C <= 350: 
        y[7] =  0.229521*(C**1.146955)
    if F <= 1420 and C >= 300 and C <= 450: 
        y[8] = 1.323601*(C**0.817227)
    if F <= 1070 and C >= 320 and C <= 600: 
        y[9] = 1.105156*(C**0.812629)
    if F <= 1220 and C >= 500 and C <= 775: 
        y[10] = 0.085761*(C**1.16559)
    if F <= 1370 and C >= 620 and C <= 1000: 
        y[11] = 0.085761*(C**1.16559)
    if F <= 1520 and C >= 1000 and C <= 1080: 
        y[12] = 8.53E-11*(C**4.104063)

    R = y[i]/D
    K = [0,1,2,3,4,5,6]
    if R > 1:                                #  :  after every if conditional
        F = R*D
        if F <= 95 and D >= 10 and D <= 31 :
            K[0] = (0.74186*D)**0.971018   # remove all :  they dont come in normal statements
        if F <= 150 and D >= 13 and D <= 37 :
            K[1] = (2.45561*D)**0.818061
        if F <= 210 and D >= 18 and D <= 46 :
            K[2] = (3.03735*D)**0.921907
        if F <= 250 and D >= 18 and D <= 48 :
            K[3] = (2.30775*D)**1.049744
        if F <= 280 and D >= 25 and D <= 59 :
            K[4] = (7.6403*D)**1.049744
        if F <= 380 and D >= 30 and D <= 60 :  
            K[5] = (17.5701*D)**1.049744
        if F <= 510 and D >= 38 and D <= 60 :
            K[6] = (9.86329*D)**1.082183    

    m = C/K[j]
    return "<BR>Number of cone crusher required : " + str(int(math.ceil(m)))

def sedimentationClassifiers(w,dp,R1,Pf,Pp,uf):
    Q = (((w * 1000)/(2.0*Pf)) + ((w*1000)/(2.0*Pp)))/3600
    Voo = (9.8 * dp * dp * 0.000001*0.000001 *(Pp-Pf))/(18*uf)
    R_1 = (Q/(2*3.14*Voo)) + (R1*R1*0.01*0.01)
    R = math.sqrt(R_1)
    D = 2*R
    T1 = ((2 * 3.14 *1)*((R*R) - (R1*R1*0.01*0.01)))/Q
    H = T1 * Voo
    outputList = []
    outputList.append( round(D,2) )
    outputList.append( round(H,2) )
    return outputList

def Velocityfunc(dp,pd,df,vis):
    dp=float(dp)
    pd= float(pd)
    df=float(df)
    vis= float(vis)
    g=10

    Re=500
    v=float(2*g*float(float(pd/df)-1)/27)**(0.7143)*(dp**(1.143))*(float(df/vis)**(0.4286))   #calculation for the reynolds no 1000=>Re>=1
    R=float(float(dp*df*v)/vis)
    g=10
    if R<1:
        v=float(g*dp**2*float((pd-df)/(18*vis)))
    elif R>=1 and R<=1000:
        v=float(2*g*float(float(pd/df)-1)/27)**(0.7143)*(dp**(1.143))*(float(df/vis)**(0.4286))  
    elif R>1000 and R<200000:
        v=float((3*g*((pd/df)-1))**(0.5))*((dp)**(0.5))
    return v

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


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


app = Flask(__name__)

# MINERAL PROCESSING -- ROUTE fns

@app.route('/sieve', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_sieve():
    feedValue = float(request.form["feedValue"])
    discharge = float(request.form["discharge"])
    throughput = float(request.form["throughput"])
    bulkden = float(request.form["bulkden"])
    serID = int(request.form["serID"])
    serNo = int(request.form["serNo"])

    a = crusher(feedValue,discharge,throughput,bulkden,serID,serNo)
    print a
    return a

# @app.route('/hydrolic', methods = ['POST'])
# @crossdomain(origin='*', headers='Content-Type')
# def api_hydrolic():
#     dia1 = float(request.form["dia1"])
#     dia2 = float(request.form["dia2"])
#     dia3 = float(request.form["dia3"])
#     dia4 = float(request.form["dia4"])
#     dia5 = float(request.form["dia5"])
#     denp = float(request.form["denp"])
#     denf = float(request.form["denf"])
#     visc = float(request.form["visc"])

#     a = crusher(feedValue,discharge,throughput,bulkden,serID,serNo)
#     print a
#     return a



@app.route('/sedim', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_sedim():
    rate = float(request.form["rate"])
    sepSize = float(request.form["sepSize"])
    inrad = float(request.form["inrad"])
    DenFluid = float(request.form["DenFluid"])
    DenSolid = float(request.form["DenSolid"])
    Viscosity = float(request.form["Viscosity"])

    a = sedimentationClassifiers(rate,sepSize,inrad,DenFluid,DenSolid,Viscosity)
    print a
    return "Depth: " + str(a[0]) + "m " + "Height: " + str(a[1]) + "m"


@app.route('/terminal', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_terminal():
    Dia = float(request.form["Dia"])
    Denpart = float(request.form["Denpart"])
    Denflu = float(request.form["Denflu"])
    visc = float(request.form["visc"])

    a = Velocityfunc(Dia,Denpart,Denflu,visc)
    print 'ans: ',a
    return "Velocity: " + str(round(a,2)) + "m/sec"


@app.route('/fsr', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_fsr():
    den1 = float(request.form["den1"])
    den2 = float(request.form["den2"])
    denfluid = float(request.form["denfluid"])
    flag = float(request.form["flag"])
    if flag==1:              
        m=0.5
    else:
        m=1
    a = free_settling_ratio(den1,den2,denfluid,m)
    print 'ans: ',a
    return "Free Settling Ratio: " + str(round(a,3))


@app.route('/tribo', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_tribo():
    ElectricField = float(request.form["ElectricField"])
    SpecificCharge = float(request.form["SpecificCharge"])
    MinimumSeparation = float(request.form["MinimumSeparation"])
    Mass = float(request.form["Mass"])
    x = triboelectric(ElectricField,SpecificCharge,Mass,MinimumSeparation)
    return x

@app.route('/hsr', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_hsr():
    Density1 = float(request.form["Density1"])
    Density2 = float(request.form["Density2"])
    DensitySlurry = float(request.form["DensitySlurry"])
    DensityLiq = float(request.form["DensityLiq"])
    Regime = float(request.form["Regime"])
    ConcWt = float(request.form["ConcWt"])
    ConcVol = float(request.form["ConcVol"])

    # If stokes regime,enter 1, if turbulent regime enter 2
    if Regime==1:
        m=0.5
    else:
        m=1

    a=Hindered_settling_ratio(Density1,Density2,DensitySlurry,DensityLiq,ConcWt,ConcVol,m)
    print 'ans: ',a
    return "Hindered Settling Ratio: " + str(round(a,3))

@app.route('/hydrocyc', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_hydrocyc():
    VolFrac = float(request.form["VolFrac"])
    SpecSol = float(request.form["SpecSol"])
    SpecFl = float(request.form["SpecFl"])
    vel = float(request.form["vel"])
    cycDia = float(request.form["cycDia"])
    mass0 = float(request.form["mass0"])
    mass1 = float(request.form["mass1"])
    mass2 = float(request.form["mass2"])
    mass3 = float(request.form["mass3"])
    mass4 = float(request.form["mass4"])
    mass5 = float(request.form["mass5"])
    mass6 = float(request.form["mass6"])
    mass7 = float(request.form["mass7"])
    mass8 = float(request.form["mass8"])
    mass9 = float(request.form["mass9"])
    cost = float(request.form["cost"])
    mass_ratained = [mass0,mass1,mass2,mass3,mass4,mass5,mass6,mass7,mass8,mass9]
    result=hydrocyclone(VolFrac, SpecSol, SpecFl, vel, cycDia, cost,mass_ratained,10)
    return x

# HYDROMETALLURGY -- ROUTE fns

@app.route('/solext', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_solext():
    Qaq = float(request.form["Qaq"])
    Qorg = float(request.form["Qorg"])
    CuAq = float(request.form["CuAq"])
    CuOrg = float(request.form["CuOrg"])
    a,b = solvent_extraction(Qaq,Qorg,CuAq,CuOrg)
    return "Solvent Extraction: " + str(a) + " & " + str(b)

@app.route('/cement', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_cement():
    Ered = float(request.form["Ered"])
    Eoxd = float(request.form["Eoxd"])
    ne = int(request.form["ne"])
    Temp = int(request.form["Temp"])
    Fe = float(request.form["Fe"])
    a = cementation(Ered,Eoxd,ne,Temp,Fe)
    return "E-O-Cell: " + str(a[0]) + "E-Conc: " + str(a[1])

@app.route('/leachFOS', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_fos():
    WtSolid = float(request.form["WtSolid"])
    NH4Cl = float(request.form["NH4Cl"])
    Dia = float(request.form["Dia"])
    StirSpeed = float(request.form["StirSpeed"])
    Temp = float(request.form["Temp"])
    time = float(request.form["time"])
    s=solid_to_liquid_ratio(WtSolid)
    x=Fraction_of_solid_diss(NH4Cl,Dia,StirSpeed,Temp,time,WtSolid)
    return "Fraction of Solid Dissolve: " + str(round(x,4))


@app.route('/leachRT', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_rt():
    WtSolid = float(request.form["WtSolid"])
    NH4Cl = float(request.form["NH4Cl"])
    Dia = float(request.form["Dia"])
    StirSpeed = float(request.form["StirSpeed"])
    Temp = float(request.form["Temp"])
    frac = float(request.form["frac"])
    s=solid_to_liquid_ratio(WtSolid)
    x=time_taken_in_reaction(NH4Cl,Dia,StirSpeed,Temp,frac,WtSolid)
    return "Fraction of Solid Dissolve: " + str(round(x,4)) + " sec"

@app.route('/rec1', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_rec1():
    I = float(request.form["I"])
    time = float(request.form["time"])
    x = rec1(I,time)
    return "Change in mass of the Copper cathode and that of anode is dM = " + str(round(x,2)) + " grams"

@app.route('/rec2', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_rec2():
    moles = float(request.form["moles"])
    Ered = float(request.form["Ered"])
    Eoxd = float(request.form["Eoxd"])
    x = rec2(moles,Ered,Eoxd)
    return x

@app.route('/rec3', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_rec3():
    WtCl = float(request.form["WtCl"])
    Vcell = float(request.form["Vcell"])
    time = float(request.form["time"])
    x = rec3(WtCl,Vcell,time)
    return x

@app.route('/rec4', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_rec4():
    NoTank = float(request.form["NoTank"])
    NoAnode = float(request.form["NoAnode"])
    NoCathode = float(request.form["NoCathode"])
    Area = float(request.form["Area"])
    ACgap = float(request.form["ACgap"])
    CurDen = float(request.form["CurDen"])
    ZnCatDep = float(request.form["ZnCatDep"])
    OverPot = float(request.form["OverPot"])
    ElecCon = float(request.form["ElecCon"])
    x = rec4(NoTank, NoAnode, NoCathode, Area, ACgap, CurDen, ZnCatDep, OverPot, ElecCon)
    return x

# PYROMETALLURGY -- ROUTE fns

@app.route('/dry', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_dry():
    DenPart = float(request.form["DenPart"])
    Dia = float(request.form["Dia"])
    mass = float(request.form["mass"])
    poro = float(request.form["poro"])
    Twet = float(request.form["Twet"])
    Tg = float(request.form["Tg"])
    moisin = float(request.form["moisin"])
    moisfin = float(request.form["moisfin"])
    supvel = float(request.form["supvel"])
    thercond = float(request.form["thercond"])
    visc = float(request.form["visc"])
    x = drying_time(DenPart,Dia,mass,poro,Twet,Tg,moisin,moisfin,supvel,thercond,visc)
    return x


@app.route('/dryk', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_dryk():
    massdry = float(request.form["massdry"])
    Intmois = float(request.form["Intmois"])
    moistcd = float(request.form["moistcd"])
    dryratecp = float(request.form["dryratecp"])
    finmois = float(request.form["finmois"])
    dryratefin = float(request.form["dryratefin"])
    
    x = dryk(massdry,Intmois,moistcd,dryratecp,finmois,dryratefin)
    return x

@app.route('/calc', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_calc():
    x1 = float(request.form["x1"])
    y1 = float(request.form["y1"])
    x2 = float(request.form["x2"])
    y2 = float(request.form["y2"])
    
    x = Decomposition_Temp(x1,y1,x2,y2)
    return "Decomposition Temperature: " + str(round(x,2)) + "K"

@app.route('/imperial', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_imperial():
    Zn = float(request.form["Zn"])
    FeO = float(request.form["FeO"])
    PbO = float(request.form["PbO"])
    SiO2 = float(request.form["SiO2"])
    finmois = float(request.form["finmois"])
    Zngas = float(request.form["Zngas"])
    ratio = float(request.form["ratio"])
    x = imperialsmelting(Zn,FeO,PbO,SiO2,finmois,Zngas,ratio)
    return x

@app.route('/flash', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_flash():
    CuBefore = float(request.form["CuBefore"])
    SiO2bef = float(request.form["SiO2bef"])
    FeBef = float(request.form["FeBef"])
    Sbef = float(request.form["Sbef"])
    Al2O3bef = float(request.form["Al2O3bef"])
    CaObef = float(request.form["CaObef"])
    CuAft = float(request.form["CuAft"])
    SiO2aft = float(request.form["SiO2aft"])
    FeAft = float(request.form["FeAft"])
    Saft = float(request.form["Saft"])
    Al2O3aft = float(request.form["Al2O3aft"])
    CaOaft = float(request.form["CaOaft"])
    O2aft = float(request.form["O2aft"])
    x = flash_smelt(CuBefore,SiO2bef,FeBef,Sbef,Al2O3bef,CaObef,CuAft,SiO2aft,FeAft,Saft,Al2O3aft,CaOaft,O2aft)
    return x


@app.route('/elldg', methods = ['POST'])
@crossdomain(origin='*', headers='Content-Type')
def api_elldg():
    Entha1 = float(request.form["Entha1"])
    Entha2 = float(request.form["Entha2"])
    Entro1 = float(request.form["Entro1"])
    Entro2 = float(request.form["Entro2"])
    x = elldiag(Entha1,Entha2,Entro1,Entro2)
    return x




if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0')

