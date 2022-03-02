import numpy as np
import matplotlib.pyplot as plt

L_zams = []; Star_mass = []

lw = 1
fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/0.3Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
# plt.plot(data['star_mass'], data['log_L'], label = '0.3 M$_{\odot}$', lw = lw)
Star_mass.append(data['star_mass'][-1]); L_zams.append(data['log_L'][-1])

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/0.7Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
# plt.plot(data['star_mass'], data['log_L'], label = '0.7 M$_{\odot}$', lw = lw)
Star_mass.append(data['star_mass'][-1]); L_zams.append(data['log_L'][-1])

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/1Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
# plt.plot(data['star_mass'], data['log_L'], label = '1 M$_{\odot}$', lw = lw)
Star_mass.append(data['star_mass'][-1]); L_zams.append(data['log_L'][-1])

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/2Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
# plt.plot(data['log_Teff'], data['log_L'], label = '2 M$_{\odot}$', lw = lw)
Star_mass.append(data['star_mass'][-1]); L_zams.append(data['log_L'][-1])

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/3Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
# plt.plot(data['star_mass'], data['log_L'], label = '3 M$_{\odot}$', lw = lw)
Star_mass.append(data['star_mass'][-1]); L_zams.append(data['log_L'][-1])

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/6Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
# plt.plot(data['star_mass'], data['log_L'], label = '6 M$_{\odot}$', lw = lw)
Star_mass.append(data['star_mass'][-1]); L_zams.append(data['log_L'][-1])

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/10Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
# plt.plot(data['star_mass'], data['log_L'], label = '10 M$_{\odot}$', lw = lw)
Star_mass.append(data['star_mass'][-1]); L_zams.append(data['log_L'][-1])

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/16Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
# plt.plot(data['log_Teff'], data['log_L'], label = '2 M$_{\odot}$', lw = lw)
Star_mass.append(data['star_mass'][-1]); L_zams.append(data['log_L'][-1])


fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/30Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
# plt.plot(data['star_mass'], data['log_L'], label = '30 M$_{\odot}$', lw = lw)
Star_mass.append(data['star_mass'][-1]); L_zams.append(data['log_L'][-1])

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/50Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
# plt.plot(data['star_mass'], data['log_L'], label = '50 M$_{\odot}$', lw = lw)
Star_mass.append(data['star_mass'][-1]); L_zams.append(data['log_L'][-1])

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/HRD/Pre-MS/100Msun-Pre-MS/LOGS/history.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
# plt.plot(data['star_mass'], data['log_L'], label = '100 M$_{\odot}$', lw = lw)
Star_mass.append(data['star_mass'][-1]); L_zams.append(data['log_L'][-1])

# plt.gca().invert_xaxis()



plt.xlabel('Log M/M$_{\odot}$')
plt.ylabel('Log L/L$_{\odot}$')

Star_mass = np.log10(Star_mass)

# plt.plot(Star_mass, L_zams, label = 'Models', lw = 0.8)
plt.scatter(Star_mass, L_zams, color = 'gray',  label = 'models')

from scipy.optimize import curve_fit
def fitting_func(x, a, b):
    return a * x + b
            
param, covar = curve_fit(fitting_func, Star_mass[0:2], L_zams[0:2] )
low_mass = np.linspace(Star_mass[0], 0, 10)
plt.plot(low_mass, fitting_func(low_mass, *param), label = 'Fitted Curve: < 1 M$_{\odot}$', color = 'C1', ls = 'dashed')

print(param)

param, covar = curve_fit(fitting_func, Star_mass[2:7], L_zams[2:7] )
intermediate_mass = np.linspace(0, Star_mass[6], 10)
plt.plot(intermediate_mass, fitting_func(intermediate_mass, *param), label = 'Fitted Curve: 1 - 10 M$_{\odot}$', color = 'C2', ls = 'dashed')

print(param)

param, covar = curve_fit(fitting_func, Star_mass[6:11], L_zams[6:11] )
intermediate_mass = np.linspace(1, Star_mass[10], 10)
plt.plot(intermediate_mass, fitting_func(intermediate_mass, *param), label = 'Fitted Curve: 10 - 100 M$_{\odot}$', color = 'C3', ls = 'dashed')

print(param)

plt.legend()

plt.tight_layout()
plt.savefig('ex_4_q1_L_M_regimes.pdf')