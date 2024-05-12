#User function Template for python3
  
class Solution:
    def armstrongNumber (self, n):
        #convert the given number into string to access the digits
        ns=str(n)
        s=0
        #calculate the sum of cubes of each digit using for loop
        for i in ns:
            s=s+int(i)**3
        #return yes if sum and number are equal, else no
        return "Yes" if s==n else "No"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends
