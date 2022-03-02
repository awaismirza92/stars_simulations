import numpy as np
import matplotlib.pyplot as plt


lw = 1
fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/low_mass_0-3_0-7_3-0/0.3Msun/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['log_Teff'], data['log_L'], label = '0.3 M$_{\odot}$', lw = lw)


fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/low_mass_0-3_0-7_3-0/0.7Msun/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['log_Teff'], data['log_L'], label = '0.7 M$_{\odot}$', lw = lw)

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/1Msun/simulation_data/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['log_Teff'], data['log_L'], label = '1 M$_{\odot}$', lw = lw)

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/low_mass_0-3_0-7_3-0/3Msun_rerun2/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['log_Teff'], data['log_L'], label = '3 M$_{\odot}$', lw = lw)

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/6Msun/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['log_Teff'], data['log_L'], label = '6 M$_{\odot}$', lw = lw)

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/high_mass_10_30_50_100/10Msun/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['log_Teff'], data['log_L'], label = '10 M$_{\odot}$', lw = lw)


fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/high_mass_10_30_50_100/30Msun/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['log_Teff'], data['log_L'], label = '30 M$_{\odot}$', lw = lw)

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/high_mass_10_30_50_100/50Msun/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['log_Teff'], data['log_L'], label = '50 M$_{\odot}$', lw = lw)

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/high_mass_10_30_50_100/100Msun/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['log_Teff'], data['log_L'], label = '100 M$_{\odot}$', lw = lw)

plt.gca().invert_xaxis()

plt.legend()

plt.xlabel('Log T$_{eff}$ (K)')
plt.ylabel('Log L/L$_{\odot}$')

# L = [-0.12, -0.18]



plt.tight_layout()
plt.savefig('ex_4_q1_HRD.pdf')