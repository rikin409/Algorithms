# Take in a list of numbers and a target number, return a list of the two indexes whose corresponding values in the array sum up to the target number

# Takeaways:
# Using a hashmap for a O(1) lookup time.


def twoSumBrute(nums, target):
    found = []
    for i in range(len(nums)):
        j = i+1
        while j<len(nums):
            if (nums[i]+nums[j]== target):
                found.append(i)
                found.append(j)
                return found
            j = j+1
def twoSumHashMap(nums, target):
    found = []
    searched = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in searched:
            found.append(i)
            found.append(searched[diff])
            return found
        else:
            searched[nums[i]] = i
