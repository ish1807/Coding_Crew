#User function Template for python3

class Solution:
	def streamAvg(self, arr, n):
		avgs=[]#define an empty list
		summ=0
		for i in arr:#use for to find averages when every number in array is added
		    summ+=i
		    a=summ/ (len(avgs)+1)#finding average for every element in array
		    avgs.append(a)
		return avgs

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.streamAvg(arr, n)
        for x in ans:
            print('%.2f'%x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
