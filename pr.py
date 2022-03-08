'''def evenSubarray(numbers, k):
    pow_set_size=int((pow(2,k)))
    counter=0
    j=0
    lst=[]
    for counter in range(0,pow_set_size):
        lst1=[]
        for j in range(0,k):
            if ((counter & (1<<j))>0):
                a=(numbers[j])
                lst1.append(a)

        lst.append(lst1)
    return lst

if __name__ == '__main__':
    numbers=list(map(int,input().split()))
    k=len(numbers)
    print(evenSubarray(numbers,k))'''


'''def evenSubarray(numbers, k):
    
    pow_set_size=int((pow(2,len(numbers))))
    counter=0
    j=0
    lst=[]
    n=len(numbers)
    for i in range(0,n):
        lst1=[]
        for j in range(i,n):
            for m in range(i,j+1):
                a=numbers[m]
                lst1.append(a)
        lst.append(lst1)
    
    set(lst)
    l=len(lst)
    ans=0
    for i in range(l):
        p=0
        for j in range(len(lst[i])):
            if lst[i][j]%2!=0:
                p+=1
        if p<=k:
            ans+=1
    return ans        



if __name__ == '__main__':
    numbers=list(map(int,input().split()))
    k=int(input())
    print(evenSubarray(numbers,k))'''

'''l=[1,[2,3],3,[2,3],1]
a=list(set(l))
print(a) ''' 


'''n=5
k=25
for i in range(n,k+1):
    
        for j in range(2,(i//2)+1):
            if i%j==0:
                break
        else:
            print(i)'''



        
    


  
