#User function Template for python3

class Solution:
    def count_divisors(self, N):
        # initialise count to zero
        c = 0
        # Iterate only up to the square root of N to decrease the loop iterations which also decreases time complexity and increases efficiency
        for i in range(1, int(N**0.5) + 1):
            #check if i is divisor
            if N % i == 0:
                # If i is divisible by 3 increase c
                if i % 3 == 0: 
                    c += 1
                # inc c if n/i is also divisible by 3
                if ((N//i)% 3==0):
                    c += 1
        #chech if perfect square is divisible by 3
            if ((i*i==N) and (i%3==0)):
                c-=1
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3#Back-end complete function Template for Python 3#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.count_divisors(N))
# } Driver Code Ends
