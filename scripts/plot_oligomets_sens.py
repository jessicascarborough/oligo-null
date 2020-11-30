'''
Plotting oligometastasis parameter sensitivity and growth curves.

Jacob Scott 23 May 2020

'''
import pylab
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np
from math import log as ln
from pylab import rcParams

# where to save file
write_path = 'oligomets/'


# first set up the parameter space you want
# tumor_doubling_time = [100] # use for pcolor, comment for surface
tumor_doubling_time = [100, 200, 300, 400]  #comment for pcolor, use for surface
r = [ln(2) / tumor_doubling_time[i] for i in range(len(tumor_doubling_time))]
size = 500
N_d = np.logspace(9, 13, size)
N_c = np.logspace(9, 13, size)
Delta_t1 =  np.zeros([size, size, len(r)])  #surface

# Delta_t1 =  np.zeros([size, size])  #pcolor

#calculate Delta t (surface)
for k in range(len(r)):
	for i in range(size):
		for j in range(size):
			if N_c[j] >= N_d[i]:
				Delta_t1[j,i,k] = 0
			else:
				Delta_t1[j,i,k] = (1/r[k]) * (ln (N_d[i] / (N_d[i] - N_c[j])) )

#calculate Delta t (pcolor)
# for i in range(size):
# 	for j in range(size):
# 		if N_c[j] >= N_d[i]:
# 			Delta_t1[j,i] = 0
# 		else:
# 			Delta_t1[j,i] = (1/r) * (ln (N_d[i] / (N_d[i] - N_c[j])) )


""" PLOT """

rcParams['figure.figsize'] = 13,11
# fig, ax = plt.subplots()
# heatmap = ax.pcolor(data, cmap='inferno', vmin=0, vmax=1)

for i in range(len(tumor_doubling_time)):
	plt.subplot(2, 2, i+1)
	heatmap = plt.pcolor(N_d, N_c, Delta_t1[:,:,i], cmap='viridis', norm=LogNorm())
	plt.title('OS benefit, $t_d$ = '+str(tumor_doubling_time[i])+' days')
	plt.xlabel('$N_d$')
	plt.ylabel('$N_c$')
	cbar = plt.colorbar()
	cbar.set_label('Days', rotation = 90)
	plt.xscale('log')
	plt.yscale('log')
	plt.clim(10**-1,10**3)
	plt.grid()

	# delta = 10**10
	# x = np.arange(10**9, 10**13, delta)
	# y = np.arange(10**9, 10**13, delta)
	X, Y = np.meshgrid(N_d,N_c)


	def iso_survival(X,Y,i):
		# if X < Y:
		# 	return 0
		# else:
		return (1/r[i]) * np.log(X/(X-Y))

	Z = iso_survival(X,Y,i) 



	# Create a simple contour plot with labels using default colors.  The
	# inline argument to clabel will control whether the labels are draw
	# over the line segments of the contour, removing the lines beneath
	# the label
	# plt.figure()
	CS = plt.contour(X, Y, Z, linewidths = 2, colors= 'k', levels=[1, 3, 10, 30, 100, 300, 1000])
	plt.clabel(CS, inline=1, fontsize=10, fmt='%1.0f')
	# plt.clf()
	# plt.figure()



plt.savefig(write_path+'oligomets_sens_4plot.png', dpi = 500)

# plt.show()
