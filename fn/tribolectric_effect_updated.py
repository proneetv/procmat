def triboelectric(E,qa,Ma,x):
    g = 9.8
    y=3.2     
    tsquare = (2*y)/g
    t = tsquare**(0.5)
    x = (qa*E*tsquare)/(2*Ma) 
    return "X = " + str(round(x,2)) + ", Time = " str(round(t,2)) "sec"

triboelectric(4,3,4,3)