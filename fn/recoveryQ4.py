def rec4(N,Na,Nc,A,L,i,R,n,k,):
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

	s = '\nThe Current Efficiency is ' + round(ni,2)
	s = s + '\nThe Voltage across each cell is ' + round(V,2) + 'V'
	s = s + '\nThe Voltage efficiency is ' + round(nv,2)
	s = s + '\nThe Power efficiency is ' + round(np,2)
	s = s + '\nThe Power consumed across all cells is ' + round(P,2) + 'Watt'
	return s
