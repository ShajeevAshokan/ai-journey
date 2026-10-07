def two_num(nums, target):
    seen = {}
    for i,n in enumerate(nums):
        need = target - n
        if need in seen:
            return(seen[need],i)
        seen[n] = i
    return None
print (two_num([2,3,6,5],11))
        