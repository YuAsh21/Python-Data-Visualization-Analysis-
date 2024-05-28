#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import style


# In[2]:


#results = pd.read_csv('3compC.csv')
#results
chunk_size = 12
batch_no = 1
for chunk in pd.read_csv('3comp.csv', chunksize=chunk_size):
    chunk.to_csv('3comp_{}.csv'.format(batch_no), index=False)
    batch_no += 1
results1 = pd.read_csv('3comp_1.csv')
results2 = pd.read_csv('3comp_2.csv')
#results3 = pd.read_csv('VVC-p_3.csv')
#results4 = pd.read_csv('VVC-p_4.csv')


# In[3]:



fig, ax = plt.subplots()



df = pd.DataFrame(results1, 
                  columns = ['Video Sequence', 'Precision', 'Recall', 'F1'])


ax = df.plot.bar(rot=90, ax=ax, x="Video Sequence", y=["Precision", "Recall", "F1"], 
                 width = 0.8, figsize=(10,5) )

'''for p in ax.patches[0:]:
    h = p.get_height()
    x = p.get_x()+p.get_width()/2.
    if h != 0:
        ax.annotate("%g" % p.get_height(), xy=(x,h), xytext=(0,-80), rotation=90, 
                   textcoords="offset points", ha="center", va="bottom")'''
plt.xlabel('Video Sequences')
plt.ylabel('Value')

for c in ax.containers:

    # annotate the container group
    ax.bar_label(c, label_type='center', rotation=90)

plt.title('Results for proposed methods in VVC')
plt.legend(loc=(1,.5))
plt.tight_layout()


plt.savefig('3comp-p1.png')
plt.savefig('3comp-p1.pdf')


plt.show()


# In[4]:


fig, ax = plt.subplots()



df = pd.DataFrame(results2, 
                  columns = ['Video Sequence', 'Precision', 'Recall', 'F1'])


ax = df.plot.bar(rot=90, ax=ax, x="Video Sequence", y=["Precision", "Recall", "F1"], 
                 width = 0.8, figsize=(10,5))

'''for p in ax.patches[0:]:
    h = p.get_height()
    x = p.get_x()+p.get_width()/2.
    if h != 0:
        ax.annotate("%g" % p.get_height(), xy=(x,h), xytext=(0,2), rotation=90, 
                   textcoords="offset points", ha="center", va="bottom")'''
plt.xlabel('Video Sequences')
plt.ylabel('Value')
for c in ax.containers:

    # annotate the container group
    ax.bar_label(c, label_type='center', rotation=90)

plt.title('Results for proposed methods in VVC')
plt.legend(loc=(1,.5))
plt.tight_layout()

plt.savefig('3comp-p2.png')
plt.savefig('3comp-p2.pdf')


plt.show()


# In[5]:


#results2 = pd.read_csv('PD-NC.csv',skiprows = 12, nrows=24)
#results2


# In[6]:


"'fig, ax = plt.subplots()



df = pd.DataFrame(results3, 
                  columns = ['Video Sequence', 'Precision', 'Recall', 'F1', 'Accuracy'])


ax = df.plot.bar(rot=90, ax=ax, x="Video Sequence", y=["Precision", "Recall", "F1", "Accuracy"], 
                 width = 0.8, figsize=(10,5))

'''for p in ax.patches[0:]:
    h = p.get_height()
    x = p.get_x()+p.get_width()/2.
    if h != 0:
        ax.annotate("%g" % p.get_height(), xy=(x,h), xytext=(0,2), rotation=90, 
                   textcoords="offset points", ha="center", va="bottom")'''
plt.xlabel('Video Sequences')
plt.ylabel('Value')
for c in ax.containers:

    # annotate the container group
    ax.bar_label(c, label_type='center', rotation=90)

plt.title('Results for proposed methods in VVC')
plt.legend(loc=(1,.5))
plt.tight_layout()

plt.savefig('VVC-p3.png')
plt.savefig('VVC-p3.pdf')


plt.show()


# In[ ]:


fig, ax = plt.subplots()



df = pd.DataFrame(results4, 
                  columns = ['Video Sequence', 'Precision', 'Recall', 'F1', 'Accuracy'])


ax = df.plot.bar(rot=90, ax=ax, x="Video Sequence", y=["Precision", "Recall", "F1","Accuracy"], 
                 width = 0.8, figsize=(10,5))

plt.xlabel('Video Sequences')
plt.ylabel('Value')
for c in ax.containers:

    # annotate the container group
    ax.bar_label(c, label_type='center', rotation=90)

plt.title('Results for proposed methods in VVC')
plt.legend(loc=(1,.5))
plt.tight_layout()

plt.savefig('VVC-p4.png')
plt.savefig('VVC-p4.pdf')


plt.show()


# In[ ]:




