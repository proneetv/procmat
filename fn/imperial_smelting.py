
def imperialsmelting(ZNOp, PBOp, FEOp, SIOp, sc, ZNp, CO2CO):

	ZNOw = (sc * ZNOp)/100
	PBOw = (sc * PBOp)/100
	FEOw = (sc * FEOp)/100
	SIOw = (sc * SIOp)/100

	ZNOm = ZNOw/81
	PBOm = PBOw/223
	FEOm = FEOw/72
	SIOm = SIOw/60
	
	Y = (ZNOm * 100) / ZNp

	ZNf = ZNOm
	COf = 2*(ZNOm + PBOm)
	CO2f = CO2CO * COf
	N2f = 1.5 * (ZNOm + PBOm) * 3.76
	
	O2f = (Y - (ZNf + COf + CO2f + N2f)) * 0.21
	
	N2f1 = N2f + (Y - (ZNf + COf + CO2f + N2f) - O2f)
	
	air_amount = N2f1/0.79
	liq_lead = PBOm
	slagFEO = FEOm
	slagSIO2 = SIOm
	coke_amount = COf + CO2f
	coke_amountf = coke_amount * 12
	
	HZNOo = 83500 #standard enthalpy of ZnO
	HPBOo = 52500 #standard enthalpy of PbO
	HZNO = 9500 #enthalpy of ZnO(1100-298)
	HPBO = 10800 #enthalpy of PbO (1100-298)
	HFEO = 10280 #enthalpy of FeO (1100-298)
	HSIO = 19940 #enthalpy of SiO2 (1100-298)
	HZN = 36160 #enthalpy of Zn (v) (1300-298)
	HCO2 = 12010 #enthalpy of CO2 (1300-298)
	HCO = 7460 #enthalpy of CO (1300-298)
	HN2 = 7500 #enthalpy of N2 (1300-298)
	HO2 = 7873 #enthalpy of O2 (1300-298)
	HPB = 10110 #enthalpy of Pb (1600-298)
	HFEOr = 11990 #enthalpy of FeO (1600-298)
	HSIO2r = 21100 #enthalpy of SiO2 (1600-298)
	slag_formation = 30602 #enthalpy of slag formation
	
	heat_reaction = (HZNOo * ZNOm)+ (HPBOo * PBOm)
	heat_reactants = (HZNO * ZNOm) + (HPBO * PBOm) + (HFEO * FEOm) + (HSIO * SIOm)
	heat_gases = (HZN * ZNf) + (HCO2 * CO2f) + (HCO * COf) + (HN2 * N2f1) + (HO2 * O2f)
	heat_slag = (HPB * liq_lead) + (HFEOr * slagFEO) + (HSIO2r * slagSIO2)
	heat_input = heat_reaction + heat_reactants + slag_formation
	heat_output = heat_gases + heat_slag
	heat_deficit = heat_output - heat_input
	Cp = 7.5
	Preheated_T = heat_deficit / (Y * Cp)
	
	outputList = []
	outputList.append( ZNf ) #moles of zinc in vapour
	outputList.append( COf ) # moles of CO2
	outputList.append( CO2f ) # moles of CO
	outputList.append( O2f ) # moles of O2
	outputList.append( N2f1 ) #moles of N2
	outputList.append( air_amount ) # amount of air in moles
	outputList.append( liq_lead ) #moles of lead
	outputList.append( slagFEO ) #moles of FeO in slag
	outputList.append( slagSIO2 ) #moles of FeO in slag
	outputList.append( coke_amountf ) # amount of coke in kg
	outputList.append( Preheated_T ) # Preaheated temperature in K
	return outputList
	
	

ZNOp=float(raw_input('Input percentage of ZnO : '))
PBOp=float(raw_input('Input percentage of PbO : '))
FEOp=float(raw_input('Input percentage of FeO : '))
SIOp=float(raw_input('Input percentage of SiO2 : '))
sc=float(raw_input('Input Sinter Capacity : '))
ZNp=float(raw_input('Input percentage of Zn(v) in gas : '))
CO2CO=float(raw_input('Input percentage of CO2/CO ratio : '))

print imperialsmelting(ZNOp, PBOp, FEOp, SIOp, sc, ZNp, CO2CO)
raw_input("press<Enter>")
