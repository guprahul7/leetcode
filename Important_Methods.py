


#map--reduce--filter--zip--enumerate--all.and.any--complex
#Above all creates its own object mostly as tuples, need to list() to see it.

#Use of max(1,2) and min(n1,n2)

#Map  - #map-object
# map(function, iterable)
# map(lambda x:x**2, iterable))  

#Filter - #filter-object
# filter(function, iterable)
# filter(lambda x: x%2==0, ls)

#Zip  - #zip-object
# zip(iterable1, iterable2, ....,)
# zips in group of tuples
#Unzip - zip-object
# zip(* zip-object)
# returns initially-zipped-objects as tuples

#Enumerate - #enumerate-object
# enumerate(iterable, start=0)  #can set starting point, default is 0
#returns tuple-pairs with (index, item) -- (0, 1)

#newEmails = list(filter(lambda x : x != 'something@something.com', emails))
#lst.remove('item') - removes first occurence of the item in the list. Returns nothing

#''.join()
#.replace()
# x = list('abc')
# y = random.choice(x)
# print(y)
# x = re.findall('[a-zA-z]+', s)

#SORT()
#   x.sort() sorts an iterable x, does not sort string, does not return anything as it just sorts the iterable
#   sorted(x) sorts an iterable x, including string, returns items from x in a new sorted list  
# sorted( iterable, key = lambda x: (x[1], x[2]) )
# sorted( sorted(a, key=lambda x: x[0]), key=lambda x:x[1])

#range(start,stop,step) #does not include stop
#list comprehension #[x for x in range(0,100,5) if x%2==0]
#if x in lst: return x

#LIST
#list.extend(iterable) --> #appends each element of given iterable to the list (extend is like multi-append items individually from another iterable)
#list.index(x)
#list.index(x, start_index, stop_index)

#lst.insert(index) #inserting item at given index

#String
#   ' '.join(iterable)  #concatenates items of an interable, along with given string/separation, returns string
#Example: lst = [1,3,5,6] -->  '-'.join(lst) --> 1-3-5-6
#Example: st = 'hello world' --> '1'.join(st) --> h..e..l..l..o.. ..w..o..r..l..d

#strings have read-only indexing iterability,
#Example: 'hello', doing s[0] returns 'h', but doing s[0] = 'c' returns Error

 
#Regex



#Set
#Set has no sort attribute

#Dictionary
#Sort
    #d = dict( sorted(d.items(), key=lambda x: x[1]) )
    #   sorted( s, key = lambda x: (x[1], x[2]) )
#Update
    #d.update( item ) #item can be dictionary, or list of tuple (key-value) pairs
        #item = {key1: value1, key2:value2}
        #item = [ (key1,value1), (key2,value2) ]
#Remove
    #d.pop(key) - if present, removes key from dictionary, returns value that is mapped to key (KeyError is not present)
    #del d[key]  - if present, removes given key from dictionary(throws KeyError if item not found)


#Any - sequence of 'OR' operations on each item in iterable
#Returns True if any item is True. (if empty or all-false returns Fale)

#All - sequence of 'AND' operations on each item in iterable
#Returns True if all items are True. (if empty returns True)
