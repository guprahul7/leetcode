
def transpose_NonSquare_matrix(m):
    rowLen = len(m)
    colLen = len(m[0])
    newM = [ [0 for i in range(rowLen) ] for i in range(colLen)]

    for c in range(0, colLen):
        for r in range(0,rowLen):
            newM[c][r] = m[r][c]

    return newM

#------------------------------------------------------

def rotate_matix_square(m):
    # m = np.array([x for x in range(1,26)]).reshape(5,5)
    # print('\norig_mat:\n',m)

    #def transpose_square_matrix
    for i in range(len(m)):
        for j in range(i, len(m[0])):
            temp = m[i][j]
            m[i][j] = m[j][i]
            m[j][i] = temp

    #def switch_cols_after_transposing
    for i in range(len(m[0])//2):
        k = len(m[0]) - i - 1
        for j in range(len(m)):
            temp = m[j][i]
            m[j][i] = m[j][k] 
            m[j][k] = temp
            
    return m

#------------------------------------------------------

def spiral_matrix(matrix):
    if len(matrix)==0: return None
        
    output_arr = []
    rowBegin = 0
    rowEnd = len(matrix) - 1
    colBegin = 0
    colEnd = len(matrix[0]) - 1
    
    while (rowBegin<=rowEnd) & (colBegin<=colEnd):
        
        for i in range(colBegin,colEnd+1):
            output_arr.append(matrix[rowBegin][i])        
        rowBegin += 1
        
        for i in range(rowBegin,rowEnd+1):
            output_arr.append(matrix[i][colEnd])
        colEnd -= 1
        
        if rowBegin <= rowEnd:
            for i in range(colEnd, colBegin-1, -1):
                output_arr.append(matrix[rowEnd][i])
        rowEnd -= 1

        if colBegin <= colEnd:  
            for i in range(rowEnd, rowBegin-1, -1):
                output_arr.append(matrix[i][colBegin])
        colBegin += 1

#------------------------------------------------------

# def repeat(a,b):
#     if len(a) > (2*len(b)):
#         return False
#     if b in a:
#         return True
#     else:
#         count += 1
#         return repeat(2*a,b)
# print(repeat('abcd', 'cdabcdab'))


# def minRepeat(a, b):
#     count = 0
#     if (len(a) >= 2*len(b)) and (b not in a):
#         print(count)
#         return False
#     else:
#         while len(a) < 2*len(b):
#             if b in a:
#                 print(count)
#                 return True
#             else:
#                 a += a
#                 count += 1
       
# print(minRepeat('abcd', 'cdabcdab'))


#Palindrome 
# import math
# print(math.sqrt(4)) 
# import re
# s = 'a man, a plan, a canal: panama'
# x = re.findall('[a-zA-z]+', s)
# s = list(''.join(x))
# print(s)

# for x in s:
#     if x != s.pop():
#         print (0)
#         print(s)
# print(s)

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         import re
#         x = re.findall('[a-zA-z]+', s)
#         s = list(''.join(x).lower())
#         print(s)
#         for x in s:
#             if x != s.pop():
#                 return False
#         return True

# import numpy as np
# m = np.arange(3*3).reshape(3,3)
# print(m[1][1])


# def transpose_matrix_notSquare(m):
#     rowLen = len(m)
#     colLen = len(m[0])
#     newM = [ [0 for i in range(rowLen) ] for i in range(colLen)]

#     for c in range(0, colLen):
#         for r in range(0,rowLen):
#             newM[c][r] = m[r][c]

#     return newM

# set1 = {1,2,3,4,5,6,7,8}
# set2 = {1,2,3,9,10,11,12}
# set3 = set1.union(set2)
# set4 = set1.intersection(set2)
# print(set3, '\n', set4)

# set5 = set1.add()
# print(set5)

# lst = [1,2,3,4,5,5,4,3]
# print(list(set(lst)))

# import re 
# needle = 'll'
# haystack = 'hello'
# x = re.search(needle, haystack).span()[0]
# print(x)

# ====================================== Graph Problem ===========================

# graph = { 
#           'Vertices' : ['A','B','C','D','E'], 
#           'Edges' : { 
#                     'A':['B'],
#                     'B':['A','C'],
#                     'C':['B','D'],
#                     'D':['B','C'],
#                     'E':['F'],
#                     'F':['E'],
#                 } 
#         }

# visited = set()

# Vertices = graph['Vertices']
# Edges = graph['Edges']

# def visit(vertex):
#     visited.add(vertex)
#     edges_of_vertex = Edges[vertex]
#     print('Vertex: ', vertex,'Edges: ',edges_of_vertex)
#     for edge in edges_of_vertex:
#         if edge not in visited:
#             print('visitingEdge: ', edge, ' of Vertex: ', vertex)
#             visited.add(edge)
#             visit(edge)

# for vertex in Vertices:
#     if vertex not in visited:
#         visit(vertex)

# print('\n\n')
# visited = set()

# for vertex in Vertices:
#     if vertex not in visited:
#         stack = [vertex]
#         while stack:
#             print(stack)
#             vert = stack.pop()
#             if vert not in visited:
#                 visited.add(vert)
#                 edges_of_vert = Edges[vert]
#                 stack.extend(edges_of_vert) 
#                 print('Vertex: ', vert,'Edges: ',edges_of_vert)  

#=========================================
class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None 

a = TreeNode(100)
a.left = TreeNode(57)
a.right = TreeNode(29)
a.left.left = TreeNode(31)
a.left.right = TreeNode(43)
a.left.left.left = TreeNode(11)
a.left.left.right = TreeNode(5)
a.left.right.right = TreeNode(2)
a.right.left = TreeNode(36)
a.right.right = TreeNode(17)
a.right.left.left = TreeNode(16)
a.right.right.right = TreeNode(46)

root = a

# def pathtoNode(root,numToFind):
#     found = False
#     visited = set([None])
#     path = []
#     stack = [root]
#     while stack:
#         node = stack.pop()
#         nodeVal = node.val

#         if node not in visited:
#             visited.add(node)
#             path.append(node)

#             if nodeVal == numToFind:
#                 found = True
#                 return [node.val for node in path]
            

#             if node.left or node.right:
#                 if node.right:
#                     stack.append(node.right)
#                 if node.left:
#                     stack.append(node.left)
#             else:
#                 path.pop()
#                 i = -1
#                 while path: 
#                     if path[i].left in visited and path[i].right in visited:
#                         path.pop()
#                     else:
#                         break

#     if not found:
#         return []
#     # else:
#     #     pathvalues = [node.val for node in path]
#     #     return pathvalues              

# print(pathtoNode(root,None))


# def BFS(root):
#     d ={}
#     levels = []
#     levelsums = []
#     queue = [[root]]
#     h = 0
#     while queue:
#         currentlevel = queue.pop(0)
#         h += 1
#         #curlevelvals = [node.val for node in currentlevel]
#         levels.append(currentlevel)
        
#         nextlevel = []
#         levelsum = 0
#         while currentlevel:
#             currentnode = currentlevel.pop(0)
#             levelsum += currentnode.val
#             if currentnode.left:
#                 nextlevel.append(currentnode.left)
#             if currentnode.right:
#                 nextlevel.append(currentnode.right)

#         if nextlevel != []:
#             queue.append(nextlevel)
#         levelsums.append(levelsum)

        
#         print(levelsums)

#         #print('h:', h, 'sum: ', levelsum, 'vals: ',curlevelvals)



#     #return dict(zip(levelsums,levels))

# print(BFS(root))



# import heapq
# l = [3,5,1,8,7,6,9,10,2]
# heapq.heapify(l)
# print(l)
# print(l[0])


#Implementing a Trie 


