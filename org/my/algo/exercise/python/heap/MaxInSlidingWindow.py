
# coding: utf-8

# In[1]:

###
# Max element in a sliding window of size K
###

from collections import deque

#arr = [1, 3, -1, -3, 5, 3, 6, 7]
arr = [1, 4, 5, 2, -5, -6, -7, 8, 10, 12, 11, 9, 15]
k = 3

dq = deque()

dq.append(0)

i = 1

while i < k:
    while dq and arr[i] > arr[dq[-1]]:
        dq.pop()
    dq.append(i)
    i = i+1


print('Max in sliding window %d is %d' % (i-k, arr[dq[0]]))

while i < len(arr):
    if i - dq[0] >= k:
        dq.popleft()
    
    while dq and arr[i] > arr[dq[-1]]:
        dq.pop()
    
    dq.append(i)
    
    i = i + 1
    print('Max in sliding window %d is %d' % (i-k, arr[dq[0]]))


# In[ ]:



