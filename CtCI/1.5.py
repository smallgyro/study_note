import collections
def onAway(s1,s2):
    counter1 = collections.Counter(s1)
    counter2 = collections.Counter(s2)
    count = 0
    for key in counter1:
        if key not in counter2:
            count += counter1[key]
        else:
            count += abs(counter1[key] - counter2[key])
        if count > 1:
            return False
    return True
s = ['pale,ple','pales,pale','pale,bale','pale,bake']
[onAway(*e.split(',')) for e in s]
