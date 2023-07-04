#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np

for i in range(10, )
a=np.random.rand(100)
c=np.random.rand(1000)
b=np.mean(c)
print(b)


# In[43]:


import matplotlib.pyplot as plt
delta=  0.001
zeta=0.1
Nt= 1000
B_var=0.1
fx=np.random.randn(Nt)*B_var/np.sqrt(zeta)
fy=np.random.randn(Nt)*B_var/np.sqrt(zeta)
xx=np.zeros(Nt)
yy=np.zeros(Nt)
for i in range(Nt):
    xx[i]=xx[i-1]+delta*fx[i-1]
    yy[i]=yy[i-1]+delta*fy[i-1]

plt.plot(fx[1:100],fy[1:100])
plt.plot(xx[1:100],yy[1:100])


# In[44]:


plt.plot(xx[1:100],yy[1:100])


# In[88]:


tlength=200
Nsample=5
xx2=np.zeros((tlength,Nsample-1))
yy2=np.zeros((tlength,Nsample-1))

for isample in range(Nsample-1):
       for itt in range(tlength):
        for it in range(Nt-tlength):
         xx2[itt,isample]=(xx[tlength*isample+itt]-xx[tlength*isample])**2
         yy2[itt,isample]=(yy[tlength*isample+itt]-yy[tlength*isample])**2
        #print((xx[it+itt-1]-xx[it-1])**2)     
xx2m=np.mean(xx2,1)
yy2m=np.mean(yy2,1)
a=(np.arange(1, len(xx2)+1))
print(np.shape(a))
plt.loglog(delta*a,xx2)


# In[68]:


#plt.plot(np.log(np.log(xx2)))
         #,yy2)


# In[ ]:





# In[ ]:




