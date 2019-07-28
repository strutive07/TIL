# Leetcode - two sum

문제 링크: <https://leetcode.com/problems/two-sum/>



```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for index, num in enumerate(nums):
            print(index, num, target)
            if target - num in hashmap:
                return [hashmap[target-num], index]
            else:
                hashmap[num] = index
```

