def bruteForce(nums, target):
	
	# Time Complexity O(n^2)
	i = 0
	result = []
	while i < (len(nums)-1):
		j = i+1
		while j < len(nums):
			if (nums[i]+nums[j] == target):
				result.append(i)
				result.append(j)
				return result
			j += 1
		i += 1

def twoPassHash(nums, target):
	# Two Pass Hash
	# Time Complexity O(n)
	# Space Complexity O(n)
	dict = {}
	for i in range(len(nums)):
		dict[nums[i]] = i
	for i in range(len(nums)):
		complement = target-nums[i]
		if complement in dict and i != dict[complement]:
			return [i, dict[complement]]


list = [3,2,4]
print(bruteForce(list,6))
print(twoPassHash(list,6))
