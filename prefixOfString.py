def prefix(strs):
    if not strs:
       return ""
    prefix=strs[0]
    for str_index,value in enumerate(strs[1:],start=1):
      temp_prefix=list()
      for chars_str,chars_start  in zip(value,prefix): 
        if chars_start==chars_str:
           temp_prefix.append(chars_start)
        else:
           break
    
      prefix = "".join(temp_prefix)  

      if not prefix:
         break
       

    return prefix     




array=["areeba","areesha","arisha","anaya"]
arr=[]
print(prefix(array))
