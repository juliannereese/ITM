#!/usr/bin/env python
# coding: utf-8

# In[1]:


def savings(gross_pay, tax_rate, expenses):

    take_home_pay = (int(gross_pay) * (1 - float(tax_rate)))//1 - int(expenses)

    return int(take_home_pay)

savings(1200,0.5,100)


# In[3]:


def material_waste(total_material, material_units, num_jobs, jobs_consumption):
    
    remaining_material = int(total_material) - (int(num_jobs) * int(jobs_consumption))

    return (str(int(remaining_material)) + (str(material_units)))
    
material_waste(100, "kg" , 10, 1)


# In[1]:


def interest (principal, rate, periods):
    
    simple_interest = principal + ((principal * rate * periods)//1)

    return (int(simple_interest))

interest (1000, 0.10, 4)


# In[ ]:




