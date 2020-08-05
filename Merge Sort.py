'''
Merge Sort

Worst Case Time Complexity- O(nlogn)
Space Complexity- O(n)
'''

def mergeSort(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]

        #Recursively Calling mergeSort for left and right subarray
        mergeSort(left)
        mergeSort(right)

        #Merge Operation (Conquer technique)
        i, j, k = 0,0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            nums[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            nums[k] = right[j]
            j+=1
            k+=1

nums = [54,26,93,17,77,31,44,55,20]
mergeSort(nums)
print(nums)