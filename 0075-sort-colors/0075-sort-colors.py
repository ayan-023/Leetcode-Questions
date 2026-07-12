class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        red=0
        white=0
        blue=n-1

        while (white<=blue):
            if nums[white]==0:
                nums[white]=nums[red]
                nums[red]=0
                white+=1
                red+=1
            elif nums[white]==1:
                white+=1
            else:
                nums[white]=nums[blue]
                nums[blue]=2
                blue-=1

        