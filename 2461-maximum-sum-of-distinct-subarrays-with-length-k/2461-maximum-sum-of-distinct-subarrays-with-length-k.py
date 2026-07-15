class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        windowSum = 0
        freq = {}

        for i in range(k):

            windowSum += nums[i]

            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1


        if len(freq) == k:
            maxSum = windowSum
        else:
            maxSum = 0

        for j in range(k, len(nums)):

            windowSum += nums[j]

            if nums[j] in freq:
                freq[nums[j]] += 1
            else:
                freq[nums[j]] = 1


            oldElement = nums[j - k]

            windowSum -= oldElement

            freq[oldElement] -= 1

            if freq[oldElement] == 0:
                del freq[oldElement]


            if len(freq) == k:
                maxSum = max(maxSum, windowSum)
            
        return maxSum