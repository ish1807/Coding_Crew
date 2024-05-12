#User function Template for python3

class Solution:
	def find_median(self, v):
            #Sort the given array
	    v.sort()
	    if(n%2!=0):
                #If there are odd number of elements return (n+1)/2th term
	        return int(v[int(n/2)])
	    #If there are even number of elements return average of n/2th term and (n/2)+1th term
	    return int((v[int((n-1)/2)]+v[int((n)/2)])/2)
	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends
