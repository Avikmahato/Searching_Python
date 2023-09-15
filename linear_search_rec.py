from termcolor import *
def Lin(A,size,tar):
    if size==-1:
        return 777
    elif A[size]==tar:
        return size
    else:
        return Lin(A,size-1,tar)
lst=[3,4,5,7,8,1,2,9]
search=int(input("Search A Number :"))
if Lin(lst,len(lst)-1,search) !=777:
    print(colored("Number Found At %d Index"%(Lin(lst,len(lst)-1,search)),'green'))
else:
    print(colored("Number Not Found.",'red'))
    