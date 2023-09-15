from termcolor import *
def Lin(A,size,tar):
    for i in range(size):
        if A[i]==tar:
            return i
    else:
        return 777
lst=[3,4,5,7,8,1,2,9]
search=int(input("Search A Number :"))
if Lin(lst,len(lst),search) !=777:
    print(colored("Number Found At %d Index"%(Lin(lst,len(lst),search)),'green'))
else:
    print(colored("Number Not Found.",'red'))
    