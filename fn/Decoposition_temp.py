def Decomposition_Temp(x1,y1,x2,y2):
    
    #(x1,y1) and(x2,y2) are two points from line of some carbonate from graph of ∆𝐺°v/s T
    #m=slope of the line in form of y=mx+c
    #c=y axis intercept of the line in form of y=mx+c
    #Here,y=(delta)G and x= Temp
    #DT=Decomposition temperature and DT=(c/R)/(m/R)
    
    m=(y2-y1)/(x2-x1)
    c=y1-(m*x1)
    DT=c/m
    
    return DT

print Decomposition_Temp(3,29,20,69)                                      #answer 9.325 ie DT
print Decomposition_Temp(50,60,35,58)                                     #answer 400.0 i.e DT
print Decomposition_Temp(75,90,2,19)                                     #answer 17.5352112676 i.e DT



    
