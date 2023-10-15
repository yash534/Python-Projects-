#!/usr/bin/env python
# coding: utf-8

# # Automatic file sorter in file explorer

# In[1]:


#importing shutil and os

import os, shutil 


# In[2]:


#path where all the files are stored and has to be sorted in their respective folder 

path = r"C:/Users/yashp/OneDrive/Documents/file sorter/"


# In[3]:


#making directories for storing files 

file_name = os.listdir(path)


# In[4]:


folder_names = ["csv files", "image files", "text files"]

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs(path + folder_names[loop])

for file in file_name:
    if ".csv"  in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" +file)
    elif ".docx"  in file and not os.path.exists(path + "doc files/" + file):
        shutil.move(path + file, path + "doc files/" +file)
    elif ".txt"  in file and not os.path.exists(path + "txt files/" + file):
        shutil.move(path + file, path + "txt files/" +file)    
    elif ".jpg"  in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" +file)
        


# In[ ]:




