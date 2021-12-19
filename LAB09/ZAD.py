from typing import Any, List
def bubblesortasc(l :List):
    n = len(l)
    for i in range(n):
        for j in range(n):
            if(l[i]<l[j]):
                temp = l[i]
                l[i] = l[j]
                l[j] = temp

def bubblesortdesc(l :List):
    n = len(l)
    for i in range(n):
        for j in range(n):
            if(l[i]>l[j]):
                temp = l[i]
                l[i] = l[j]
                l[j] = temp

def selectionsortasc(l :List):
    n = len(l)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if(l[j]<l[min_index]):
                min_index = j
        l[i],l[min_index]=l[min_index],l[i]

def selectionsortdesc(l :List):
    n = len(l)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if(l[j]>l[min_index]):
                min_index = j
        l[i],l[min_index]=l[min_index],l[i]

def insertionsortasc(l: List):
    n = len(l)
    for i in range(1,n):
        key = l[i]
        j = i-1
        while(j>=0 and l[j]>key):
            l[j+1]=l[j]
            j=j-1 
            l[j+1]=key

def insertionsortdesc(l: List):
    n = len(l)
    for i in range(1,n):
        key = l[i]
        j = i-1
        while(j>=0 and l[j]<key):
            l[j+1]=l[j]
            j=j-1 
            l[j+1]=key

list = [6,1,7,3,4,9,2,5,8,0]
list2 = [8, 5, 4, 2, 1, 7, 9, 6, 0, 3]
list3 = [3, 4, 0, 7, 1, 5, 2, 8, 9, 6]
list4 = [3, 4, 1, 2, 5, 0, 9, 8, 6, 7]
list5 = [3, 5, 8, 7, 1, 6, 9, 4, 0, 2]
list6 = [0, 7, 9, 4, 8, 6, 5, 3, 2, 1]
list7 = [9, 2, 1, 5, 8, 0, 6, 4, 3, 7]
list8 = [4, 5, 2, 7, 0, 9, 1, 3, 6, 8]
list9 = [0, 8, 2, 7, 6, 3, 9, 1, 5, 4]
list10 = [2, 0, 7, 3, 4, 5, 8, 6, 9, 1]
bubblesortasc(list)
bubblesortasc(list2)
bubblesortasc(list3)
selectionsortasc(list4)
selectionsortasc(list5)
selectionsortasc(list6)
insertionsortasc(list7)
insertionsortasc(list8)
insertionsortasc(list9)
insertionsortasc(list10)
print(list)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
print(list7)
print(list8)
print(list9)
print(list10)
bubblesortdesc(list)
bubblesortdesc(list2)
bubblesortdesc(list3)
selectionsortdesc(list4)
selectionsortdesc(list5)
selectionsortdesc(list6)
insertionsortdesc(list7)
insertionsortdesc(list8)
insertionsortdesc(list9)
insertionsortdesc(list10)
print(list)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
print(list7)
print(list8)
print(list9)
print(list10)
