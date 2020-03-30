import time

def insertonset(tab,x):
    
    start=time.time()
    value=[]
    index=[]
    j=0
    
    for i in range(len(tab)):
        if tab[i]>x:
            value.append(tab[i])
            index.append(i)
            j=j+1
            if j==3:
                break
                
    for i in range(2):
        k=value[i]
        l=index[i]
        z=i-1
        while z>=0 and value[z]>k:
            value[z+1]=value[z]
            index[z+1]=index[z]
            z=z-1
            value[z+1]=k
            index[z+1]=l
    
    finish=time.time()
    t=finish-start
    return index[2],index[1],index[0],t

b=insertonset([9,1,1,1,0,0,0,8,10,11,14,2132323,24234524], 2)
print(b)