# BOJ 1958 LCS 3

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
#include <functional>

typedef long long int ll;
using namespace std;
#define INF 1234567890
#define N 200000

const int LIMIT = 1e+9;
string a, b, c;
int dp[105][105][105];


int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> a >> b >> c;

	for (int i = 1; i <= a.length(); i++) {
		for (int j = 1; j <= b.length(); j++) {
			for (int k = 1; k <= c.length(); k++) {
				
				if (a[i-1] == b[j-1] && b[j-1] == c[k-1]) {
					dp[i][j][k] = dp[i-1][j-1][k-1] + 1;
				}

				dp[i][j][k] = max({
					dp[i][j][k],
					dp[i-1][j][k],
					dp[i][j-1][k],
					dp[i][j][k-1]
				});
				
			}
		}
	}

	cout << dp[a.length()][b.length()][c.length()];
	return 0;
}


```

---

# LCS 3

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞은 사람 | 정답 비율 |
| --------- | ----------- | ---- | ---- | --------- | --------- |
| 2 초      | 128 MB      | 3032 | 1424 | 1119      | 48.737%   |

## 문제

문자열과 놀기를 세상에서 제일 좋아하는 영식이는 오늘도 문자열 2개의 LCS(Longest Common Subsequence)를 구하고 있었다. 어느 날 영식이는 조교들이 문자열 3개의 LCS를 구하는 것을 보았다. 영식이도 도전해 보았지만 실패하고 말았다.

이제 우리가 할 일은 다음과 같다. 영식이를 도와서 문자열 3개의 LCS를 구하는 프로그램을 작성하라.

## 입력

첫 줄에는 첫 번째 문자열이, 둘째 줄에는 두 번째 문자열이, 셋째 줄에는 세 번째 문자열이 주어진다. (각 문자열의 길이는 100보다 작거나 같다)

## 출력

첫 줄에 첫 번째 문자열과 두 번째 문자열과 세 번째 문자열의 LCS의 길이를 출력한다.



## 예제 입력 1

```
abcdefghijklmn
bdefg
efg
```

## 예제 출력 1

```
3
```



## 출처

- 잘못된 조건을 찾은 사람: [myungwoo](https://www.acmicpc.net/user/myungwoo)