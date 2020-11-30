'''
Plotting oligometastasis growth curves.

Jacob Scott 24 May 2020

'''

import pylab
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np
from math import log as ln
from pylab import rcParams

# where to save file
write_path = 'oligomets/'


# first set up the parameter space you want
total_t = int(1.3*10**3)
end_time = int(1.3*10**3)

# print(total_t/4,total_t/2,3*total_t/4)
tumor_doubling_time = [150, 200, 300, 400]  #comment for pcolor, use for surface
r = [ln(2) / tumor_doubling_time[i] for i in range(len(tumor_doubling_time))]
# size = 1000
# N_d = [0.1, 0.35, 0.6, 0.85]

N_c = [5]
t0 =  np.linspace(0, end_time, total_t)
t =  np.linspace(0, end_time, total_t)
t1 = np.linspace((3/8)*end_time, end_time, (5/8)*total_t)
t2 = np.linspace((1/2)*end_time, end_time, (1/2)*total_t)
t3 = np.linspace((5/8)*end_time, end_time, (3/8)*total_t)

N0 = [100 for i in range(total_t)]
N = [np.exp(r[0]*t[i]) for i in range(total_t)]
# print(N)
N1 = [(N[int((3/8)*total_t)] - N_c) * np.exp(r[0]*t[i]) for i in range(int((5/8)*total_t))]
N2 = [(N[int((1/2)*total_t)] - N_c) * np.exp(r[0]*t[i]) for i in range(int((1/2)*total_t))]
N3 = [(N[int((5/8)*total_t)] - N_c) * np.exp(r[0]*t[i]) for i in range(int((3/8)*total_t))]

# print(N[int(total_t/4)] - N_c,N[int(total_t/2)] - N_c, N[int(3*total_t/4)] - N_c)

""" PLOT """

# print(len(N),len(t),len(N1),len(t1),len(N2),len(t2),len(N3),len(t3))

plt.plot(t0,N0, c = 'k', linestyle = '--',label='$N_T$',linewidth = 5.0)
plt.plot(t,N, c = 'k', label='Untreated',linewidth = 5.0)
plt.plot(t1,N1, c = 'g', label='Treat early',linewidth = 5.0)
plt.plot(t2,N2, c = 'r', label='Treat middle',linewidth = 5.0)
plt.plot(t3,N3, c = 'c', label='Treat late',linewidth = 5.0)
# plt.title('OS benefit, $t_d$ = '+str(tumor_doubling_time[i]))
plt.xlabel('time (days)')
plt.ylabel('$N(t)$')
plt.grid()
plt.xlim((400,1200))
plt.ylim((0,120))
plt.legend(loc = 4)
# plt.semilogy()
# cbar = plt.colorbar()
# cbar.set_label('Days', rotation = 90)
# plt.xscale('log')
# plt.yscale('log')




plt.savefig(write_path+'oligomets_curves.png', dpi = 500)

# plt.show()
