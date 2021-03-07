def merge(a,b):
    c=[]
    i,j=0,0   
    
    # -------- 1 -----------
    #      a=3   b=3
    # 1--- i=0   j=0      [1]
    # 2--- i=1   j=0      [1,2]
    # 3----i=2   j=0      [1,2,3]
    
    # -------  2 -----------
    #      a=4   b=3
    # 1--- i=0   j=0  [1]
    # 2--- i=1   j=0  [1,2]
    # 3--- i=2   j=0  [1,2,3]
    # 4--- i=3   j=0  [1,2,3,4]
    # 5--- i=3   j=1  [1,2,3,4,5]
    # 6--- i=3   j=2  [1,2,3,4,5,6]
    # 7--- i=3   j=3 ---end
    
    while i<len(a) and j<len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    
    if i == len(a):
        c += b[j:]
    else:
        c += a[i:]
        
    return c


def mergeSort(lst):
    
    if len(lst) <= 1:
        return lst
    
    mid=len(lst)//2
    
    
    left_part = mergeSort(lst[:mid])
    
    right_part = mergeSort(lst[mid:])
    
    
    return merge( left_part , right_part )


a=[1,2,3]
b=[4,5,6]
merge(a,b)


lst=[1,4,2,10,3]


mergeSort(lst)











from random import randint
for _ in range(10):
    random_list=[ randint(0,1000) for _ in range(1000)  ]
    
#     print(random_list)
    
    print( sorted(random_list) == mergeSort(random_list) )  
