# BOJ 6156 Cow Contest

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


bool check[105][105];


int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n >> m;

	for (int i = 1; i <=n; i++) {
		check[i][i] = true;
	}

	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		check[a][b] = true;
	}

	for (int k = 1; k <= n; k++) {
		for (int i = 1; i <= n; i++) {
			if (check[i][k]) {
				for (int j = 1; j <= n; j++) {
					if (check[k][j]) check[i][j] = true;
				}
			}
		}
	}
	int cnt = 0;
	for (int i = 1; i <= n; i++) {
		bool isFinish = true;
		for (int j = 1; j <= n; j++) {
			if (!(check[i][j] || check[j][i])) {
				isFinish = false;
				break;
			}
		}
		if (isFinish)
			cnt++;
	}
	cout << cnt << "\n";

	return 0;
}


```



# Cow Contest

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞은 사람 | 정답 비율 |
| --------- | ----------- | ---- | ---- | --------- | --------- |
| 1 초      | 128 MB      | 147  | 98   | 83        | 67.480%   |

## 문제

N (1 <= N <= 100) cows, conveniently numbered 1..N, are participating in a programming contest. As we all know, some cows code better than others. Each cow has a certain constant skill rating that is unique among the competitors.

The contest is conducted in several head-to-head rounds, each between two cows. If cow A has a greater skill level than cow B (1 <= A <= N; 1 <= B <= N; A != B), then cow A will always beat cow B.

Farmer John is trying to rank the cows by skill level. Given a list the results of M (1 <= M <= 4,500) two-cow rounds, determine the number of cows whose ranks can be precisely determined from the results. It is guaranteed that the results of the rounds will not be contradictory.

## 입력

- Line 1: Two space-separated integers: N and M
- Lines 2..M+1: Each line contains two space-separated integers that describe the competitors and results (the first integer, A, is the winner) of a single round of competition: A and B

## 출력

- Line 1: A single integer representing the number of cows whose ranks can be determined



## 예제 입력 1

```
5 5
4 3
4 2
3 2
1 2
2 5
```

## 예제 출력 1

```
2
```



## 출처

[Olympiad ](https://www.acmicpc.net/category/2)> [USA Computing Olympiad ](https://www.acmicpc.net/category/106)> [2007-2008 Season ](https://www.acmicpc.net/category/146)> [USACO January 2008 Contest ](https://www.acmicpc.net/category/151)> [Silver](https://www.acmicpc.net/category/detail/682) 1번

## 링크

- [PKU Judge Online](http://poj.org/problem?id=3660)