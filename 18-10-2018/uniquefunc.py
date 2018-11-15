def unique_func(itarable, seen=None):
 seen=list(seen or []) 
 for item in itarable:
   if item not in seen:
    seen.append(item)
 return seen


print(unique_func([1,1,1,2,2,3,3]))

if __name__ == '__main__':
    assert unique_func([1,1,1,2,2,3,3,3]) == [1, 2, 3]
