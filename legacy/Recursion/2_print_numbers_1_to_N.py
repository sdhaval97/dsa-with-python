class Solution:
    def onetoN(self, num, N):
        
        if num > N:
            return 
        
        print(num, end=" ")
        
        self.onetoN(num+1, N)

if __name__ == "__main__":
    sol = Solution()
    sol.onetoN(0,5)