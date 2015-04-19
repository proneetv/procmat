def dryk(m,Xi,Xc,Rc,Xf,Rf):
	Rc = Rc * (10**(-3))
	Rf = Rf * (10**(-3))
	y1 = Xi / (100 - Xi)
	y3 = Xf / (100 - Xf)
	tc = (m * ( y1 - Xc ) ) / (Rc)
	tf = (m * (( Xc- y3)/ (Rc - Rf))) * ((math.log(Rc/Rf)))
	tt = tc + tf

	s = "Constant falling rate time: " + tc + "sec" + "\nFirst falling rate time:" + tf + "sec\n"
	s = s + "Total time: " + tt + "sec"
