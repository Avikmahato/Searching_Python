from termcolor import *
def Bin(A,tar,high,low):
    mid=(high+low)//2
    if A[mid]==tar:
        return mid
    elif A[mid]<tar:
        return Bin(A,tar,high,mid+1)
    elif A[mid]>tar:
        return Bin(A,tar,mid-1,low)
    else:
        return 777
lst=[1,2,3,4,5,6,7,8,9,10]
search=int(input("Search A Number :"))
if Bin(lst,search,len(lst)-1,0) !=777:
    print(colored("Number Found At %d Index"%(Bin(lst,search,len(lst)-1,0)),'green'))
else:
    print(colored("Number Not Found.",'red'))
    