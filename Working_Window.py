
# st = 'aabbccddeefghiiii'

# d = {}
# count = {}
# for x in st:
#        if x in d:
#               d[x] += 1
#        else:
#               d[x] = 1

# for key,value in d.items():
#        if value in count:
#               count[value] += 1
#        else:
#               count[value] = 1

# print(d)
# print(count) 


# st = 'ABCCBA'
# x = enumerate(st)
# print(x)
# x = set(x)
# print(x)

# print(x.index((1,'B')))


# def check_count(st):
       
#        count = 0
#        for x in range(0, len(st)-2):
#               for marker in range (len(st), x+1, -1):
#                      y = st[x:marker]
#                      if 'A' in y and 'B' in y and 'C' in y:
#                             count += 1
#                             print(y)
#        return count

# print(check_count(st))

# rules = [0, 1, 0, 0, 0, 1, 0, 0, 0]

#Learn Permutations







# def neighbors(cell):
#        if 



# x = 'def'


# print(s)

# x = set(['B','C','D',"E",'A'])
# print(x)
# y = set('A')
# print(y)

# print(x-y)

# nums1 = [1,4,5,1]
# nums2 = [2,2]

# print(nums1.index(4))
# #num.append(nums1.pop(nums1.index(4)))
# # nums1.pop()


# s = 'hello there children'
# print(' '.join(list(s.split()[-1::-1])))
# from collections import OrderedDict
# d = OrderedDict()
# for x in range (5):
#    d.update({'string{}'.format(x): ['Hello {}'.format(x+10)]})
# print(d)

# for x in d:
#     print(x, d[x])

# s = 'hello'
# # strings have read-only indexing iterability

# d = {1:'x', 2:'y'}
# if 1 in d:
#     print('y')

#-------------------------------------------------
# ls = [1,12,3,0,5,7,3,9,0,20,0,0,0,22]

# def zero_ends(A):
    
#     if len(A) == 0 or len(A) == 1:
#         return A
    
#     start_index = 0
#     end_index = len(A) - 1
    
#     while start_index < end_index:

#         if A[start_index] == 0:  
            
#             while A[end_index] == 0:
#                 end_index -= 1
            
#             A[start_index] = A[end_index]
#             A[end_index] = 0
#             end_index -= 1
            
#         start_index += 1
        
#     return A

# print(zero_ends(ls))
#------------------------------------------------


# ls = ['i', 'ij','a','b','a','a','b','i','i','i']
# ls.sort()

# d = dict()
# for word in ls:
#     if word in d:
#         d[word] += 1
#     else:
#         d[word] = 1
    

# print( dict(sorted( d.items(), key = lambda x: x[1], reverse=True))  ) 

# from operator import itemgetter
# from collections import _Ordered

# from operator import itemgetter
# from collections import OrderedDict

# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_x = OrderedDict(sorted(x.items(), key=itemgetter(1)))

# v_crush = [[] for _ in range(10)] 

# print(v_crush)

# d = {'r':1, 'e':2, 't':1}
# print(d.items(), '\n')
# print(sorted(d.items(), key=lambda x: x[1], reverse= True))

# import copy 
# nums = [2,3,4,5]
# ncopy = copy.deepcopy(nums)
# print(nums, ncopy)
# ncopy.pop(0)
# print(nums, ncopy)

# s = 'abccccdddd'
# print(set(s))
# print(list(s))


# import numpy as np
# print(np.e)


# from queue import Queue

# q = Queue()

# q.put(2)
# q.get(2)
# q.empty()

# from queue import PriorityQueue
# pq = PriorityQueue()
# pq.

visited = {0}
vertEdges = {1,2,0}
print(vertEdges.intersection(visited))






