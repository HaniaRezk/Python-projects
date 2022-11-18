import random
import math
import time

def insertionsort(a): #insertion sort
    n=len(a)
    for j in range(1,n):
        key=a[j]
        i=j-1
        while i>0 and a[i]>key:
            a[i+1]=a[i]
            i-=1
        a[i+1]=key

def merge(a,p,q,r): #merge part of the algorithm
    n1=p-q+1
    n2=r-q
    A1=list(range(n1+1))
    A2=list(range(n2+1))
    i=0
    while i<n1:
        A1[i]=a[p+i+1]
    j=0
    while j<n2:
        A2[j]=a[q+1]
    A1[n1]=math.inf
    A2[n2]=math.inf
    i=0
    j=0
    k=p
    while k<r+1:
        if A1[i]<=A2[j]:
            a[k]=A1[i]
            i+=1
        else:
            a[k]=A2[j]
            j+=1
def merge_sort(a,p,r): #mergesort recurive algorithm// most efficient sorting algorithm
    if p<r:
        q=math.floor((p+r)/2)
    merge_sort(a,p,q)
    merge_sort(a,q+1,r)
    merge(a,p,q,r)


import random
def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            z=A[i]
            A[i]=A[j]
            A[j]=z
    c=A[i+1]
    A[i+1]=x
    A[r]=c
    return i+1

def randomizedpartition(A,p,r): #randomized version of partition: more efficient than normal one
    q=random.randint(p,r)
    z=A[q]
    A[q]=A[r]
    A[r]=z
    return partition(A,p,r)

def Quicksort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        Quicksort(A,p,q-1)
        Quicksort(A,q+1,r)

def randomizedquicksort(A,p,r): #another very efficient sorting algorithm.
    if p<r:
        q=randomizedpartition(A,p,r)
        randomizedquicksort(A,p,q-1)
        randomizedquicksort(A,q+1,r)
