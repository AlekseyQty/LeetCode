# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

def solution(nums):
    k = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            for j in range(k,len(nums)):
                if nums[j] == 0:
                    if j > i:
                        continue
                    nums[i],nums[j] = nums[j],nums[i]
                    k+=1
                    break
    print(nums)

nums = [1,0]
solution(nums)