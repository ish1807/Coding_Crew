class Solution:
    def get(self, a, b):
        temp=a#storing value of a in temporary variable temp
        a=b #value of b is stored in a
        b=temp #value of temp(which is value a before swap) is stored in b
        return (a,b)# returning the swapped values

#{ 
 # Driver Code Starts.
if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		a,b = map(int,input().strip().split())
		ob = Solution()
		ans=ob.get(a,b)
		print(str(ans[0])+" "+str(ans[1]))
# } Driver Code Ends
