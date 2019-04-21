# BOJ 1800 Telephone Lines

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
int n, p, k;

vector<pair<int, int>> vc[1005];

priority_queue<pair<int, int>> que;


bool do_dijkstra(int mid) {
	vector<int> dist(1005, INF);
	vector<bool> check(1005, false);
	dist[1] = 0;
	que.push({ 1, 0 });
	while (!que.empty()) {
		int here = que.top().first;
		int here_value = que.top().second;
		que.pop();
		if (dist[here] != here_value) continue;

		for (auto a : vc[here]) {
			int there = a.first;
			int there_dist = a.second;
			if (dist[there] > here_value + (there_dist > mid)) {
				dist[there] = here_value + (there_dist > mid);
				que.push({there, dist[there]});
			}
		}
	}
	return dist[n] <= k;
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> p >> k;

	int left = 0;
	int right = -1;
	int res = -1;
	for (int i = 0; i < p; i++) {
		int u, v, cost;
		cin >> u >> v >> cost;
		vc[u].push_back({ v, cost });
		vc[v].push_back({ u, cost });
		right = max(right, cost);
	}
	
	while (left <= right) {
		int mid = (left + right) / 2;
		bool isOk = do_dijkstra(mid);
		if (isOk) {
			right = mid - 1;
			res = mid;
		}
		else {
			left = mid + 1;
		}
	}
	cout << res;

	return 0;
}


```



# Telephone Lines

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞은 사람 | 정답 비율 |
| --------- | ----------- | ---- | ---- | --------- | --------- |
| 2 초      | 128 MB      | 240  | 87   | 66        | 34.197%   |

## 문제

Farmer John wants to set up a telephone line at his farm. Unfortunately, the phone company is uncooperative, so he needs to pay for some of the cables required to connect his farm to the phone system.

There are N (1 <= N <= 1,000) forlorn telephone poles conveniently numbered 1..N that are scattered around Farmer John's property; no cables connect any them.  A total of P (1 <= P <= 10,000) pairs of poles can be connected by a cable; the rest are too far apart.

The i-th cable can connect the two distinct poles A_i and B_i, with length L_i (1 <= L_i <= 1,000,000) units if used. The input data set never names any {A_i,B_i} pair more than once. Pole 1 is already connected to the phone system, and pole N is at the farm. Poles 1 and N need to be connected by a path of cables; the rest of the poles might be used or might not be used.

As it turns out, the phone company is willing to provide Farmer John with K (0 <= K < N) lengths of cable for free. Beyond that he will have to pay a price equal to the length of the longest remaining cable he requires (each pair of poles is connected with a separate cable), or 0 if he does not need any additional cables.

Determine the minimum amount that Farmer John must pay.

## 입력

\* Line 1: Three space-separated integers: N, P, and K

\* Lines 2..P+1: Line i+1 contains the three space-separated integers: A_i, B_i, and L_i

## 출력

\* Line 1: A single integer, the minimum amount Farmer John can pay. If it is impossible to connect the farm to the phone company, print -1.



## 예제 입력 1

```
5 7 1
1 2 5
3 1 4
2 4 8
3 2 3
5 2 9
3 4 7
4 5 6
```

## 예제 출력 1

```
4
```

## 힌트

If pole 1 is connected to pole 3, pole 3 to pole 2, and pole 2 to pole 5 then Farmer John requires cables of length 4, 3, and 9. The phone company will provide the cable of length 9, so the longest cable needed has length 4.

## 출처

[Olympiad ](https://www.acmicpc.net/category/2)> [USA Computing Olympiad ](https://www.acmicpc.net/category/106)> [2007-2008 Season ](https://www.acmicpc.net/category/146)> [USACO January 2008 Contest ](https://www.acmicpc.net/category/151)> [Silver](https://www.acmicpc.net/category/detail/682) 3번

- 문제의 오타를 찾은 사람: [adream](https://www.acmicpc.net/user/adream) [jh05013](https://www.acmicpc.net/user/jh05013) [kks227](https://www.acmicpc.net/user/kks227)
- 문제를 번역한 사람: [author9](https://www.acmicpc.net/user/author9)

## 링크

- [PKU Judge Online](http://poj.org/problem?id=3662)