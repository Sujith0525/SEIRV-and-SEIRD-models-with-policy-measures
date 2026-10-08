#!/usr/bin/env python
# coding: utf-8

# In[327]:


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#sigma # Rate of becoming infections after contact with the exposed(unit in [day]**-1)
#gamma # Rate of either dying or recovering(unit in [day]**-1) 
#beta # Attack(contact) rate, those who can infect others(unit [day]**-1[person]**-1)
#f # fatality rate,f% of infected people will die and (1-f)% will survive(recovered)    

u = 0.5 # social distancing (0-1)
         # 0   = no social distancing
         # 0.1 = masks
         # 0.2 = masks and hybrid classes
         # 0.3 = masks, hybrid, and online classes

f = 0.0066  #fatality rate due to COVID19

t_incubation = 3.2
t_infectivity = 8.5
R0 = 2  # reproductive number 
N = 21919000 # Population

#initial number of infected and recovered individuals
e0 = 1
i0 = 0
r0 = 0
d0 = 0
s0 = N - e0 - i0 - r0 - d0
x0 = [s0,e0,i0,r0,d0]

sigma = 1./t_incubation  # latent period 
gamma = 1./t_infectivity  # avg infection period 
beta  = R0 * gamma
#infection death period (days from infection to death)
n = 1/21

# sigma = 1/3.2   #t_incubation   # latent period 
# gamma = 0.82   #1./t_infectivity # avg infection period 
# beta = 0.0059     #R0 * gamma
# #infection death period (days from infection to death)
# f = 1/22

def covid(x,t):
    s,e,i,r,d = x
    dx = np.zeros(5)
    dx[0] = -(1-u*0.3) * beta * i * s/N
    dx[1] = (1-u*0.3) * beta * i * s/N - sigma * e
    dx[2] = sigma * e - (1-f) * gamma * i - f * n * i 
    dx[3] = (1-f) * gamma * i
    dx[4] = f * n * i
    return dx;

t = np.linspace(0, 500, 251)
x = odeint(covid,x0,t)
s = x[:,0]; e = x[:,1]; i = x[:,2]; r = x[:,3]; d = x[:,4]

# plot the data
plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.title('Closure = '+str(u*100)+'%')
plt.plot(t,s, color='blue', lw=2, label='Susceptible')
plt.plot(t,r, color='green',  lw=2, label='Recovered')
plt.plot(t,i, color='orange', lw=2, label='Infectivity')
plt.plot(t,e, color='purple', lw=2, label='Exposed')
#plt.ylabel('Fraction')
plt.legend()

plt.subplot(2,1,2)
plt.plot(t,d, color='red', lw=2, label='Dead')
#plt.ylim(0, 0.05)
plt.ylabel('Population')
plt.xlabel('Time (days)')
#plt.ylabel('Fraction')
plt.grid(True)
plt.legend()

plt.show()


# In[324]:


result = max(d)
print("The maximum number is:", result)


# In[325]:


result = max(i)
print("The maximum number is:", result)


# In[326]:


result = max(e)
print("The maximum number is:", result)


# In[138]:


def beta(t):
    return R0(t) * gamma


# In[141]:


print(R0* gamma)


# In[ ]:




