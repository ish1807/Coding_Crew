#User function Template for python3

class Solution:
    def greatestOfThree(self,A,B,C):
        if A>=C and A>=B: #check whether if A is greater
            return A
        elif B>=C and B>=A: #check whether if B is greater
            return B
        else:   #if A and B are greater C will be the greatest of three
            return C
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split(' '))
        ob=Solution()
        print(ob.greatestOfThree(A,B,C))   
# } Driver Code Ends
