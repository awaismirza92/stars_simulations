import numpy as np
import matplotlib.pyplot as plt

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/high_mass_10_30_50_100/10Msun/LOGS/history.data_old'
data = np.genfromtxt(fname, skip_header = 5, names = True)

fig, ax1 = plt.subplots()

ax1.plot(data['star_age'], data['log_L'], label = 'Surface luminosity')
ax1.plot(data['star_age'], data['log_LH'], label = 'Hydrogen luminosity')
ax1.plot(data['star_age'], data['log_LHe'], label = 'Helium luminosity')

ax1.set_ylim(3.4,4.5)
ax1.set_ylim(2.5,4.5)

plt.xlabel('Star age (years)')
plt.ylabel('Log L/L$_{\odot}$')
plt.xlim(1.99e7,2.4e7)
# plt.xlim(2e7,2.075e7)
plt.legend(loc = 'lower left')

ax1.text(2.01e7, 3.9, 'A')
ax1.text(2.017e7, 3.56, 'B')
ax1.text(2.017e7, 4.18, 'C')

ax2 = ax1.twinx()
# ax2.plot(data['star_age'], data['log_Teff'], color = 'C3', label = 'Effective temperature')
# ax2.plot(data['star_age'], data['center_h1'], color = 'C3', label = 'Effective temperature')
ax2.plot(data['star_age'], data['center_he4'], color = 'C3', label = 'Y')
plt.ylabel('mass fraction')
# ax2.set_ylim(3.5,4.7)
# ax2.set_ylim(0,0.004)
ax2.set_ylim(0.96,1)
plt.legend()

# for i in range(data['star_age'].size):
#     if data['star_age'][i+1]-data['star_age'][i]<0:
#         print(data['star_age'][i+1])


plt.tight_layout()

# plt.savefig('ex3_q3_time.pdf')
