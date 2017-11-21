import sys
def holtwinters(y, alpha, beta, gamma, c, debug=True):
    """
    y - time series data.
    alpha , beta, gamma - exponential smoothing coefficients 
                                      for level, trend, seasonal components.
    c -  extrapolated future data points.
    	  1 daily
          4 quarterly
          7 weekly.
          12 monthly
 
 
    The length of y must be a an integer multiple  (> 2) of c.
    """
    #Compute initial b and intercept using the first two complete c periods.
    ylen =len(y)
    if ylen % c !=0:
        return None
    fc =float(c)
    ybar2 =sum([y[i] for i in range(c, 2 * c)])/ fc
    ybar1 =sum([y[i] for i in range(c)]) / fc
    b0 =(ybar2 - ybar1) / fc
    # if debug: # print "b0 = ", b0
 
    #Compute for the level estimate a0 using b0 above.
    tbar  =sum(i for i in range(1, c+1)) / fc
    # print tbar
    a0 =ybar1  - b0 * tbar
    # if debug: print "a0 = ", a0
 
    #Compute for initial indices
    I =[(float(y[i]) / float((a0 + (i+1) * b0))) for i in range(0, ylen)]
    # if debug: print "Initial indices = ", I
 
    S=[0] * (ylen+ c)
    for i in range(c):
        S[i] =(I[i] + I[i+c]) / 2.0
 
    #Normalize so S[i] for i in [0, c)  will add to c.
    tS =c / sum([S[i] for i in range(c)])
    for i in range(c):
        S[i] *=tS
        # if debug: print "S[",i,"]=", S[i]
 
    # Holt - winters proper ...
    # if debug: print "Use Holt Winters formulae"
    F =[0] * (ylen+ c)   
    
    At =a0
    Bt =b0
    for i in range(ylen):
        Atm1 =At
        Btm1 =Bt
        At =alpha * y[i] / S[i] + (1.0-alpha) * (Atm1 + Btm1)
        Bt =beta * (At - Atm1) + (1- beta) * Btm1
        S[i+c] =gamma * y[i] / At + (1.0 - gamma) * S[i]
        F[i]=(a0 + b0 * (i+1)) * S[i]
        # print "i=", i+1, "y=", y[i], "S=", S[i], "Atm1=", Atm1, "Btm1=",Btm1, "At=", At, "Bt=", Bt, "S[i+c]=", S[i+c], "F=", F[i]
        # print i,y[i],  F[i]
    #Forecast for next c periods:
    for m in range(c):
        print (At + Bt* (m+1))* S[ylen + m]
 
# the time-series data.
temp = sys.argv[1]
temp=temp.split()
y = [float(x) for x in temp]
# y =[146, 96, 59, 133, 192, 127, 79, 186, 272, 155, 98, 219]
 
holtwinters(y, 0.2, 0.1, 0.05, 1)
