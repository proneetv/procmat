def roasting(iCu,iSiO2,iFe,iS,iAl2O3,iCaO,fCu,fSiO2,fFe,fS,fAl2O3,fCaO,fO2):
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