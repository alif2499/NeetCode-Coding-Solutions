class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        output = []
        cntZero = 0
        flag = False
        for i in nums:
            if i != 0:
                prod = prod * i
            else:
                flag = True
                cntZero += 1
                continue
        for i in range(len(nums)):
            if nums[i] != 0:
                if flag:
                    output.append(0)
                else:
                    output.append(int(prod / nums[i]))
            else:
                if cntZero > 1:
                    output.append(0)
                else:
                    output.append(prod)

        return output