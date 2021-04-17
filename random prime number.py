import time
import random
charra = random.randint(1,5)
rand=[]
sc=0
len = random.randint(10,100000)
startTime=time.time()
m =[]
i = 0

############################################################
while(i<len):#                                             #
    m.append(i)#                                           #
    i+=1#                                                  #
p = 2#                                                     #
while(p<len):#                                             #
    if(m[p] !=0):#                                         #
        sc+=1#                                             #
        j = p#                                             #
        rand.append(j)#                                    #
        while(j<len):#                                     #
            m[j]=0#                                        #
            j+=p#                                          #
    p+=1#                                                  #
############################################################

if charra < 3:
    sorted(rand, reverse = True)
randel=random.choice(rand)
print("Random prime number:", randel)
print("Time:", time.time()-startTime)
