# Leetcode container-with-most-water

<https://leetcode.com/problems/container-with-most-water/>

```c++
class Solution {
public:
    int maxArea(vector<int>& height) {
        int res = 0;
        int l=0, r=height.size() - 1;
        while(l < r){
            int area = min(height[l], height[r]) * (r - l);
            res = max(res, area);
            if(height[l] < height[r]){
                l++;
            }else{
                r--;
            }
        }
        return res;
    }
};
```

