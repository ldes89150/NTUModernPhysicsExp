import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
dslit = pd.read_csv("laser.csv")
opdst = pd.read_csv("single photon.csv")

xx = np.array(dslit["x(mm)"])
ox = np.array(opdst["xx"])

laserf = np.array(dslit["laserF(nV)"])
laserl = np.array(dslit["laserB(nV)"])
leftf = np.array(dslit["leftF(nV)"])
righf = np.array(dslit["right"])

opav = np.array(opdst["avg"])
opsd = np.array(opdst["std"])

be = np.pi/0.67 # unit in um
pk = 194.-15.

def det(z):
    return (z-2.25)/500.# np.sin(np.arctan((z-2.25)/500.))

def sslit(x, d, b, p):
    return p*(np.sin(be*b*((x-d)/500.)))**2/(be*b*((x-d)/500.))**2
ssf, sof = curve_fit(sslit, xx, righf, p0=[1.65,100.,47.])
print ssf

# sin(theta) ~ theta ~ x
def dos(x, b, d, c):
    return pk*(np.cos(be*d*(det(x)))**2)*(np.sin(be*b*(det(x))))**2/(be*b*(det(x)))**2+15.
paf, pof = curve_fit(dos, xx, laserf, p0=[100.,450.,15.])
pal, pol = curve_fit(dos, xx, laserl, p0=[100.,450.,15.])
print paf

import plotly.plotly as py
from plotly.graph_objs import *
dataf = Scatter(
    x=xx,
    y=laserf,
    mode='lines',
    line=Line(
        color='blue',
        width=1
    ),
)
rf = Scatter(
    x=xx,
    y=righf,
    mode='lines',
    line=Line(
        color='black',
        width=1
    ),
)
lf = Scatter(
    x=xx,
    y=leftf,
    mode='lines',
    line=Line(
        color='black',
        width=1
    ),
)
tx = np.linspace(min(xx),max(xx),100)
thef = Scatter(
    x=tx,
    y=[dos(tx[i],100.,457.,15.) for i in range(len(tx))],
    mode='lines',
    line=Line(
        color='red',
        width=1,
        dash='dash',
    ),
)
fitf = Scatter(
    x=xx,
    y=[dos(xx[i],paf[0],paf[1],15.) for i in range(len(xx))],
    mode='lines',
    line=Line(
        color='green',
        width=1,
        dash='solid',
    ),
)
# lafgo = Data([dataf,thef,fitf,rf,lf])
# layout = Layout(title='LaserF')
# lafpt = Figure(data=lafgo, layout=layout)
# py.plot(lafpt,filename='LaserF', fileopt='new')

datal = Scatter(
    x=xx,
    y=laserl,
    mode='lines',
    line=Line(
        color='blue',
        width=1
    ),
)
tx = np.linspace(min(xx),max(xx),100)
thel = Scatter(
    x=tx,
    y=[dos(tx[i],100.,457.,15.) for i in range(len(tx))],
    mode='lines',
    line=Line(
        color='red',
        width=1,
        dash='dash',
    ),
)
fitl = Scatter(
    x=xx,
    y=[dos(xx[i],pal[0],pal[1],15.) for i in range(len(xx))],
    mode='lines',
    line=Line(
        color='green',
        width=1,
        dash='solid',
    ),
)
# lalgo = Data([datal,thel,fitl])
# layout = Layout(title='LaserL')
# lalpt = Figure(data=lalgo, layout=layout)
# py.plot(lalpt,filename='LaserL', fileopt='new')
bee = np.pi/0.46
pkk=520.
def dee(z):
    return (z-2.85)/500.# np.sin(np.arctan((z-2.85)/500.))
def paco(x,d,j,b,t):
    return pkk/2.*(1+j*np.cos(2*bee*d*(dee(x))))*(np.sin(bee*b*(dee(x))))**2/(bee*b*(dee(x)))**2+t
opf, poo = curve_fit(paco, ox, opav, p0=[350.,0.5,100.,100.])
print opf
datao = Scatter(
    x=ox,
    y=opav,
    mode='lines',
    line=Line(
        color='blue',
        width=1
    ),
    error_y=ErrorY(
        type='data',
        array=opsd,
        visible=True
    ),
)
tt = np.linspace(min(ox),max(ox),100)
ttt = Scatter(
    x=tt,
    y=[paco(tt[i],356.,0.5,100.,50.) for i in range(len(tt))],
    mode='lines',
    line=Line(
        color='red',
        width=1,
        dash='dash',
    ),
)
fito = Scatter(
    x=ox,
    y=[paco(ox[i],opf[0],opf[1],opf[2],opf[3]) for i in range(len(ox))],
    mode='lines',
    line=Line(
        color='green',
        width=1,
        dash='solid',
    ),
)
tttt = Data([datao,fito,ttt])
layout = Layout(title='test')
pt = Figure(data=tttt, layout=layout)
py.plot(pt,filename='test',fileopt='new')

