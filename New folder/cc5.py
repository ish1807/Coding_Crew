
class Solution:
    def gcd(self, a : int, b : int) -> int:
        #using euclidean algorithm to find gcd
        while b!=0:
            r=a%b
            a=b
            b=r
        return a
        #if we divide the larger number with smaller number the gcd will not change, when the remainder becomes zero the other number will be our gcd
        



#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a = int(input())
        
        
        b = int(input())
        
        obj = Solution()
        res = obj.gcd(a, b)
        
        print(res)
        

# } Driver Code Ends
