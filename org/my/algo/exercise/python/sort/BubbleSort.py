
# coding: utf-8

# In[11]:

arr = [10, 6, 5, 8, 7, 2, 3, 1, -12, -10, 20, 16]

for i in range(len(arr)):
    j = i + 1;
    
    while j < len(arr):
        if arr[i] > arr[j]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
        j = j + 1


print("sorted arr: %s" %(arr))


# In[ ]:




# In[ ]:



