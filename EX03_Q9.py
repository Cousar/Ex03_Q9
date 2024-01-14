#!/usr/bin/env python
# coding: utf-8

# In[26]:


import numpy as np
import requests
from io import StringIO

import matplotlib.pyplot as plt

github_url = 'https://raw.githubusercontent.com/xaratustrah/teach/main/appacc2324/2016-07-11_ipm_data.txt'

response = requests.get(github_url)

data = np.genfromtxt(StringIO(response.text), dtype=float)

x = np.arange(len(data)).reshape(len(data), 1)

max_value = np.max(data)
max_index = np.argmax(data)


fig, ax = plt.subplots(figsize=(14, 10))
fig.patch.set_facecolor('black')  


ax.plot(x, data, color='blue', label='Data') 


ax.set_facecolor('black') 


ax.scatter(max_index, max_value, color='red', label='Max Value')


ax.set_xlabel('Index', color='white')
ax.set_ylabel('Value', color='white')
ax.set_title('Matrix Plot with Max Value Highlighted', color='white')


ax.tick_params(axis='both', colors='white')
ax.legend()
plt.show()


# In[ ]:




