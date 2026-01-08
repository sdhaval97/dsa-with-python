class Solution:
    def factorial(self, n):
        
        if n == 0:
            return 1
        
        return n * self.factorial(n-1)

if __name__ == "__main__":
    sol = Solution()
    print(sol.factorial(0))