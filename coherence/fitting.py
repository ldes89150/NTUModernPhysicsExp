import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from numpy import genfromtxt

bdg = np.array(genfromtxt('bulb_double_green.csv', delimiter=','))
bdgx = np.array([i for i in range(len(bdg))])
bdp = np.array(genfromtxt('bulb_double_polarizer.csv', delimiter=','))
bdpx = np.array([i for i in range(len(bdp))])
bd = np.array(genfromtxt('bulb_double.csv', delimiter=','))
bdx = np.array([i for i in range(len(bd))])
btg = np.array(genfromtxt('bulb_triple_green.csv', delimiter=','))
btgx = np.array([i for i in range(len(bdg))])
btp = np.array(genfromtxt('bulb_triple_polarizer.csv', delimiter=','))
btpx = np.array([i for i in range(len(bdg))])
bt = np.array(genfromtxt('bulb_triple.csv', delimiter=','))
btx = np.array([i for i in range(len(bdg))])

hdg = np.array(genfromtxt('hg_double_green.csv', delimiter=','))
hdgx = np.array([i for i in range(len(hdg))])
hdp = np.array(genfromtxt('hg_double_polarizer.csv', delimiter=','))
hdpx = np.array([i for i in range(len(hdg))])
hd = np.array(genfromtxt('hg_double.csv', delimiter=','))
hdx = np.array([i for i in range(len(hdg))])
htg = np.array(genfromtxt('hg_triple_green.csv', delimiter=','))
htgx = np.array([i for i in range(len(bdg))])
htp = np.array(genfromtxt('hg_triple_polarizer.csv', delimiter=','))
htpx = np.array([i for i in range(len(bdg))])
ht = np.array(genfromtxt('hg_triple.csv', delimiter=','))
htx = np.array([i for i in range(len(bdg))])

ldg = np.array(genfromtxt('laser_double_green.csv', delimiter=','))
ldgx = np.array([i for i in range(len(ldg))])
ldp = np.array(genfromtxt('laser_double_polarizer.csv', delimiter=','))
ldpx = np.array([i for i in range(len(ldg))])
ld = np.array(genfromtxt('laser_double.csv', delimiter=','))
ldx = np.array([i for i in range(len(ldg))])
ltg = np.array(genfromtxt('laser_triple_green.csv', delimiter=','))
ltgx = np.array([i for i in range(len(bdg))])
ltp = np.array(genfromtxt('laser_triple_polarizer.csv', delimiter=','))
ltpx = np.array([i for i in range(len(bdg))])
lt = np.array(genfromtxt('laser_triple.csv', delimiter=','))
ltx = np.array([i for i in range(len(bdg))])


# plt.plot(bdgx, bdg, 'r')
# plt.show()   


# print bdg[0]
# laserf = np.array(dslit["laserF(nV)"])


# be = np.pi/0.67 # unit in um
# pk = 194.-15.

# def det(z):
#     return (z-2.25)/500.# np.sin(np.arctan((z-2.25)/500.))

# def sslit(x, d, b, p):
#     return p*(np.sin(be*b*((x-d)/500.)))**2/(be*b*((x-d)/500.))**2
# ssf, sof = curve_fit(sslit, xx, righf, p0=[1.65,100.,47.])
# print ssf

# # sin(theta) ~ theta ~ x
# def dos(x, b, d, c):
#     return pk*(np.cos(be*d*(det(x)))**2)*(np.sin(be*b*(det(x))))**2/(be*b*(det(x)))**2+15.
# paf, pof = curve_fit(dos, xx, laserf, p0=[100.,450.,15.])
# pal, pol = curve_fit(dos, xx, laserl, p0=[100.,450.,15.])
# print paf

import plotly.plotly as py
from plotly.graph_objs import *


pkk=19000.
ofs=364.5
def paco(x,j,b,d,p,t):
    return p/2.*(1+j*np.cos(2*(x-ofs)*d))*(np.sin((x-ofs)*b))**2/(b*(x-ofs))**2+t
# opf, poo = curve_fit(paco, bdgx, bdg, p0=[0.8,0.008,0.03,18500.,1000.])
# print opf

import scipy.odr as odrr
def paco(p,x):
    return p[3]/2.*(1+p[0]*np.cos(2*(x-ofs)*p[2]))*\
           (np.sin((x-ofs)*p[1]))**2/(p[1]*(x-ofs))**2+p[4]
md = odrr.Model(paco)
opf = odrr.RealData(bdgx, bdg, sy=[50. for i in range(len(bdg))])
opr = odrr.ODR(opf, md, beta0=[0.8,0.008,0.03,18500.,1000.])

# opr.run().pprint()
# plt.plot(bdgx, [paco([0.99975,0.0076892,0.028753,18895.93,410.62],bdgx[i]) for i in range(len(bdgx))], 'b')
# plt.show()

# datao = Scatter(
#     x=ox,
#     y=opav,
#     mode='lines',
#     line=Line(
#         color='blue',
#         width=1
#     ),
#     error_y=ErrorY(
#         type='data',
#         array=opsd,
#         visible=True
#     ),
# )
# tt = np.linspace(min(ox),max(ox),100)
# ttt = Scatter(
#     x=tt,
#     y=[paco(tt[i],356.,0.5,100.,50.) for i in range(len(tt))],
#     mode='lines',
#     line=Line(
#         color='red',
#         width=1,
#         dash='dash',
#     ),
# )
# fito = Scatter(
#     x=ox,
#     y=[paco(ox[i],opf[0],opf[1],opf[2],opf[3]) for i in range(len(ox))],
#     mode='lines',
#     line=Line(
#         color='green',
#         width=1,
#         dash='solid',
#     ),
# )
# tttt = Data([datao,fito,ttt])
# layout = Layout(title='test')
# pt = Figure(data=tttt, layout=layout)
# py.plot(pt,filename='test',fileopt='new')  


