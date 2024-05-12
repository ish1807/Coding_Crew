#User function Template for python3

class Solution:
	def reverse_digit(self, n):
	    #using slicing to reverse the given integer
	    #first convert it to string to use string slicing
	    #reverse the converted integer using [::-1]
	    #return the integer value of given string to neglect the leading zeroes
	    return int(str(n)[::-1])
	    
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
# } Driver Code Ends
