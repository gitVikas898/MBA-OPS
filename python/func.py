def containsDuplicate(nums):
    unique_nums = set(nums)
    if len(unique_nums) < len(nums):
        return True
    else:
        return False



nums = [1,2,2,1,3,4,5,6,7,8,9]

if containsDuplicate(nums):
    print("The List Contains Duplicates")
else:
    print("No Duplicates");