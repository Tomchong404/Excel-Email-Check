#!/usr/bin/env python
# coding: utf-8

# In[67]:


import csv
import pandas as pd
import re


# In[68]:


# Read file to compare
file_name = 'Fake Emails.csv'
df = pd.read_csv(file_name)
print(df.head())


# In[69]:


# Select specific column
df = df[['Fake Email']]
print(df)


# In[70]:


# Compare against emailing list from outlook 
email_list = []
entry = input("enter your email: ")
email_list = entry.split(';')


# In[71]:


# Extracting email addresses from user input
email_addresses = []

for item in email_list:
    # Using regular expression to find email addresses
    emails = re.findall(r'[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}', item)
    email_addresses.extend(emails)

print(email_addresses)


# In[76]:


# Function to check if '@' is present in a cell
def email(cell):
    return '@' in str(cell)

# Apply the function to each element in the DataFrame
filtered_values = df.applymap(email)

# Create a list of values containing '@'
emails = df[filtered_values].stack().tolist()

#Change to string
approval_emails = list(set(emails))
print (str(approval_emails ))


# In[78]:


approval_emails_l = [item.lower().strip() for item in approval_emails]
email_addresses_l = [item.lower().strip() for item in email_addresses]

# Find elements in approval_emails_l but not in email_addresses_l
mismatch1 = list(set(approval_emails_l) - set(email_addresses_l))

# Find elements in email_addresses_l but not in approval_emails_l
mismatch2 = list(set(email_addresses_l) - set(approval_emails_l))

# Combine the mismatches
all_mismatches = mismatch1 + mismatch2

# Print the results
print("Only found in excel file:", mismatch1)
print("Only found in user entry:", mismatch2)
print("All mismatches:", all_mismatches)

