import time

def bubbleonset(tab,x):
    
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
        for i in range(2):
            if value[i]<value[i+1]:
                value[i],value[i+1]=value[i+1],value[i]
                index[i],index[i+1]=index[i+1],index[i]
    finish=time.time()
    t=finish-start
    return index,t

a=bubbleonset([9,1,1,1,0,0,0,8,10,11,14,2132323,24234524], 2)
print(a)