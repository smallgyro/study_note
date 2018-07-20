def checkPP(s):
    counter = {}
    for i in s:
        if i != ' ':
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
    isOdd = False
    for key in counter:
        if counter[key]%2 == 1:
            if isOdd:
                return False
    return True
a = 'Tact Coa'
checkPP(a)
