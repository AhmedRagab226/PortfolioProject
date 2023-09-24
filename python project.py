#!/usr/bin/env python
# coding: utf-8

# In[3]:


num = 0 
while num < 5:
    print(num)
    num +=1


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[4]:


def number_cust(number,power):
    print(number**power)


# In[5]:


number_cust(5,3)


# In[21]:


def number_kwarg(**number):
    print('my number is:' +number['integer'] + 'my other number is :' +number['integer2'] )


# In[22]:


number_kwarg(integer ='2334' , integer2= '7695' )


# In[ ]:





# In[24]:


list_type = [1,2,3,3,2,1,2,3,2,1]


# In[26]:


tuple(list_type)


# In[ ]:





# In[27]:


dict_type = {'name': 'Alex','age': 28, 'hair': 'N/A'}


# In[28]:


dict_type.items()


# In[29]:


dict_type.values()


# In[30]:


dict_type.keys()


# In[31]:


list(dict_type.keys())


# In[32]:


list(dict_type.values())


# In[ ]:





# In[1]:


name = input("Enter you name: ")

weight = int(input("Enter your weight in Kg: "))

height = float(input("Enter your height in m: "))

BMI = (weight) / (height * height)

print(BMI)

if BMI > 0 :
    if BMI < 18.5 :
        print(name + ',you are Underweight ')
    elif  BMI <24.9 :
        print(name + ',you are Normal Weight ')
    elif  BMI <29.9 :
        print(name + ',you are Overweight ')
    elif  BMI <34.9 :
        print(name + ',you are Obese ')
    elif  BMI <39.9 :
        print(name + ',you are Severely Obese ')
    else:
        print(name + ',you are Morbidly Obese ')
else : 
    print('you are valid')
        


# In[ ]:





# In[67]:


import os, shutil


# In[68]:


path  = r"C:/Users/Ahmed/OneDrive/Desktop/python toturial/"


# In[69]:


file_name = os.listdir(path)


# In[70]:


folder_names = ['csv files', 'image files', 'text files','PDF files','xlsx files']

for loop in range(0,5):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])
        
        
        
for file in file_name:
    if '.txt' in file and not os.path.exists(path +'text files/'+file ):
        shutil.move(path + file ,path +'text files/'+file)
    elif '.csv' in file and not os.path.exists(path +'csv files/'+file ):
        shutil.move(path + file ,path +'csv files/'+file)
    elif '.xlsx' in file and not os.path.exists(path +'xlsx files/'+file ):
        shutil.move(path + file ,path +'xlsx files/'+file)
    elif '.jpg' in file and not os.path.exists(path +'image files/'+file ):
        shutil.move(path + file ,path +'image files/'+file)
    elif '.pdf' in file and not os.path.exists(path +'PDF files/'+file ):
        shutil.move(path + file ,path +'PDF files/'+file)
        


# In[66]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


Under 18.5	Underweight	Minimal
18.5 - 24.9	Normal Weight	Minimal
25 - 29.9	Overweight	Increased
30 - 34.9	Obese	High
35 - 39.9	Severely Obese	Very High
40 and over	Morbidly Obese	Extremely High


# In[ ]:





# In[ ]:





# In[ ]:





# In[12]:


import os ,shutil


# In[13]:


path = r"C:/Users/Ahmed/OneDrive/Desktop/python toturial/"


# In[14]:


file_name = os.listdir(path)


# In[15]:


folder_name = ['csv files','PDF files','xlsx files', 'text files','image files']

for loop in range(0,5):
    if not os.path.exists(path + folder_name[loop]):
        #print(path + folder_name[loop])
        os.makedirs(path + folder_name[loop])
        
        
for file in file_name:
    if '.txt' in file and not os.path.exists(path + 'text files/' + file):
        shutil.move(path + file ,path + 'text files/' + file )
    elif '.xlsx' in file and not os.path.exists(path + 'xlsx files/' + file):
        shutil.move(path + file ,path + 'xlsx files/' + file )
    elif '.csv' in file and not os.path.exists(path + 'csv files/' + file):
        shutil.move(path + file ,path + 'csv files/' + file )
    elif '.pdf' in file and not os.path.exists(path + 'pdf files/' + file):
        shutil.move(path + file ,path + 'pdf files/' + file )
    elif '.jpg' in file and not os.path.exists(path + 'image files/' + file):
        shutil.move(path + file ,path + 'image files/' + file )        


# In[ ]:





# In[17]:


from bs4 import BeautifulSoup
import requests


# In[18]:


url = 'https://www.scrapethissite.com/pages/forms/'


# In[19]:


page = requests.get(url)


# In[20]:


soup = BeautifulSoup(page.text,'html')


# In[21]:


print(soup)


# In[39]:


soup.find('th').text.strip()


# In[38]:


soup.find('td').text.strip()


# In[ ]:





# In[3]:


from bs4 import BeautifulSoup
import requests


# In[4]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[6]:


soup.find('table')


# In[9]:


soup.find_all('table')[1]


# In[13]:


soup.find('table', class_ = 'wikitable sortable' )


# In[23]:


Table = soup.find_all('table')[1]


# In[29]:


print(Table)


# In[36]:


World_Title = Table.find_all('th')


# In[37]:


World_Title


# In[38]:


World_Table_Title = [title.text.strip() for title in World_Title]


# In[39]:


print(World_Table_Title)


# In[51]:


import pandas as pd


# In[56]:


df= pd.DataFrame(columns = World_Table_Title)


df


# In[ ]:





# In[57]:


column_data = Table.find_all('tr')


# In[77]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    

    
    


   
    


# In[78]:


df


# In[79]:


df.to_csv(r'C:\Users\Ahmed\OneDrive\Desktop\python project\companies.csv', index = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




