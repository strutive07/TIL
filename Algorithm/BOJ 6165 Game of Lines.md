# BOJ 6165 Game of Lines

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
int x[205], y[205];
set<double> sset;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> x[i] >> y[i];
	}
	bool isZero = false;
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			int dx, dy;
			double dydx;
			dx = x[i] - x[j];
			dy = y[i] - y[j];
			if (dx == 0) {
				isZero = true;
			}
			else {
				dydx = (double)dy / dx;
				sset.insert(dydx);
			}
			
		}
	}
	
	int ans = sset.size();
	if (isZero)
		ans++;
	cout << ans;

	return 0;
}


```



# Game of Lines

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞은 사람 | 정답 비율 |
| --------- | ----------- | ---- | ---- | --------- | --------- |
| 1 초      | 128 MB      | 77   | 36   | 32        | 47.761%   |

## 문제

Farmer John has challenged Bessie to the following game: FJ has a board with dots marked at N (2 <= N <= 200) distinct lattice points. Dot i has the integer coordinates X_i and Y_i (-1,000 <= X_i <= 1,000; -1,000 <= Y_i <= 1,000).

Bessie can score a point in the game by picking two of the dots and drawing a straight line between them; however, she is not allowed to draw a line if she has already drawn another line that is parallel to that line. Bessie would like to know her chances of winning, so she has asked you to help find the maximum score she can obtain.

## 입력

- Line 1: A single integer: N
- Lines 2..N+1: Line i+1 describes lattice point i with two space-separated integers: X_i and Y_i.

 

## 출력

- Line 1: A single integer representing the maximal number of lines Bessie can draw, no two of which are parallel.

 



## 예제 입력 1

```
4
-1 1
-2 0
0 0
1 1
```

## 예제 출력 1

```
4
```

## 힌트

Bessie can draw lines of the following four slopes: -1, 0, 1/3, and 1.

 

## 출처

[Olympiad ](https://www.acmicpc.net/category/2)> [USA Computing Olympiad ](https://www.acmicpc.net/category/106)> [2007-2008 Season ](https://www.acmicpc.net/category/146)> [USACO February 2008 Contest ](https://www.acmicpc.net/category/152)> [Silver](https://www.acmicpc.net/category/detail/685) 1번

## 링크

- [PKU Judge Online](http://poj.org/problem?id=3668)
- [Sphere Online Judge](http://www.spoj.com/problems/LINES/)