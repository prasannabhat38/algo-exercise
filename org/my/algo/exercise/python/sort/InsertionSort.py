
# coding: utf-8

# In[13]:

arr = [10, 6, 5, 8, 7, 2, 3]

for i in range(len(arr)):
    tmp = arr[i]
    j = i - 1
    loc = i
    
    while j >= 0:
        if arr[j] > tmp:
            arr[j + 1] = arr[j]
            loc = j
        j = j - 1
    
    arr[loc] = tmp

print('sorted arr: %s' % (arr))
    
    


# In[ ]:



