#!/usr/bin/env python
# coding: utf-8

# In[13]:


import re
import numpy
import pandas as pd
from numpy import dot
from numpy.linalg import norm


# In[14]:


file = open("sentences.txt", "r")
sentences = []
for line in file:
    sentences.append(line.strip().lower())


# In[15]:


words = {}
a = 0
index = 0
sent = sentences.copy()
for line in sent:
    line = re.split('[^a-z]', line)
    sent[a] = line
    a+=1
    for x in line:
        if x not in words and x!='':
            words[x] = index
            index+=1


# In[17]:


num_words = len(words)
num_sentence = len(sentences)
matrix = numpy.zeros((num_sentence, num_words))
for i in range(num_sentence):
    sen_w = sent[i]
    for x in sen_w:
        if x!='':
            matrix[i][words[x]] += 1


# In[19]:


distances = {}
first = matrix[0, :]
for i in range(num_sentence):
    change = matrix[i, :]
    distances[i] = 1 - (dot(first, change)/(norm(first)*norm(change)))


# In[21]:


dist_data_frame = pd.DataFrame.from_dict(distances, orient = 'index')
dist_data_frame.columns = ['Distance']
dist_data_frame['Sentence'] = list(map(lambda x: sentences[x], dist_data_frame.index.values))


# In[22]:


dist_data_frame.sort_values('Distance')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




