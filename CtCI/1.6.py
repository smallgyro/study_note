def SCompress(s):
    if len(s) <= 2:
        return s
    ret = ''
    start = s[0]
    i = 1
    count = 1
    while i<len(s):
        if s[i] != start:
            ret = ret + start + str(count)
            start = s[i]
            count = 1
            i += 1
        else:
            count += 1
            i += 1
    ret = ret + start + str(count)
    return ret if len(ret)<len(s) else s
a = 'aabcccccaaa'
SCompress(a)
