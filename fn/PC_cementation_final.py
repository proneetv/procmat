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
	

print cementation(Eanode, Ecathode, n, T, Fe)
