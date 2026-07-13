class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digit = "123456789"
        arr=[]

        for length in range(2,10):
            for start in range(10-length):
                num=int(digit[start:length+start])

                if low<=num<=high:
                    arr.append(num)

        return arr