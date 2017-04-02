
# coding: utf-8

# In[6]:

import pandas as p
obj = p.Series([1.2, 3.4, 5.6, 7.1], index=(range(4)))
obj.reindex(range(1,5), fill_value=1.1)


# In[18]:

obj3 =p.Series(['Red', 'Blue', 'Purple'], index=([1, 3, 6]))
obj3.reindex(range(0,8), method='ffill')


# In[24]:

obj3.reindex(range(0,7), method='bfill')


# In[39]:

import numpy as np
frame =p.DataFrame(np.arange(4).reshape((2, 2)), index=(['a', 'c']), columns=(['Cali', 'Ohio']))
frame.reindex(['a', 'c', 'd'])
st = ['Cali', 'Nc', 'Ohio']
frame.reindex(columns=(st), index=(['a', 'c', 'd']), method='ffill')


# In[42]:

frame


# In[43]:

frame.ix[['a', 'c', 'd'], st]


# In[ ]:



