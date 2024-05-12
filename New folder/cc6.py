#User function Template for python3

class Solution:
    def isDigitSumPalindrome(self, n):
        n=str(n)#converting number into string
        digit_sum=sum(map(int,n))#finding the sum of digits in number
        r=int(str(digit_sum)[::-1])#reversing the sum of digits in number
        if digit_sum==r:
            return 1 #return 1 if sum of digits and reverse of that number are same
        return 0  # else return zero


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends
