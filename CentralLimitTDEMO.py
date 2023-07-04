#!/usr/bin/env python
# coding: utf-8

# # Demonstration of Central Limit Theorem
# 
# Suppose you draw random samples of size $n$ from some population which is not necessarily normally distributed.
# From these samples you calculate the sample means.
# Then for large enough values of $n$ the sample means will tend to approximate normal distribution as $n$ increases in size.
# The mean value of this distribution of sample means coincides with that of the population mean and variance is given by
#     \begin{equation*}
#         \sigma_{\bar{x}}^2 = \frac{\sigma^2}{n}
#     \end{equation*}
# where $\sigma^2$ is the population variance and $n$ is the sample size.
# 
# In order to see this result in action, please click the play button on the left side of the python code below.
# Change the values of sample size to see its effect.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# population
N = int(input("Enter size of population:"))#10000 # This is the size of the population

population1 = np.random.uniform(size=N,low=-1.5,high=5.5) # This population is  uniformly distributed
population2 = np.random.gamma(size=N,shape=1,scale=2) # This population follows  gamma distribution
population3 = np.random.normal(size=N,loc=2,scale=2) # This population follows  normal distribution

print('Here distributions are chosen with almost similar mean values and variances')
print("Population mean of first: ",np.mean(population1))
print("Population variance of first: ",np.var(population1))
print('----------------------------------')
print("Population mean of second: ",np.mean(population2))
print("Population variance of second: ",np.var(population2))
print('----------------------------------')
print("Population mean of third: ",np.mean(population3))
print("Population variance of third: ",np.var(population3))


f,ax = plt.subplots(nrows=2,ncols=3,figsize=(15,10))
o1 = ax[0,0].hist(population1,bins=20)
o2 = ax[0,1].hist(population2,bins=20)
o3 = ax[0,2].hist(population3,bins=20)

print('----------------------------------')

sampleSize = 3
numberOfSamples = 10000

population = np.vstack((population1,population2,population3))
for i in range(3):
  means = np.zeros(numberOfSamples)
  for j in range(numberOfSamples):
    sample = np.random.choice(population[i,:], size=sampleSize)
    means[j] = np.mean(sample)

  print('Mean of sample means for population'+str(i+1)+': ',np.mean(means))
  print('Variance of sample means for population'+str(i+1)+': ',np.var(means))
  print('Population variance/n for population'+str(i+1)+': ',np.var(population[i,:])/sampleSize)
  print('----------------------------------')
  out = ax[1,i].hist(means,bins=15)
# plt.xlim([3,5])
print('The first row in the following plot shows population distribution')
print('The second row in the following plot shows the distribution of sample means')


# In[ ]:





# In[ ]:




