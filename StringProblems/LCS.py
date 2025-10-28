def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    min_len = min(len(s) for s in strs)
    result = ""
    
    for i in range(min_len):
        ch = strs[0][i]
        flag = True
        for j in range(1,len(strs)):
            if ch != strs[j][i]:
                flag = False
                break
        if flag:
            result+=ch
        else:
            break
    return result
    
print(longestCommonPrefix(["flower", "flow", "fle"]))

    
    