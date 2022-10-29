#!/usr/bin/env python
# coding: utf-8

# In[6]:


#import libraries

import pandas as pd
import os


# In[14]:


#merging 12 months of sales data into single file

df = pd.read_csv("E:/My projects/Python/Sales analysis/SalesAnalysis/Sales_Data/Sales_April_2019.csv")

#read and list all the files from directory

files = [file for file in os.listdir("E:/My projects/Python/Sales analysis/SalesAnalysis/Sales_Data")]

files

#create empty dataframe to store all the files

all_months_data = pd.DataFrame()

#Concatenate all the data files in to empty dataframes

for file in files:
    df = pd.read_csv("E:/My projects/Python/Sales analysis/SalesAnalysis/Sales_Data/" +file)
    all_months_data=pd.concat([all_months_data,df])
    
all_months_data.head()


# In[15]:


all_months_data.to_csv("E:/My projects/Python/Sales analysis/SalesAnalysis/Sales_Data/all_data.csv", index=False)


# In[17]:


all_data=pd.read_csv("E:/My projects/Python/Sales analysis/SalesAnalysis/Sales_Data/all_data.csv")
all_data.head()


# #### Task 1 : Clean up data, drop all NaN values
# 

# In[18]:


all_data= all_data.dropna(how="all")
all_data.head()


# #### Task 2 : Find "Or" and delete it

# In[27]:


all_data=all_data[all_data["Order Date"].str[0:2] != "Or"]


# In[ ]:





# In[ ]:





# #### Task  : Create a month column

# In[26]:


#Create a month column by extracting first two strings of Order Date column

all_data["Months"] = all_data["Order Date"].str[0:2]

all_data["Months"] = all_data["Months"].astype("int32")

all_data.head()


# #### Convert "Quantity order" and " Price Each" into numeric
# 

# In[30]:


all_data["Quantity Ordered"] = all_data["Quantity Ordered"].astype("int")
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])


# ####  Question 1 : What was the best month for sale? and how much was earned tha month?

# In[34]:


all_data["Sales"] = all_data["Quantity Ordered"] * all_data["Price Each"]
all_data.head()

result = all_data.groupby("Months").sum()

result


# #### Visualization :  What was the best month for sale? and how much was earned that month?

# In[40]:


import matplotlib.pyplot as plt

months = range(1,13)
plt.bar(months,result["Sales"])
plt.ticklabel_format(style='plain')
plt.xticks(months)
plt.xlabel("Month Number")
plt.ylabel("Total earning in USD")
plt.show()


# #### Question 2 : What US City has highest number of sales?
# 

# In[101]:


all_data["City"] = all_data["Purchase Address"].apply(lambda x : x.split(",")[1] + "(" + x.split(",")[2].split(" ")[1] + ")")
#all_data["States"] = all_data["Purchase Address"].apply(lambda x : x.split(",")[2])

all_data.head()

all_data.drop(columns = "States")


# In[102]:


results = all_data.groupby("City").sum()

results


# #### Visualization 2 :  What US City has highest number of sales?

# In[120]:


import matplotlib.pyplot as plt

cities=[ city for city, df in all_data.groupby("City") ]

plt.bar(cities,results["Sales"])
plt.xticks(cities, rotation = "vertical", size = 8)
plt.xlabel("US City Names")
plt.ylabel("Total earning in USD")
plt.show()


# #### Question 3 : What time should we display advertisements to maximize likelihood of customer's buying products?

# In[121]:


#Convert "Order Date column into DateTime format"

all_data["Order Date"] = pd.to_datetime(all_data["Order Date"])


# In[126]:



# Extract "hours" from Order Date column

all_data["Hour"] = all_data["Order Date"].dt.hour
all_data["Minute"] = all_data["Order Date"].dt.minute
all_data.head()


# #### Visualization 3 of Question 3

# In[136]:



hours = [hour for hour, df in all_data.groupby("Hour")]
y = all_data.groupby("Hour").count()
plt.plot(hours, y, color = "red")
plt.grid()
plt.xlabel("Hours")
plt.xticks(hours, size = 8)
plt.ylabel("Number of orders")


# #### Question 4: What products are more often sold together?

# In[137]:


all_data.head()


# #### Question 5 : What product was sold most? Why do you think it wa ssold the most

# In[186]:


product_group = all_data.groupby("Product")
quantity_ordered = product_group.sum()["Quantity Ordered"]

products = [product for product, df in product_group]


plt.bar(products,quantity_ordered)
plt.xticks(products, rotation = "vertical", size = 8)
plt.show()


# In[181]:





# In[177]:





# In[178]:





# In[179]:





# In[ ]:




