

def combinationSumII(array, target):

    array = sorted(array)
    currentlist=[]
    result = []
    #Recursive Function brlow
    #findCombinations(array, index, target, [], result)
    findCombinations(array, 0, target, currentlist, result)

    return result

    def findCombinations(array, index, target, currentlist, result):
        if target==0:
            result.append(currentlist)
            return
        if target < 0:
            return
        for i in range(index,len(array)):
            if i==index or array[i] != array[i-1]:
                currentlist.append(array[i])
                findCombinations(array,i+1,target-array[i],currentlist,result)
                currentlist.pop()


            

