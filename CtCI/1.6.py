#be aware that StringBuild(), method of append, is O(n)
#s += a could be O(n**2) in python, this problem was mitigated, but best practice is still [].append and ''.join([])

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
