#User function Template for python3

class Solution:
    def nPr(self, n, r):
        #npr = n!/(n-r)!
        #that will be equal to n*(n-1)*(n-2)*....(n-r-1)
        p=1
        for i in range(0,r): #using for loop to find npr
            p=p*(n-i)
        return p


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nPr(n, r))
# } Driver Code Ends
