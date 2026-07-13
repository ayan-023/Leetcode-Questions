class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digit = "123456789"
        arr=[]

        for i in range(2,10):
            for j in range(10-i):
                num=int(digit[j:i+j])

                if low<=num<=high:
                    arr.append(num)
            arr.sort()
        return arr