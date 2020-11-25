#Merge K Sorted Lists

from queue import PriorityQueue

pq = PriorityQueue()

def mergeKsortedLists(lists):
    x = []
    while lists:
        minVal = min([lists[i].val for i in range(len(lists))])
        index = 0
        for l in lists:
            if l.val == minVal:
                x.append(l)
                if l.next == None:
                    lists.remove(l)
                else:
                    lists[index].next = l.next
                break
    
    for i in range(len(x)-1):
        x[i].next = x[i+1]

    x[len(x)-1].next = None