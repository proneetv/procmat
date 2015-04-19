#===========================================================================================================================
#Code Authors name: Prateek Mishra, Pranshul Jain
#Roll no.s: 12507, 12501



import sys
import numpy as np  
import matplotlib.pyplot as plt  

def graph(a, b, c, T, G):
    assert(c == 0 or c == 1), "c can only be 0 or 1\n";
    m = a / b               # m is slope
    if c == 1:              # if on same side slope is negative
        m = -m
    k = G / (8.314*T)       
    x = np.array(range(-4, 4))
    y = eval('x * m + k')   # evaluating the y coordinates
    plt.plot(x, y)          # plotting

N = int(raw_input("Enter the number of lines you want to plot: "))
for i in xrange(N):
    a = float(raw_input("Enter the coefficient of O2: "))
    b = float(raw_input("Enter the coefficient of SO2: "))
    c = int(raw_input("enter 1 if both O2 and SO2 lie on the same side, else enter 0: "))
    T = float(raw_input("Enter the temperature (in Kelvin): "))
    G = float(raw_input("Enter the value of Delta G naught(in KJ / mol): "))

    graph(a, b, c, T, G)        # plotting with required values

plt.show()      # Printing the graph




