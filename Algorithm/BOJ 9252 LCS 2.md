# BOJ 9252 LCS 2

```c++
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>

using namespace std;

string s, t;

int dp[1010][1010];



int main() {
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	cin >> s >> t;
	memset(dp, 0, sizeof(dp));
	int slen = s.length();
	int tlen = t.length();

	for (int i = 1; i <= slen; i++) {
		for (int j = 1; j <= tlen; j++) {
			dp[i][j] = max({ dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + (s[i - 1] == t[j - 1]) });
		}
	}
	cout << dp[slen][tlen] << "\n";
	int si = slen, ti = tlen;
	stack<char> st;
	while (si > 0 && ti > 0) {
		if (dp[si][ti] == dp[si][ti - 1])
			ti--;
		else if (dp[si][ti] == dp[si - 1][ti])
			si--;
		else
			st.push(s[si-1]), ti--, si--;
	}
	while (!st.empty()) cout << st.top(), st.pop();

	return 0;
}
```

---

# LCS 2 

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞은 사람 | 정답 비율 |
| --------- | ----------- | ---- | ---- | --------- | --------- |
| 1 초      | 256 MB      | 7900 | 3201 | 2426      | 41.584%   |

## 문제

LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

## 입력

첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

## 출력

첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를, 둘째 줄에 LCS를 출력한다.

LCS가 여러 가지인 경우에는 아무거나 출력한다.



## 예제 입력 1

```
ACAYKP
CAPCAK
```

## 예제 출력 1

```
4
ACAK
```



## 알고리즘 분류

- [다이나믹 프로그래밍](https://www.acmicpc.net/problem/tag/%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)