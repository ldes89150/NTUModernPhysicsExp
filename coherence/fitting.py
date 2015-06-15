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
hdx = np.array([i for i in range(len(hd))])
htg = np.array(genfromtxt('hg_triple_green.csv', delimiter=','))
htgx = np.array([i for i in range(len(htg))])
htp = np.array(genfromtxt('hg_triple_polarizer.csv', delimiter=','))
htpx = np.array([i for i in range(len(htp))])
ht = np.array(genfromtxt('hg_triple.csv', delimiter=','))
htx = np.array([i for i in range(len(ht))])

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


plt.plot(btgx, btg, 'r')
plt.show()
import plotly.plotly as py
from plotly.graph_objs import *



# def paco(x,j,b,d,p,t):
#     return p/2.*(1+j*np.cos(2*(x-ofs)*d))*(np.sin((x-ofs)*b))**2/(b*(x-ofs))**2+t
# opf, poo = curve_fit(paco, bdgx, bdg, p0=[0.8,0.008,0.03,18500.,1000.])
# print opf

import scipy.odr as odrr
def paco(p,x):
    return p[3]/2.*(1+p[0]*np.cos(2*(x-ofs)*p[2]))*\
           (np.sin((x-ofs)*p[1]))**2/(p[1]*(x-ofs))**2
md = odrr.Model(paco)

#######l
##ldg
# ofs=364.5

# opf = odrr.RealData(ldgx, ldg)
# opr = odrr.ODR(opf, md, beta0=[0.8,0.008,0.03,17000.,0.])

# opr.run()
# print opr.output.beta
# plt.plot(ldgx, [paco(opr.output.beta,ldgx[i]) for i in range(len(ldgx))], 'b')
# plt.show()

##ldp
# ofs=363.

# opf = odrr.RealData(ldpx, ldp)
# opr = odrr.ODR(opf, md, beta0=[0.93,0.0075,0.0288,23000.])
# plt.plot(ldpx, [paco([0.93,0.0075,0.0288,23000.],ldpx[i]) for i in range(len(ldpx))], 'b') 

# opr.run().pprint()
# plt.plot(ldpx, [paco(opr.output.beta,ldpx[i]) for i in range(len(ldpx))], 'b')
# plt.show() 


# ##ld
# ofs=363.

# opf = odrr.RealData(ldx, ld)
# beta=[0.96,0.0071,0.028]
# opr = odrr.ODR(opf, md, beta0=beta)

# opr.run().pprint()
# plt.plot(ldx, [paco(beta,ldx[i]) for i in range(len(ldx))], 'b')
# plt.plot(ldx, [paco(opr.output.beta,ldx[i]) for i in range(len(ldx))], 'b')
# plt.show()


#######hg
##hdg
# ofs=406.5

# opf = odrr.RealData(hdgx, hdg)
# beta=[0.6,0.0074,0.032,3800.]
# opr = odrr.ODR(opf, md, beta0=beta)

# opr.run().pprint()
# #plt.plot(ldx, [paco(beta,ldx[i]) for i in range(len(ldx))], 'k')
# plt.plot(hdgx, [paco(opr.output.beta,hdgx[i]) for i in range(len(hdgx))], 'b')
# plt.show()

##hd
# ofs=406.5

# opf = odrr.RealData(hdx, hd)
# beta=[0.6,0.008,0.032,10000.]
# opr = odrr.ODR(opf, md, beta0=beta)

# opr.run().pprint()
# # plt.plot(ldx, [paco(beta,ldx[i]) for i in range(len(ldx))], 'k')
# plt.plot(hdx, [paco(opr.output.beta,hdx[i]) for i in range(len(hdx))], 'b')
# plt.show()

##hdp
# ofs=411.3

# opf = odrr.RealData(hdpx, hdp)
# beta=[0.58,0.0081,0.032,4000.]
# opr = odrr.ODR(opf, md, beta0=beta)

# opr.run().pprint()
# # plt.plot(ldx, [paco(beta,hdpx[i]) for i in range(len(ldx))], 'k')
# plt.plot(hdpx, [paco(opr.output.beta,hdpx[i]) for i in range(len(hdpx))], 'b')
# plt.show()

#######b
##bdg
# ofs=375.8

# beta=[0.72,0.00755,0.0315,27000.]
# opf = odrr.RealData(bdgx, bdg)
# opr = odrr.ODR(opf, md, beta0=beta)

# opr.run().pprint()
# # plt.plot(ldx, [paco(beta,hdpx[i]) for i in range(len(bdgx))], 'k')
# plt.plot(bdgx, [paco(opr.output.beta,bdgx[i]) for i in range(len(bdgx))], 'b')
# plt.show()

##bd
# ofs=377.4

# opf = odrr.RealData(bdx, bd)
# beta=[0.79,0.00725,0.0295,46000.]
# opr = odrr.ODR(opf, md, beta0=beta)

# opr.run().pprint()
# #plt.plot(ldx, [paco(beta,hdpx[i]) for i in range(len(bdx))], 'k')
# plt.plot(bdx, [paco(opr.output.beta,bdx[i]) for i in range(len(bdx))], 'b')
# plt.show()

##bdp
# ofs=377.4

# opf = odrr.RealData(bdpx, bdp)
# beta=[0.79,0.0073,0.0275,28000.]

# opr = odrr.ODR(opf, md, beta0=beta)

# opr.run().pprint()
# #plt.plot(ldx, [paco(beta,hdpx[i]) for i in range(len(bdpx))], 'k')

# plt.plot(bdpx, [paco(opr.output.beta,bdpx[i]) for i in range(len(bdpx))], 'b')
# plt.show()

###################################
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


