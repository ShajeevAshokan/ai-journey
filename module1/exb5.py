def unique(items):
    seen = set()
    result = []
    for x in items:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result
print(unique([1,2,2,3,1,4,3]))
    