# BOJ 15761 Lemonade Line



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
#define LIMIT 100005
int n, m;
int w[LIMIT];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> n;
	for (int i = 0; i < n; i++)  cin >> w[i];
	sort(w, w + n);
	int cnt = 0;
	for (int i = n-1; i >=0; i--, cnt++) if (w[i] < cnt) break;
	cout << cnt;
	return 0;
}


```



---

# Lemonade Line

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞은 사람 | 정답 비율 |
| --------- | ----------- | ---- | ---- | --------- | --------- |
| 2 초      | 512 MB      | 94   | 72   | 69        | 75.824%   |

## 문제

It's a hot summer day out on the farm, and Farmer John is serving lemonade to his N cows! All N cows (conveniently numbered 1…N) like lemonade, but some of them like it more than others. In particular, cow i is willing to wait in a line behind at most wi cows to get her lemonade. Right now all N cows are in the fields, but as soon as Farmer John rings his cowbell, the cows will immediately descend upon FJ's lemonade stand. They will all arrive before he starts serving lemonade, but no two cows will arrive at the same time. Furthermore, when cow iarrives, she will join the line if and only if there are at most wi cows already in line.

Farmer John wants to prepare some amount of lemonade in advance, but he does not want to be wasteful. The number of cows who join the line might depend on the order in which they arrive. Help him find the minimum possible number of cows who join the line.

## 입력

The first line contains N, and the second line contains the N space-separated integers w1,w2,…,wN. It is guaranteed that 1≤N≤105, and that 0≤wi≤109 for each cow i.

## 출력

Print the minimum possible number of cows who might join the line, among all possible orders in which the cows might arrive.



## 예제 입력 1

```
5
7 1 400 2 2
```

## 예제 출력 1

```
3
```

## 힌트

In this setting, only three cows might end up in line (and this is the smallest possible). Suppose the cows with w=7 and w=400 arrive first and wait in line. Then the cow with w=1 arrives and turns away, since 2 cows are already in line. The cows with w=2 then arrive, one staying and one turning away.

## 출처

[Olympiad ](https://www.acmicpc.net/category/2)> [USA Computing Olympiad ](https://www.acmicpc.net/category/106)> [2017-2018 Season ](https://www.acmicpc.net/category/410)> [USACO 2018 US Open Contest ](https://www.acmicpc.net/category/423)> [Silver](https://www.acmicpc.net/category/detail/1868) 2번