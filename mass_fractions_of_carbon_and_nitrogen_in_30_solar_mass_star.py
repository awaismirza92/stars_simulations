import numpy as np
import matplotlib.pyplot as plt

# fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/high_mass_10_30_50_100/30Msun/LOGS/profile56.data'
# data = np.genfromtxt(fname, skip_header = 5, names = True)


# plt.plot(data['mass'], data['c12'], label = 'Carbon 12')

# plt.plot(data['mass'], data['n14'], label = 'Nitrogen 14')


fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/high_mass_10_30_50_100/30Msun/LOGS/profile1.data'
data = np.genfromtxt(fname, skip_header = 5, names = True)
plt.plot(data['mass'], data['c12'], label = '$^{12}$C at beginning', color = 'C10')




# fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/high_mass_10_30_50_100/30Msun/LOGS/profile81.data'
# data = np.genfromtxt(fname, skip_header = 5, names = True)


# plt.plot(data['mass'], data['c12'], label = 'Carbon 12', color = 'C10', ls = 'dashed')

# plt.plot(data['mass'], data['n14'], label = 'Nitrogen 14', color = 'C1', ls = 'dashed')



fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/high_mass_10_30_50_100/30Msun/LOGS/profile68.data'
data1 = np.genfromtxt(fname, skip_header = 5, names = True)


plt.plot(data1['mass'], data1['c12'], label = '$^{12}$C at RGB start', color = 'C10', ls = 'dotted')

plt.plot(data['mass'], data['n14'], label = '$^{14}$N at beginning', color = 'C1')

plt.plot(data1['mass'], data1['n14'], label = '$^{14}$N at RGB start', color = 'C1', ls = 'dotted')



# fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/high_mass_10_30_50_100/30Msun/LOGS/profile86.data'
# data = np.genfromtxt(fname, skip_header = 5, names = True)


# plt.plot(data['mass'], data['c12'], label = 'Carbon 12', color = 'C10', ls = '-.')

# plt.plot(data['mass'], data['n14'], label = 'Nitrogen 14', color = 'C1', ls = '-.')

plt.xlabel('m/M$_{\odot}$')
plt.ylabel('Mass fraction')
# plt.yscale('log')
# plt.ylim(1e-4,1)

plt.legend()
plt.tight_layout()
plt.savefig('ex3_q2_c_n_core.pdf')