#!/usr/bin/env python
# coding: utf-8

# In[140]:


import pandas as pd
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#vaccination coverage (0.1, 0.5, 0.8)
#a = 0.5
#vaccine efficacy  (0.4, 0.6, 0.8)
b = 0.6
#vaccination rate (0.01, 0.02, 0.05)
neta = 0.05

#vaccination coefficient
mu = b*neta

t_incubation = 3.2
t_infectivity = 8.5
# reproductive number (2, 4, 6, 8)
R0 = 4
# Population
N = 21919000

# initial number of infected and recovered individuals
e0 = 1
i0 = 0
r0 = 0
v0 = 0
s0 = N - e0 - i0 - r0 - v0
x0 = [s0,e0,i0,r0,v0]

# aborgation of infectivity as the susceptible fraction falls 
alpha = 1.2 
# latent period 
sigma = 1./t_incubation   
gamma = 1/t_infectivity
beta = R0*gamma
#time to reproductive immunity after vaccination 
c = 1./14    

def covid(x,t):
    s,e,i,r,v = x
    dx = np.zeros(5)
    dx[0] = -beta * i * (s/N) -  mu * s
    dx[1] = beta * i * (s/N) + beta * i * (v/N) - sigma * e
    dx[2] = sigma * e - gamma * i
    dx[3] = gamma * i + c * v
    dx[4] = mu * s - beta * i * (v/N) - c * v
    return dx;

t = np.linspace(0, 200, 101)
x = odeint(covid,x0,t)
s = x[:,0]; e = x[:,1]; i = x[:,2]; r = x[:,3]; v = x[:,4]

# plot the data
plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.title('Vaccination Coefficient = '+str(mu))
plt.plot(t,s, color='blue', lw=2, label='Susceptible')
plt.plot(t,r, color='red',  lw=2, label='Recovered')
plt.plot(t,i, color='orange', lw=2, label='Infectivity')
plt.plot(t,e, color='purple', lw=2, label='Exposed')
plt.legend()

plt.subplot(2,1,2)
plt.plot(t,v, color='green', lw=2, label='Vaccinated')
plt.xlabel('Time (days)')
plt.ylabel('Population')
plt.grid(True)
plt.legend()

plt.show()


# In[141]:


result = max(v)
print("The maximum number is:", result)


# In[142]:


result = max(i)
print("The maximum number is:", result)


# In[139]:


result = max(e)
print("The maximum number is:", result)


# In[ ]:




