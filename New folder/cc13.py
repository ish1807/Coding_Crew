#User function Template for python3

class Solution:
    def oppositeFaceOfDice(self, N):
    	return 7-N #for a dice, 1 is opp to 6, 2 is opp to 5, 3 is opp to 4


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.oppositeFaceOfDice(N)
        print(ans)
# } Driver Code Ends
