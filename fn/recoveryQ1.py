def rec1(I,T):
	Q = I*T*60*60             #Calculating the total charge being passed in the cell
	dM = 63.5*Q/(2*96500)     #Calculating mass of copper deposited on the cathode
	print 'Change in mass of the Copper cathode and that of anode is dM =',round(dM,2),'grams'
