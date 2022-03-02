import numpy as np
import matplotlib.pyplot as plt
import math

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/low_mass_0-3_0-7_3-0/3Msun/LOGS/history.data'

ax = plt.subplot()

data = np.genfromtxt(fname, skip_header = 5, names = True)


plt.plot(data['star_age'], data['log_abs_Lgrav'], label = 'Gravitational')
plt.plot(data['star_age'], data['pp'], label = 'pp-chain')
plt.plot(data['star_age'], data['cno'], label = 'CNO')
plt.plot(data['star_age'], data['tri_alfa'], label = 'tri_alfa')
plt.plot(data['star_age'], data['burn_c'], label = 'burn_c')
plt.plot(data['star_age'], data['burn_n'], label = 'burn_n')
plt.plot(data['star_age'], data['burn_o'], label = 'burn_o')

# plt.xlim(5e-6,0.4e10)
plt.xlim(1e6,0.6e9)
y_min, y_max = plt.ylim(-20, 10)
plt.xlabel('Age (years)')
plt.ylabel('Log L/L$_{\odot}$')
plt.xscale('log')
#plt.tight_layout()
plt.legend(loc = 'upper left', ncol = 3)
#plt.legend(ncol = 2)
# plt.legend()


# plt.annotate('MS starts', (2.6e6, -1), xytext = (2.6e6, -14), horizontalalignment = 'center',
#                 arrowprops = dict(arrowstyle = "->") )

# plt.annotate('MS ends', (3.1e8, -1), xytext = (2.0e8, -10), horizontalalignment = 'center',
#                 arrowprops = dict(arrowstyle = "->") )

plt.vlines(x = 4e6, ymin = -20, ymax = y_max, colors = 'C2', lw = 0.8, ls = 'dotted')
plt.vlines(x = 3.2e8, ymin = -20, ymax = y_max, colors = 'C3', lw = 0.8, ls ='dashed')

plt.title('3 M$_{\odot}$')




from mpl_toolkits.axes_grid1.inset_locator import inset_axes
axins = inset_axes(ax, 3, 1, bbox_to_anchor=(0.87,0.55), bbox_transform=ax.figure.transFigure)

axins.set_xlim(3e8,4.7e8)
axins.set_ylim(-4, 8)

plt.plot(data['star_age'], data['log_abs_Lgrav'], label = 'Gravitational')
plt.plot(data['star_age'], data['pp'], label = 'pp-chain')
plt.plot(data['star_age'], data['cno'], label = 'CNO')
plt.plot(data['star_age'], data['tri_alfa'], label = 'tri_alfa')
plt.plot(data['star_age'], data['burn_c'], label = 'burn_c')
plt.plot(data['star_age'], data['burn_n'], label = 'burn_n')
plt.plot(data['star_age'], data['burn_o'], label = 'burn_o')

from mpl_toolkits.axes_grid1.inset_locator import mark_inset
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

axins.vlines(x = 3.2e8, ymin = -20, ymax = y_max, colors = 'C3', lw = 0.8, ls ='dashed')

plt.tight_layout()
plt.savefig('ex2_3_0_nuc_prod.pdf')