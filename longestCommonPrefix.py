def longestCommonPrefix(strs):
        prefix = ""
        min_length = strs[0]
        
        curr = ""
        for n in strs:
            if len(n) <= min_length:
                min_length = len(n)
                
        for i in range(0, min_length):
            curr = strs[0][i]
            
            for word in strs:
                if word[i] == curr:
                    continue
                else:
                    return prefix
                    

            prefix += n[i]
        
        return prefix

def longestCommonPrefix(strs):
    prefix = ""
    min_length = strs[0]

    curr = ""
    for n in strs:
         if len(n) <= min_length:
              min_length = len(n)
    for i in range(0, min_length):
         curr = strs[0][i]

         for word in strs:
              if word[i] == curr:
                   continue
              else:
                   return prefix
              
    return prefix
    