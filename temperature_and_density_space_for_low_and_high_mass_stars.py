import numpy as np
import matplotlib.pyplot as plt

#model 612, time ~ 2 x 10^8 years
fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/low_mass_0-3_0-7_3-0/0.3Msun/LOGS/profile17.data'
data = np.genfromtxt(fname, skip_header = 5, names = True, usecols = (2, 3, 10, 11, 12))
plt.plot(data['logRho'], data['logT'], label = '0.3 M$_{\odot}$')
mu_0_3 = 1 / (2 * data['x_mass_fraction_H'] + 0.75 * data['y_mass_fraction_He'] + 0.5 * data['z_mass_fraction_metals'])
mu_0_3_e = 2/(1+data['x_mass_fraction_H'])

#model 639, time ~ 8 x 10^7 years
fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/low_mass_0-3_0-7_3-0/0.7Msun/LOGS/profile17.data'
data = np.genfromtxt(fname, skip_header = 5, names = True, usecols = (2, 3))
plt.plot(data['logRho'], data['logT'], label = '0.7 M$_{\odot}$')

#model 671, time ~ 1 x 10^8 years
fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/1Msun/simulation_data/LOGS/profile19.data'
data = np.genfromtxt(fname, skip_header = 5, names = True, usecols = (2, 3))
plt.plot(data['logRho'], data['logT'], label = '1 M$_{\odot}$')

#model 748, time ~ 4 x 10^6 years
fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/low_mass_0-3_0-7_3-0/3Msun/LOGS/profile20.data'
data = np.genfromtxt(fname, skip_header = 5, names = True, usecols = (2, 3))
plt.plot(data['logRho'], data['logT'], label = '3 M$_{\odot}$')

#model 821, time ~ 1.8 x 10^5 years
fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/high_mass_10_30_50_100/10Msun/LOGS/profile22.data'
data = np.genfromtxt(fname, skip_header = 5, names = True, usecols = (2, 3))
plt.plot(data['logRho'], data['logT'], label = '10 M$_{\odot}$')


#model 2099, time ~ 3 x 10^4 years
fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/high_mass_10_30_50_100/30Msun/LOGS/profile56.data'
data = np.genfromtxt(fname, skip_header = 5, names = True, usecols = (2, 3))
plt.plot(data['logRho'], data['logT'], label = '30 M$_{\odot}$')

#model 5344, time ~ 3.2 x 10^6 years
fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/high_mass_10_30_50_100/50Msun/LOGS/profile143.data'
data = np.genfromtxt(fname, skip_header = 5, names = True, usecols = (2, 3, 10, 11, 12))
plt.plot(data['logRho'], data['logT'], label = '50 M$_{\odot}$')
mu_50_0 = 1 / (2 * data['x_mass_fraction_H'] + 0.75 * data['y_mass_fraction_He'] + 0.5 * data['z_mass_fraction_metals'])

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/high_mass_10_30_50_100/100Msun/LOGS/profile4.data'
data = np.genfromtxt(fname, skip_header = 5, names = True, usecols = (2, 3, 10, 11, 12))
plt.plot(data['logRho'], data['logT'], label = '100 M$_{\odot}$')

x_min, x_max = plt.xlim()


rho = np.linspace(x_min, 9, np.size(mu_0_3))

lw = 0.7
temp = 3.2 * 10**7 * (10**rho)**(1/3) * mu_0_3**(-1/3)
plt.plot(rho, np.log10(temp), ls = 'dashed', color = 'k', lw = lw)



# rho = np.linspace(x_min, x_max, np.size(mu_50_0))
# temp = 3.2 * 10**7 * (10**rho)**(1/3) * mu_50_0**(-1/3)
# plt.plot(rho, np.log10(temp), ls = 'dashed', color = 'b', label = '50')

rho = np.linspace(x_min, 6, np.size(mu_0_3))
temp_g_nr = 1.21 * 10**5 * (10**rho)**(2/3) * mu_0_3 * mu_0_3_e**(-5/3)
plt.plot(rho, np.log10(temp_g_nr), ls = 'dashed', color = 'k', lw = lw)


plt.vlines(np.log10(9.7 * 10**5 * mu_0_3_e[0]), ymin = 0, ymax = 8.9, ls = 'dashed', lw = lw)


rho = np.linspace(6, 9, 100)
temp_g_er = 1.5 * 10**7 * (10**rho)**(1/3) * mu_0_3[0] * mu_0_3_e[0]**(-4/3)
plt.plot(rho, np.log10(temp_g_er), ls = 'dashed', color = 'k', lw = lw)



plt.text(-7.5, 6.5, 'radiation')
plt.text(-8.5, 2.8, 'ideal gas')
plt.text(4.54, 5, 'degenerate')
plt.text(1.5, 2.8, 'NR')
plt.text(7.35, 2.8, 'ER')

plt.xlim(-9.5,9)
plt.ylabel('Log T (K)')
plt.xlabel(r'Log $\rho$ (g/cm$^{-3}$)')
plt.ylim(2,10)
# plt.gca().set_aspect('equal')
#plt.xscale('log')
#plt.tight_layout()
#plt.legend(loc = 'center left')
plt.legend(ncol = 2)


# plt.title('3 M$_{\odot}$')


plt.tight_layout()
# plt.show()
# plt.savefig('ex3_q1_trho.pdf')