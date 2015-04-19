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
    s = 'specific surface area '  + round(Ss,2) + 'm2/kg' 
    s = s +'height ' +  round(H,2) + ' m'
    s = s + 'Mass flow rate of ' + round(am,2) + 'kg/m2-s'
    s = s + 'Moisture to be removed ' + round(mm,2) + 'kg/m2'
    s = s + 'heat transfer coefficent ' + round(h,2) + 'W/m2-k'
    s = s + 'Final air outlet Temp ' + round(tgf,2) + 'kelvin'
    s = s + 'Total time for drying '  + round(time1,2) + 'Min.'
