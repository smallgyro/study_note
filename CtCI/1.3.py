from array import array
def replace(string,lenth):
    lenth = lenth + 2*sum(1 for e in string[:lenth] if e == ' ')
    slow = fast = lenth -1
    string = array('c',string)
    while string[fast] == ' ':
        fast -=1
    if fast < 0:
        return
    while fast>=0:
        if string[fast] != ' ':
            string[fast],string[slow] = string[slow],string[fast]
            fast -=1
            slow -=1
        else:
            string[slow-2:slow+1] = array('c','%20')
            slow -= 3
            fast -= 1
    return string
a = "Mr John Smith    "
replace(a,13)
# be aware that string is immutable in python
