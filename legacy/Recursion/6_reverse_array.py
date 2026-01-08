class Solution:
    def reverse_array(self, left, right, myarr):

        # setting base condition
        if left >= right:
            return

        # swapping the elements
        myarr[left], myarr[right] = myarr[right], myarr[left]

        # recursive call with pointers moved inward
        self.reverse_array(left + 1, right - 1, myarr)


# Test the function
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    arr1 = [1, 2, 3, 4, 5]
    print(f"Original: {arr1}")
    sol.reverse_array(0, len(arr1) - 1, arr1)
    print(f"Reversed: {arr1}")

    # Example 2
    arr2 = [10, 20, 30, 40]
    print(f"\nOriginal: {arr2}")
    sol.reverse_array(0, len(arr2) - 1, arr2)
    print(f"Reversed: {arr2}")
