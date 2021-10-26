#Heres a python code to search for an item in an array using 2 methods (linear and binary search)

def binsearch(ar,item): 
    low=0 
    high=len(ar)-1 
    while low<=high: 
        mid=int((low+high)/2) 
        if item==ar[mid]:
            return mid 
        elif item<ar[mid]: 
            high=mid-1 
        else: 
            low=mid+1 
    else: 
        return ('invalid') 

    
def linsearch(ar,item):
    for i in range(len(ar)):
        if ar[i]==item:
            print(item,"found at position",i+1)
            flag=1
            if flag==1:
                break
    else:
        print('no. not found')
                

arr=list(eval(input("Enter the list(comma seperated): ")))
item=int(input("Enter the number to search:")) 
            
ch=int(input('enter 1 for binary search and 2 for linear search: '))
if item in arr:

    if ch==1:
        res=binsearch(arr,item) 
        print(item,"found at position",res+1) 

    if ch==2:
        linsearch(arr,item)  

else:
    print("Number not found, please check again") 
