# BOJ 1757 Running

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
typedef long long int ll;
using namespace std;
#define INF 1234567890
#define LIMIT 1
int n, m;
int value[10005], dp[10005];
int res = -1;




int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> value[i];
	}
	
	for(int i=0; i<n; i++){
		if (dp[i + 1] < dp[i]) {
			dp[i + 1] = dp[i];
		}
		int sum = dp[i];
		int here = i;

		for (int j = 0; j < m; j++) {
			if (here > n)
				break;
			sum += value[i + j];
			here += 2;
			if (sum > dp[here]) dp[here] = sum;
		}
	}

	cout << dp[n];

	return 0;
}


```



# Running  

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞은 사람 | 정답 비율 |
| --------- | ----------- | ---- | ---- | --------- | --------- |
| 2 초      | 128 MB      | 153  | 56   | 48        | 40.000%   |

## 문제

The cows are trying to become better athletes, so Bessie is running on a track for exactly N (1 <= N <= 10,000) minutes. During each minute, she can choose to either run or rest for the whole minute.

The ultimate distance Bessie runs, though, depends on her 'exhaustion factor', which starts at 0. When she chooses to run in minute i, she will run exactly a distance of D_i (1 <= D_i <= 1,000) and her exhaustion factor will increase by 1 -- but must never be allowed to exceed M (1 <= M <= 500).  If she chooses to rest, her exhaustion factor will decrease by 1 for each minute she rests. She cannot commence running again until her exhaustion factor reaches 0. At that point, she can choose to run or rest.

At the end of the N minute workout, Bessie's exaustion factor must be exactly 0, or she will not have enough energy left for the rest of the day.

Find the maximal distance Bessie can run.

## 입력

\* Line 1: Two space-separated integers: N and M

\* Lines 2..N+1: Line i+1 contains the single integer: D_i

## 출력

\* Line 1: A single integer representing the largest distance Bessie can run while satisfying the conditions.

 



## 예제 입력 1

```
5 2
5
3
4
2
10
```

## 예제 출력 1

```
9
```

## 힌트

Bessie runs during the first minute (distance=5), rests during the second minute, runs for the third (distance=4), and rests for the fourth and fifth. Note that Bessie cannot run on the fifth minute because she would not end with a rest factor of 0.

 

## 출처

[Olympiad ](https://www.acmicpc.net/category/2)> [USA Computing Olympiad ](https://www.acmicpc.net/category/106)> [2007-2008 Season ](https://www.acmicpc.net/category/146)> [USACO January 2008 Contest ](https://www.acmicpc.net/category/151)> [Silver](https://www.acmicpc.net/category/detail/682) 2번

- 문제를 번역한 사람: [author9](https://www.acmicpc.net/user/author9)

## 링크

- [PKU Judge Online](http://poj.org/problem?id=3661)