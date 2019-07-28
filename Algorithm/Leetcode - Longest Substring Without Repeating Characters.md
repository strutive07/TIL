# Leetcode - Longest Substring Without Repeating Characters

  

문제 링크: <https://leetcode.com/problems/longest-substring-without-repeating-characters/>



```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l=0, r=0;
        int max_length = s.length();
        set<char> sset;
        int res = 0;
        
        while(l < max_length && r < max_length){
            if (sset.find(s[r]) != sset.end()){
                sset.erase(s[l++]);
            }else{
                sset.insert(s[r]);                
                res = max(res, r - l + 1);
                r++;
            }
        }
        return res;
    }
};
```

