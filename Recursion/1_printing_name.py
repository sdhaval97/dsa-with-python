class Solution:
    def printName(self, name, count, N):
        # stop recursion if count equals N
        if count == N:
            return
        
        # print the name
        print(name)
        
        # recursive call with incremented count
        self.printName(name, count+1, N)

if __name__ == "__main__":
    sol = Solution()
    N = 5
    name = "Dhaval"
    
    sol.printName(name, 0, N)
    


    