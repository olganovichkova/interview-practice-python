# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i



        # seen = {}
        # for i in range(0, len(nums)):
        #      diff = target - nums[i]
        #      if diff in seen:
        #           return [seen[diff], i]
        #      else:
                #   seen[nums[i]] = i
     
        

def main():
    twoSum([1, 3, 6, 9], 4)

if __name__ == '__main__':
    main()
