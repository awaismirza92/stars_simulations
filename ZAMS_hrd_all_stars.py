import numpy as np
import matplotlib.pyplot as plt

L_zams = []; T_zams = []

lw = 1
fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/0.3Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['log_Teff'], data['log_L'], label = '0.3 M$_{\odot}$', lw = lw)
T_zams.append(data['log_Teff'][-1]); L_zams.append(data['log_L'][-1])

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/0.7Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['log_Teff'], data['log_L'], label = '0.7 M$_{\odot}$', lw = lw)
T_zams.append(data['log_Teff'][-1]); L_zams.append(data['log_L'][-1])

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/1Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['log_Teff'], data['log_L'], label = '1 M$_{\odot}$', lw = lw)
T_zams.append(data['log_Teff'][-1]); L_zams.append(data['log_L'][-1])

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/2Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['log_Teff'], data['log_L'], label = '2 M$_{\odot}$', lw = lw)
T_zams.append(data['log_Teff'][-1]); L_zams.append(data['log_L'][-1])

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/3Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['log_Teff'], data['log_L'], label = '3 M$_{\odot}$', lw = lw)
T_zams.append(data['log_Teff'][-1]); L_zams.append(data['log_L'][-1])

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/6Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['log_Teff'], data['log_L'], label = '6 M$_{\odot}$', lw = lw)
T_zams.append(data['log_Teff'][-1]); L_zams.append(data['log_L'][-1])

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/10Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['log_Teff'], data['log_L'], label = '10 M$_{\odot}$', lw = lw)
T_zams.append(data['log_Teff'][-1]); L_zams.append(data['log_L'][-1])

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/16Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['log_Teff'], data['log_L'], label = '16 M$_{\odot}$', lw = lw)
T_zams.append(data['log_Teff'][-1]); L_zams.append(data['log_L'][-1])

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/30Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['log_Teff'], data['log_L'], label = '30 M$_{\odot}$', lw = lw)
T_zams.append(data['log_Teff'][-1]); L_zams.append(data['log_L'][-1])

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/50Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['log_Teff'], data['log_L'], label = '50 M$_{\odot}$', lw = lw)
T_zams.append(data['log_Teff'][-1]); L_zams.append(data['log_L'][-1])

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/100Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['log_Teff'], data['log_L'], label = '100 M$_{\odot}$', lw = lw)
T_zams.append(data['log_Teff'][-1]); L_zams.append(data['log_L'][-1])

plt.gca().invert_xaxis()



plt.xlabel('Log T$_{eff}$ (K)')
plt.ylabel('Log L/L$_{\odot}$')

# L = [-0.12, -0.18]

plt.plot(T_zams, L_zams, ls = 'dotted', label = 'ZAMS')

plt.legend()

plt.tight_layout()
plt.savefig('ex_4_q1_ZAMS_hrd.pdf')