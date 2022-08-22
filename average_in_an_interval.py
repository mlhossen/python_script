####this python script calaultes avearge of successive intervals of a certain data set, The current ####
####Current set up calculates average of a data file which has single column from where we are #########
####calculating average that's why interval = [x ** 1 for x in r[i:i + 100]] has 1 after ** where#######
#### the number 1 is indicating the column number. x (not X or Y axis) is just a variable.##############
import numpy as np
filename = 'In_Na_202_hbonds.dat'
r = np.loadtxt(filename)
for i in range(0, 3900, 100):
    interval = [x ** 1 for x in r[i:i + 100]]
    av_r = np.mean(interval)
    print(av_r)
