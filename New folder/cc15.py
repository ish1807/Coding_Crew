#User function Template for python3

class Solution:
    def isSumPalindrome (self, n):
        # Loop for a maximum of 6 iterations as after 6 iterations the number itself becomes a pallindrome number
        for _ in range(6):
            # Check if the number is already a palindrome
            if str(n) == str(n)[::-1]:
                return n

            # Add the reverse of the number to itself
            reverse = int(str(n)[::-1])
            n =n+ reverse

        # If not a palindrome within 6 iterations, return -1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.isSumPalindrome(n))
# } Driver Code Ends
