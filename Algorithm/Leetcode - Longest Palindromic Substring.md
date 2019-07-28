# Leetcode - Longest Palindromic Substring



문제 링크: <https://leetcode.com/problems/longest-palindromic-substring/>



```c++
class Solution {
public:
    string longestPalindrome(string s) {
        int len = s.length();
        int dp[1005][1005];
        int res_l = 0, res_r = 0;
        
        memset(dp, 0, sizeof(dp));
        
        // length 1 Palindromic substring
        for(int i=0; i<len; i++){
            dp[i][i] = 1;
        }
        
        // length 2 Palindromic substring
        for(int i=1; i<len; i++){
            if (s[i] == s[i-1]){
                dp[i-1][i] = 1;
                res_l = i - 1;
                res_r = i;
            }
        }
        
        for(int i=2; i < len; i++){
            for(int j=i; j<len; j++){
                if(s[j] == s[j - i] && dp[j - i + 1][j - 1]){
                    dp[j - i][j] = 1;
                    res_l = j - i;
                    res_r = j;
                }
            }
        }
        
        return s.substr(res_l, res_r - res_l + 1);
        
    }
};
```

