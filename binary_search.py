from termcolor import *
def Bin(A,size,tar):
    high=len(A)-1
    low=0
    mid=(high+low)//2
    while A[mid]!=tar and mid!=0 and mid!=size-1:
        if A[mid]>tar:
            high=mid-1
            mid=(high+low)//2
        else:
            low=mid+1
            mid=(high+low)//2
    if A[mid]==tar:
        return mid
    else:
        return 777
lst=[1,2,3,4,5,6,7,8,9,10]
search=int(input("Search A Number :"))
if Bin(lst,len(lst),search) !=777:
    print(colored("Number Found At %d Index"%(Bin(lst,len(lst),search)),'green'))
else:
    print(colored("Number Not Found.",'red'))
    