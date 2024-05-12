#User function Template for python3

class Solution:
    def findNthTerm(self, N):
        # here the series is sum of 1st n natural numbers where n starts from 1 and goes on
        # for nth term we can just find the sum of first n natural numbers
        return (N*(N+1))//2


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.findNthTerm(N))
# } Driver Code Ends
