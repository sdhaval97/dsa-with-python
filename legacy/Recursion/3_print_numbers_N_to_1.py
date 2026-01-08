class Solution:
    def Nto1(self, num):
        
        if num < 1:
            return 
        
        print(num, end=" ")
        
        self.Nto1(num-1)

if __name__ == "__main__":
    sol = Solution()
    sol.Nto1(5)