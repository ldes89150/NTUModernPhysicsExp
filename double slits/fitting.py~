import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
dslit = pd.read_csv("laser.csv")

xx = np.array(dslit["x(mm)"])
laserf = np.array(dslit["laserF(nV)"])

be = np.pi/0.67 # unit in um
pk = 194.-15.


def det(z):
    return (z-2.25)/500.# np.sin(np.arctan((z-2.25)/500.))

# sin(theta) ~ theta ~ x
def dos(x, b, d, c):
    return pk*(np.cos(be*d*(det(x)))**2)*(np.sin(be*b*(det(x))))**2/(be*b*(det(x)))**2+15.
par, potv = curve_fit(dos, xx, laserf, p0=[100.,350.,15.])
print par

ll = dos(xx, 100.,457.,15.)
lf = dos(xx, par[0],par[1],15.)
rs = []
for i in range(len(xx)):
    rs.append(laserf[i]-lf[i])

f = open("laserf.txt", "w")
for i in range(len(xx)):
    f.write(str(xx[i])+'  '+str(laserf[i])+'  '+str(lf[i])+'  '+str(ll[i])+'\n')
f.close()


# def dosl(p, fjac=None, x=None, y=None, err=None):
#     model = pk*(np.sin(be*p[0]*x))**2/(be*p[0]*x)**2 \
#            *((np.cos(be*(p[0]+p[1])*x))**2)
#     status = 0
#     return [status, (y-model)/err]

# pds = [100., 200.]
# fa = {'x':xx, 'y':laserf, 'err':[0.1 for i in range(len(xx))]}
# mp = mpfit.mpfit(dosl, pds, functkw=fa)
# print mp.params

