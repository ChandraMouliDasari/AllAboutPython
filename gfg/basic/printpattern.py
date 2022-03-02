def printPat(n):
    #Code here
    while n > 0:
        if i in range(n):
            print(str(i)*3)
    return
    
    

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n= int(input())
        print (printPat(n))
# } Driver Code Ends