
# coding: utf-8

# In[ ]:

from urllib.request import urlopen

def exchange(cur_from,cur_to,amt_from):                                     #the exchange function
    url='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+str(cur_from)+'&to='+str(cur_to)+'&amt='+str(amt_from)
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    tlen=len(jstr)
    front='"to" : "'
    for i in range(tlen-7):                                              #find the location of the result number
        if jstr[i:i+8]==front:
            break
        else:
            continue
    fpos=i+8
    newjstr=jstr[fpos:]
    rpos=newjstr.find(' ')
    numstr=newjstr[:rpos]                                               #cut off the number part from the original URL
    amt_to=float(numstr)
    return amt_to
    

    
    
def testres():                                                            #test the result
    assert exchange('USD','EUR',2.5)==2.0952375                           #this program may fail if the website change the currency proportions
    
    
def test():                                                             #main test function
    testres()
    print('*****All tests passed*****')                            #print the test result
    
    
def mymain():                                                        #main body of this program
    cur_from=input('From which currency:')
    cur_to=input('Into which currency:')
    amt_from=input('Amount of money before calculation:')
    result=exchange(cur_from,cur_to,amt_from)
    return result


print('The result is:',mymain())                                    #starting calculations
test()
quit=input('Press enter to quit')                                   #show the result before closing

