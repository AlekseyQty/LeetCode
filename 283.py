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

def good_solution(nums):
    last_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i],nums[last_zero] = nums[last_zero],nums[i]
            last_zero +=1
    print(nums)

nums = [0,1,0,3,12]
good_solution(nums)