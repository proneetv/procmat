def rec2(n,Ec,Ea):
    Ecell = Ec+Ea                                                                             #Calculating the Cell Potential
    print "The cell potential of the reaction is Ecell =", round(Ecell,2) ,'Volts'
    dG = -n*96484.56*Ecell                                                                           #Calculating the Free energy of the reaction 
    print"The free energy of the reaction is dG =",round(dG,2),"J"                            #Printing the free energy in joules
    if dG<0:
        print 'The zinc ions will plate out onto the copper at standard conditions ince the reaction is spontaneous(dG<0) ' #Printing the statement for the reaction to be spontaneous. 
    elif dG>0:
        print 'The zinc ions will not plate out onto the copper at standard conditions since the reaction is not spontaneous(dG>0)' #Printing the statement for the reaction to not to be spontaneous.
