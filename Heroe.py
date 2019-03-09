#!/usr/bin/env python
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head(10)


# ## Player Count

# * Display the total number of players
# 

# In[2]:


#purchase_data["Purchase ID"].sum()
#purchase_data_info = purchase_data.sum()
#f"Total number of Players {purchase_data_info}"

total = purchase_data['SN'].count()

print("Total number of Players",total)






# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[3]:


purchase_item_name = len(purchase_data["Item Name"].unique())

purchase_average = purchase_data["Price"].mean()

purchase_total = purchase_data["Price"].sum()

summary_table = pd.DataFrame(
    {"Total Unique Item": purchase_item_name,
    "Average Item Price": [purchase_average],
    "Total Purchase Price": [purchase_total]})
summary_table



# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[4]:



gender_total = purchase_data.groupby("Gender")

total_gender= gender_total.nunique()["SN"]

player_percentage = total_gender / total * 100

summary_gender = pd.DataFrame({
          "Gender totals":[total_gender],
          "Persentage male and female": [player_percentage]})
summary_gender.index.name = None
summary_gender.sort_values(["Gender totals"], ascending = False).style.format({"player_percentage":"{:.2f}"})
#summary_gender.head(15)




#summary_gender.index.name =None
#summary_gender.head()


#Gender_total_df = pd.DataFrame({"Gender Percentage": player_percentage,
                               #"Count":gender_total})
#

#Gender_total_df.sort_values(["Count"], ascending = False)


# In[5]:


gender_total = purchase_data.groupby("Gender")
total_gender= gender_total.nunique()["SN"]
player_percentage = total_gender / total * 100
player_percentage


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[6]:


#count_buy = gender_total["Purchase ID"].count()

#price_avg = gender_total["Price"].mean()
price_total = gender_total["Price"].agg([np.mean, np.sum , np.std,len])
price_total


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[11]:


Age_bin = [0,10,14,19,24,29,34,41,100]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

purchase_data["age group"] = pd.cut(purchase_data["Age"],Age_bin,labels=group_names )
purchase_data


age_costgroup = purchase_data.groupby("age group")

age_count = age_costgroup["SN"].nunique()

Percentage = (age_count/total) * 100

Playercount_byage = pd.DataFrame({"Player Percentage": Percentage,"Count": age_count})

Playercount_byage.head()


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[12]:


total_purch_age = age_costgroup["Purchase ID"].count()
average_purch = age_costgroup["Price"].mean()
total_age_purch = age_costgroup["Price"].sum()

purchase_per_age_avg = (total_age_purch/age_count) *100

Age_Analysis_pd = pd.DataFrame({"Player Percent": purchase_per_age_avg,
                              "count": age_count })

Age_Analysis_pd.head()


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[22]:


top_spender =purchase_data.groupby("SN")

spender_count = top_spender["Purchase ID"].count()

spender_count


# In[21]:


top_spender =purchase_data.groupby("SN")

spender_count = top_spender["Purchase ID"].count()
avg_spender = top_spender["Price"].mean()

spender_total = top_spender["Price"].sum()

Most_spenders_pd = pd.DataFrame({"Spender Count": spender_count,
                                 "Avg spent": avg_spender,
                                 "Spender total": spender_total})

Most_spenders_pd.head()
# was up late dont know what I am doing wrong cant get it to count all the 
SN 


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[30]:


most = purchase_data[["Item ID", "Item Name", "Price"]]
item_grup = most.groupby(["Item ID", "Item Name"])  

item_count = item_grup["Price"].count()

Item_price = item_grup["Price"].sum()

real_cost = Item_price/item_count


Most_popular_Stuff = pd.DataFrame({"count of items": item_count,
                                  "item price": Item_price,
                                  "Real cost": real_cost})


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[31]:


most_profit = Most_popular_Stuff.sort_values(["Real cost"], ascending=False).head()

most_profit


# In[ ]:




