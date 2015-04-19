def elldiag(R1,R2,x1,y1,x2,y2):
    x1 = round(x1, 2)
    y1 = round(y1, 2)
    x2 = round(x2, 2)
    y2 = round(y2, 2)

    list1 = [x1, y1]
    list2 = [x2, y2]

    if list1[1] == list2[1]:
        print 'There exist no temp. where gibbs free energy of both the reactions in same'

    else:
        int = 'temp' 
        temp = float(list1[0]-list2[0])/float(list1[1]-list2[1])
        temp = round(temp, 2)
        print "Equ. Temp: =",round(temp,2),"K"

