
# coding: utf-8

# In[1]:

import urllib.request

def retrieve_page(url):
    my_socket = urllib.request.urlopen(url)
    dta = my_socket.read().decode()
    my_socket.close()
    return dta

def countwords(wdlib):
    counts = {}
    for l in wdlib:
        counts[l] = counts.get(l, 0) + 1
    return counts


def findw(txt):
    lib='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    wd=''
    tlen=len(txt)
    chfd=False
    if tlen==0:
        return ''
    for i in range(tlen):
        ch=txt[i]
        if ch in lib:
            wd=wd+ch
            chfd=True
        else:
            if chfd:
                return wd
    return ''

def chop(txt,wd):
    wlen=len(wd)
    tlen=len(txt)
    if wd=='':
        return ''
    for i in range(tlen):
        testwd=txt[i:i+wlen]
        if testwd==wd:
            break
    newtxt=txt[i+wlen:]
    return newtxt


txt = retrieve_page("http://www.gutenberg.org/cache/epub/19033/pg19033.txt")
wdlib=[]
while txt!='':
    word=findw(txt)
    ntxt=chop(txt,word)
    txt=ntxt
    wdlib.append(word)
wddict=countwords(wdlib)
sparedict=wddict
vals=wddict.values()
vallist=list(vals)
vallist.sort()
maxnums=vallist[-10:]
topwds=set()
for n in range(10):
    for awd in wddict:
        if wddict[awd]==maxnums[-n]:
            topwds.add((maxnums[-n],awd))
finlist=list(topwds)
finlist.sort()
pre=finlist[:]
final=[]
for i in range(10):
    sing=pre[-i-1]
    newel=(sing[1],sing[0])
    final.append(newel)
for i in range(10):
    spcnum=20-len(final[i][0])
    print(final[i][0],' '*spcnum,final[i][1])

