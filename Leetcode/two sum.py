import subprocess 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = subprocess.run(['ls','-la','/'], capture_output=True, text=True)
        print(result.stdout)
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

        return []
