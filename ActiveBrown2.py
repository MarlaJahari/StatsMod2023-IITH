#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
delta=0.001
zeta=1
Nt=1000
B_var0=0.2

iloop=1
B_var=B_var0*iloop
DT=B_var0/zeta
Dr=1000
v00=0.001
v0=v00
Np=1
Nloop=1
for iloop in range(Nloop):
    v0=v00*10*iloop
for ip in range(Np):
    fx=np.random.randn(Nt,1)*np.sqrt(DT*2.0)
    fy=np.random.randn(Nt,1)*np.sqrt(DT*2.0)
    fth=np.random.randn(Nt,1)*np.sqrt(Dr*2.0)
#initialize 


# In[7]:


import numpy as np
import matplotlib.pyplot as plt

Nt = 1000
delta = 0.001
zeta = 1
B_var0 = 0.000
B_var = B_var0
DT = B_var0 / zeta
Dr = 10.00
v00 = 0.0001
v0 = v00
Np = 5
Nloop = 1

for iloop in range(1, Nloop + 1):
    v0 = v00 * 10 ** iloop
for ip in range(1, Np + 1):
    fx = np.random.randn(Nt) * np.sqrt(DT * 2.0)
    fy = np.random.randn(Nt) * np.sqrt(DT * 2.0)
    fth = np.random.randn(Nt) * np.sqrt(Dr * 2.0)
        
x0 = 0.0
y0 = 0.0
th0 = np.random.rand() * 2 * np.pi
xx = np.zeros(Nt + 1)
yy = np.zeros(Nt + 1)
th = np.zeros(Nt + 1)
xx[0] = x0
yy[0] = x0
th[0] = th0
        
for it in range(1, Nt + 1):
    xx[it] = xx[it-1] + np.sqrt(delta) * fx[it-1] + delta * v0 * np.cos(th[it-1])
    yy[it] = yy[it-1] + np.sqrt(delta) * fy[it-1] + delta * v0 * np.sin(th[it-1])
    th[it] = th[it-1] + np.sqrt(delta) * fth[it-1]
            
    xxd = (xx - xx[0])[:Nt]
    yyd = (yy - yy[0])[:Nt]
        
plt.figure(iloop)
plt.plot(xx, yy)
#plt.hold(True)
        
plt.show()


# In[6]:


plt.figure(iloop)
plt.plot(xx, yy)


# In[19]:


import numpy as np
import matplotlib.pyplot as plt

Nt = 100000
delta = 0.01
zeta = 1
B_var0 = 0.000
B_var = B_var0
DT = B_var0 / zeta
Dr = 10.00
v00 = 0.0001
v0 = v00
Np = 5
Nloop = 1

for iloop in range(1, Nloop + 1):
    v0 = v00 * 10 ** iloop
    for ip in range(1, Np + 1):
        fx = np.random.randn(Nt) * np.sqrt(DT * 2.0)
        fy = np.random.randn(Nt) * np.sqrt(DT * 2.0)
        fth = np.random.randn(Nt) * np.sqrt(Dr * 2.0)
        
        x0 = 0.0
        y0 = 0.0
        th0 = np.random.rand() * 2 * np.pi
        xx = np.zeros(Nt + 1)
        yy = np.zeros(Nt + 1)
        th = np.zeros(Nt + 1)
        xx[0] = x0
        yy[0] = x0
        th[0] = th0
        
        for it in range(1, Nt + 1):
            xx[it] = xx[it-1] + np.sqrt(delta) * fx[it-1] + delta * v0 * np.cos(th[it-1])
            yy[it] = yy[it-1] + np.sqrt(delta) * fy[it-1] + delta * v0 * np.sin(th[it-1])
            th[it] = th[it-1] + np.sqrt(delta) * fth[it-1]
            
        xxd = (xx - xx[0])[:Nt]
        yyd = (yy - yy[0])[:Nt]
        
        plt.figure(iloop)
        plt.plot(xx, yy)
        
plt.show()


# In[116]:


import numpy as np
import matplotlib.pyplot as plt

Nt = 1000
delta = 0.001
zeta = 1
B_var0 = 0.000
B_var = B_var0
DT = B_var0 / zeta
Dr = 10.00
v00 = 0.001
v0 = v00
Np = 100
Nloop = 1

for iloop in range(1, Nloop + 1):
    v0 = v00 * 10 ** iloop
    for ip in range(1, Np + 1):
        fx = np.random.randn(Nt) * np.sqrt(DT * 2.0)
        fy = np.random.randn(Nt) * np.sqrt(DT * 2.0)
        fth = np.random.randn(Nt) * np.sqrt(Dr * 2.0)
        
        x0 = 0.0
        y0 = 0.0
        th0 = np.random.rand() * 2 * np.pi
        xx = np.zeros(Nt + 1)
        yy = np.zeros(Nt + 1)
        th = np.zeros(Nt + 1)
        xx[0] = x0
        yy[0] = x0
        th[0] = th0
        
        xxd = np.zeros((Nt, Np))
        yyd = np.zeros((Nt, Np))
        
        for it in range(1, Nt + 1):
            xx[it] = xx[it-1] + np.sqrt(delta) * fx[it-1] + delta * v0 * np.cos(th[it-1])
            yy[it] = yy[it-1] + np.sqrt(delta) * fy[it-1] + delta * v0 * np.sin(th[it-1])
            th[it] = th[it-1] + np.sqrt(delta) * fth[it-1]
            
            xxd[it-1, ip-1] = (xx[it] - xx[0])
            yyd[it-1, ip-1] = (yy[it] - yy[0])
        
        plt.figure(iloop)
        plt.plot(xx, yy)
        
plt.show()


# In[117]:


#ori_data.dropna(inplace=True)

nmin=5
nmax=50
rr2=xxd**2+yyd**2
rr2_m=np.mean(rr2,axis=1)

tt_m = delta * (np.arange(1, len(rr2_m)+1)) - delta

plt.plot(np.log10(tt_m), np.log10(rr2_m), 'k')
plt.plot(np.log10(tt_m), 2*np.log10(tt_m) + 0.5, 'b--')
plt.plot(np.log10(tt_m), np.log10(tt_m) + 0.5, 'r--')

tt1 = tt_m[nmin-1:nmax]
rr1 = rr2_m[nmin-1:nmax]
tt2 = tt_m[int(Nt/5)-1:Nt]
rr2 = rr2_m[int(Nt/5)-1:Nt]
plt.plot(np.log10(tt1),np.log10(rr1),'bo')


plt.plot(np.log10(tt2), np.log10(rr2), 'ro')
plt.show()

cc2 = np.polyfit(np.log10(tt2), np.log10(rr2), 1)
DD = 10 ** cc2[1] / 2
vv = np.sqrt(10 ** cc2[1])
print(DD)







# In[61]:


import numpy as np
import matplotlib.pyplot as plt

Nt = 1000
delta = 0.01
zeta = 1
B_var0 = 0.1000
B_var = B_var0
DT = B_var0 / zeta
Dr = 10.00
v00 = 0.0001
Np = 5
Nloop = 1

for iloop in range(1, Nloop + 1):
    v0 = v00 * 10 ** iloop
    for ip in range(1, Np + 1):
        fx = np.random.randn(Nt) * np.sqrt(DT * 2.0)
        fy = np.random.randn(Nt) * np.sqrt(DT * 2.0)
        fth = np.random.randn(Nt) * np.sqrt(Dr * 2.0)
        
        x0 = 0.0
        y0 = 0.0
        th0 = np.random.rand() * 2 * np.pi
        xx = np.zeros(Nt + 1)
        yy = np.zeros(Nt + 1)
        th = np.zeros(Nt + 1)
        xx[0] = x0
        yy[0] = x0
        th[0] = th0
        
        for it in range(1, Nt + 1):
            xx[it] = xx[it-1] + np.sqrt(delta) * fx[it-1] + delta * v0 * np.cos(th[it-1])
            yy[it] = yy[it-1] + np.sqrt(delta) * fy[it-1] + delta * v0 * np.sin(th[it-1])
            
        xxd = (xx - xx[0])[:Nt]
        yyd = (yy - yy[0])[:Nt]
        
        plt.figure(iloop)
        plt.plot(xx, yy)
        
plt.show()


# In[42]:


rr2=xxd**2+yyd**2
print(xxd.shape)
rr2_m=np.mean(rr2)
print(rr2)
result = delta * np.arange(1, (rr2_m.shape[0]) + 1)
print(rr2)


# In[ ]:




