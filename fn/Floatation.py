import time

def float_float(T,t,n,T1,N):

	num = T/t
	num = int(num)
	print num
	conc = []
	time = []
	for i in range(0,num+1):
	    print('input concn at time')
	    print i*t
	    conc.append(float(raw_input('')))
	    time.append(i*t)

	print conc
	print time
	#time.sleep(15)

	m=[[]]
	m[0].extend([conc[0],time[0]])
	for i in range(1, num+1):
	    m.append([conc[i],time[i]])

	    # print tc
	    # conc_time.append(tc)
	    
	print m

