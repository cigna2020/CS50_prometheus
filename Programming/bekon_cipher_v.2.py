key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

import sys

dic = {"aaaaa":'a', "aaaab":'b', "aaabb":'c', 
    "aabbb":'d', "abbbb":'e', "bbbbb":'f', 
    "bbbba":'g', "bbbab":'h', "bbabb":'i', 
    "babbb":'j', "abbba":'k', "bbbaa":'l', 
    "bbaab":'m', "baabb":'n', "aabba":'o', 
    "abbab":'p', "bbaba":'q', "babab":'r', 
    "ababb":'s', "babba":'t', "abbaa":'u', 
    "bbaaa":'v', "baaab":'w', "aaaba":'x', 
    "aabab":'y', "ababa":'z'}

x = sys.argv[1]

x = x.replace(' ', '')

y = ''

z = 0

l = []

for i in x:
    if i.islower() == True:
        x = x.replace(i, "a")
    elif i.isupper() == True:
        x = x.replace(i, "b")

while z < len(x):
    l.append(x[z:z+5])
    z += 5
    for i in l:
        if len(i) < 5:
            del l[l.index(i)]

for a in l:
    for i in dic.keys():
        if i == a:
            y = y + dic.get(i)

print(y)