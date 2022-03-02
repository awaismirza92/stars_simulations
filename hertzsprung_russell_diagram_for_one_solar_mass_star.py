import numpy as np
import matplotlib.pyplot as plt
import math

fname = '/e_drive/MEGA/MSc_Astrophysics/3rd_Semester/SSE/Lab/Simulations/1Msun/simulation_data/LOGS/history.data'

data = np.genfromtxt(fname, skip_header = 5, names = True)

complete_model_number = data['model_number'].tolist()

model_number = []; log_Teff = []; log_L = []

for i in np.arange(len(complete_model_number)):
    if complete_model_number[i] > 500 and complete_model_number[i] < 900:
        model_number.append(data['model_number'][i])
        log_Teff.append(data['log_Teff'][i])
        log_L.append(data['log_L'][i])

plt.figure(dpi = 150)

plt.plot(log_Teff, log_L, label = 'Track of 1M$_{\odot}$ star', c = 'C9')
plt.gca().invert_xaxis()

#for i in np.arange(len(model_number)):
#    plt.text(log_Teff[i],log_L[i], str(model_number[i]), fontsize = 5)

color = 'red'

T_sun = math.log10(5772)
plt.scatter(T_sun, 0, marker = 'o', color = color, s = 40, edgecolors=color, label = 'Sun right now')

index = model_number.index(744)
print(index)
print(model_number[80])
print(model_number[81])
print(model_number[82])

print(np.sqrt((log_Teff[80]-T_sun)**2 + (log_L[80]-0)**2))
print(np.sqrt((log_Teff[81]-T_sun)**2 + (log_L[81]-0)**2))
print(np.sqrt((log_Teff[82]-T_sun)**2 + (log_L[82]-0)**2))
print(np.sqrt((log_Teff[83]-T_sun)**2 + (log_L[83]-0)**2))
print(np.sqrt((log_Teff[84]-T_sun)**2 + (log_L[84]-0)**2))

color = 'b'
plt.scatter(log_Teff[index], log_L[index], marker = 'o', color = color, s = 40, edgecolors=color, label = 'Nearest model: 743')

plt.xlabel('Temperature Log T$\mathrm{_{eff}}$ (K)')
plt.ylabel(r'$\frac{L}{L_{\odot}}$')
plt.ylabel(r'Luminosity Log L (L$_{\odot}$)')
plt.legend()
plt.tight_layout()
plt.savefig('ex1_hr.pdf')
plt.show()