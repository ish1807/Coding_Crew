
class Solution:
    def seriesSum(self, n : int) -> int:
        #Here n is number of elements
        res = (n*(n+1))//2
        #The above formula gives sum of first n natural numbers
        return (res)
        #Return the result obtained
    
#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.seriesSum(n)

        print(res)

# } Driver Code Ends
