class Solution:
    def sumofN(self, n):
        
        if n == 0:
            return 0
        
        return n + self.sumofN(n-1)

if __name__ == "__main__":
    sol = Solution()
    print(sol.sumofN(6))