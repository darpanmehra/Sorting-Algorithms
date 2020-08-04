'''
Insertion Sort

Worst Case Time Complexity - O(n^2)
Space Complexity - O(1)

'''

def insertion_sort(nums):
    if len(nums) <= 1:
        return nums
    for i in range(1, len(nums)):
        j = i-1
        key = nums[i]
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] =key
    return nums

nums = [3,6,2,7,2,1,9,8,0]
print(insertion_sort(nums))